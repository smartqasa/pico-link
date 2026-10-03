# __init__.py — Integration entry point
from __future__ import annotations

import asyncio
import logging
from copy import deepcopy
from typing import Any

import voluptuous as vol
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import EVENT_HOMEASSISTANT_STOP
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady, HomeAssistantError
from homeassistant.helpers.typing import ConfigType

from .config import PicoConfig, parse_pico_config
from .const import DOMAIN
from .controller import PicoController
from .placeholder import async_setup_placeholder
from .ui_config import entry_config, validate_document

_LOGGER = logging.getLogger(__name__)


async def async_setup(
    hass: HomeAssistant,
    config: ConfigType,
) -> bool:
    """Set up Pico Link from configuration.yaml."""
    root = config.get(DOMAIN)
    runtime = hass.data.setdefault(DOMAIN, {})
    runtime["yaml_config"] = deepcopy(root)
    method = root.get("config_method") if isinstance(root, dict) else None
    if method is not None and method not in ("yaml", "ui"):
        _LOGGER.error("pico_link.config_method must be yaml or ui")
        return False
    runtime["config_method"] = method
    from .panel import async_setup_panel

    await async_setup_panel(hass)
    await async_setup_placeholder(hass, config)
    # A saved UI entry owns the installation, including when disabled. Never
    # silently activate a second set of controllers from leftover YAML.
    if method == "ui" or (method != "yaml" and hass.config_entries.async_entries(DOMAIN)):
        if root is not None:
            _LOGGER.info("Pico Link is managed in the UI; its YAML is not loaded")
        return True

    if root is None:
        _LOGGER.debug(
            "No %s configuration found in configuration.yaml",
            DOMAIN,
        )
        return True

    if not isinstance(root, dict):
        _LOGGER.error(
            "Invalid %s configuration: expected a mapping with optional "
            "'defaults' and required 'devices', got %s",
            DOMAIN,
            type(root).__name__,
        )
        return False

    # =============================================================
    # DEFAULTS
    # =============================================================

    raw_defaults = root.get("defaults")

    if raw_defaults is None:
        defaults: dict[str, Any] = {}
    elif isinstance(raw_defaults, dict):
        defaults = raw_defaults
    else:
        _LOGGER.error(
            "Invalid '%s.defaults' configuration: expected a mapping, got %s",
            DOMAIN,
            type(raw_defaults).__name__,
        )
        return False

    # =============================================================
    # DEVICES
    # =============================================================

    device_list = root.get("devices")

    if not isinstance(device_list, list):
        _LOGGER.error(
            "Invalid '%s.devices' configuration: expected a list, got %s",
            DOMAIN,
            type(device_list).__name__,
        )
        return False

    controllers: list[PicoController] = []

    # Track the configuration entry where each physical Pico was first
    # registered. A second entry for the same device would otherwise
    # create another controller subscribed to the same Pico events.
    configured_device_entries: dict[str, int] = {}

    for index, device_raw in enumerate(
        device_list,
        start=1,
    ):
        if not isinstance(device_raw, dict):
            _LOGGER.error(
                "Invalid %s device entry %s: expected a mapping, got %s: %r",
                DOMAIN,
                index,
                type(device_raw).__name__,
                device_raw,
            )
            continue

        try:
            pico_config: PicoConfig = parse_pico_config(
                hass,
                defaults,
                device_raw,
            )
        except ValueError as err:
            device_identifier = (
                device_raw.get("device_id") or device_raw.get("name") or "<unknown>"
            )
            device_type = device_raw.get("type") or "<unknown>"

            _LOGGER.error(
                "Invalid %s device entry %s (device=%s, type=%s): %s",
                DOMAIN,
                index,
                device_identifier,
                device_type,
                err,
            )
            continue

        first_entry = configured_device_entries.get(pico_config.device_id)

        if first_entry is not None:
            _LOGGER.error(
                "Invalid %s device entry %s: Pico device %s is "
                "already configured by entry %s",
                DOMAIN,
                index,
                pico_config.device_id,
                first_entry,
            )
            continue

        controller = PicoController(
            hass,
            pico_config,
        )

        try:
            await controller.async_start()
        except (ValueError, vol.Invalid, HomeAssistantError) as err:
            await controller.async_stop()
            _LOGGER.error(
                "Invalid Pico %s script configuration: %s", pico_config.device_id, err
            )
            continue
        configured_device_entries[pico_config.device_id] = index
        controllers.append(controller)

    # =============================================================
    # COMPLETED SETUP
    # =============================================================

    if not controllers:
        _LOGGER.warning(
            "%s is configured, but no valid Pico devices were created",
            DOMAIN,
        )
        return True

    runtime["controllers"] = controllers
    runtime["source"] = "yaml"

    # =============================================================
    # SHUTDOWN
    # =============================================================

    async def _async_stop(_: Any) -> None:
        await asyncio.gather(*(controller.async_stop() for controller in controllers))

    runtime["unsub_stop"] = hass.bus.async_listen_once(
        EVENT_HOMEASSISTANT_STOP,
        _async_stop,
    )

    _LOGGER.info(
        "%s initialized with %s controller(s)",
        DOMAIN,
        len(controllers),
    )

    return True


async def _async_stop_controllers(hass: HomeAssistant) -> None:
    runtime = hass.data[DOMAIN]
    if unsub := runtime.pop("unsub_stop", None):
        unsub()
    controllers = runtime.pop("controllers", [])
    await asyncio.gather(*(controller.async_stop() for controller in controllers))
    runtime.pop("source", None)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Load one UI document without concurrent YAML or partial controllers."""
    runtime = hass.data.setdefault(DOMAIN, {})
    if runtime.get("config_method") == "yaml":
        # Explicit YAML wins even if an older UI document is still saved.
        # Keep that document available for a later deliberate switch back.
        _LOGGER.info("Pico Link UI settings are inactive because config_method is yaml")
        return True
    if runtime.get("entry_id") not in (None, entry.entry_id):
        raise HomeAssistantError("Only one Pico Link configuration is supported")
    controllers = []
    try:
        configs = await validate_document(hass, entry_config(entry))
        # Validation precedes retiring YAML. Never subscribe new controllers
        # until the previous ones have finished stopping.
        for conf in configs:
            controllers.append(PicoController(hass, conf))
        await _async_stop_controllers(hass)
        for controller in controllers:
            await controller.async_start()
    except Exception as err:
        await asyncio.gather(*(controller.async_stop() for controller in controllers))
        raise ConfigEntryNotReady(f"Cannot load Pico Link settings: {err}") from err
    runtime["controllers"] = controllers
    runtime["entry_id"] = entry.entry_id
    runtime["source"] = "ui"

    async def stop(_event):
        # The one-shot listener has already removed itself at this point.
        runtime.pop("unsub_stop", None)
        await _async_stop_controllers(hass)

    runtime["unsub_stop"] = hass.bus.async_listen_once(EVENT_HOMEASSISTANT_STOP, stop)
    entry.async_on_unload(entry.add_update_listener(_async_options_updated))
    return True


async def _async_options_updated(hass: HomeAssistant, entry: ConfigEntry) -> None:
    await hass.config_entries.async_reload(entry.entry_id)


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Drain scripts and timers before a reload replaces their controllers."""
    runtime = hass.data.get(DOMAIN, {})
    if runtime.get("entry_id") == entry.entry_id:
        await _async_stop_controllers(hass)
        runtime.pop("entry_id", None)
    return True
