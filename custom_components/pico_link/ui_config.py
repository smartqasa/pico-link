"""Validation shared by the configuration editor and config-entry setup."""

from __future__ import annotations

import json
from copy import deepcopy
from typing import Any

from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.script import async_validate_actions_config

from .color_cycle import CYCLE_ACTION, normalize_palette
from .config import (
    PicoConfig,
    _detect_pico_type,
    _expand_action_placeholders,
    parse_pico_config,
)
from .const import DOMAIN_ENTITY_FIELDS, VALID_PICO_TYPES
from .placeholder import placeholder_entity_id
from .script_runner import script_schema

# key: (minimum, maximum, built-in default, unit)
NUMBERS = {
    "hold_time_ms": (100, 2000, 400, "ms"),
    "double_tap_time_ms": (100, 2000, 300, "ms"),
    "step_time_ms": (100, 2000, 650, "ms"),
    "light_on_pct": (1, 100, 100, "%"),
    "light_low_pct": (1, 99, 5, "%"),
    "light_step_pct": (1, 25, 10, "%"),
    "light_transition_on": (0, 300, 0, "s"),
    "light_transition_off": (0, 300, 0, "s"),
    "cover_open_pos": (1, 100, 100, "%"),
    "cover_step_pct": (1, 25, 10, "%"),
    "fan_on_pct": (1, 100, 100, "%"),
    "media_player_vol_step": (1, 20, 10, "%"),
}
TIMING = ("hold_time_ms", "double_tap_time_ms", "step_time_ms")
DEVICE_SETTINGS = {
    "light": tuple(key for key in NUMBERS if key.startswith("light_")),
    "cover": ("cover_open_pos", "cover_step_pct"),
    "fan": ("fan_on_pct",),
    "media_player": ("media_player_vol_step",),
    "switch": (),
}
MODES = ("single", "restart", "queued", "parallel")
LOG_LEVELS = ("silent", "debug", "info", "warning", "error", "critical")


def entry_config(entry) -> dict[str, Any]:
    """Options are a complete saved document, never a partial overlay."""
    return deepcopy(dict(entry.options if "devices" in entry.options else entry.data))


def remote_type(hass, raw) -> str:
    """UI selections must identify a registered Lutron device."""
    device = dr.async_get(hass).async_get(raw.get("device_id", ""))
    lutron = {e.entry_id for e in hass.config_entries.async_entries("lutron_caseta")}
    if device is None or not device.config_entries.intersection(lutron):
        raise ValueError("Choose a device from the Lutron Caséta integration.")
    explicit = raw.get("type")
    if explicit is not None:
        if explicit not in VALID_PICO_TYPES:
            raise ValueError("Choose a supported Pico layout or Automatic.")
        return explicit
    return _detect_pico_type(hass, device.id)


def remote_name(hass, raw) -> str:
    device = dr.async_get(hass).async_get(raw.get("device_id", ""))
    return (
        ((device.name_by_user or device.name) if device else None)
        or raw.get("name")
        or "Unavailable Pico"
    )


async def validate_actions(hass, actions, placeholders=None) -> None:
    """Validate without persisting HA's normalized Template objects."""
    if not isinstance(actions, list):
        raise ValueError("Actions must be a sequence.")
    if placeholders is None:
        placeholders = {
            field: [f"{domain}.pico_link_example"]
            for domain, field in DOMAIN_ENTITY_FIELDS.items()
        }
        if light_placeholder := placeholder_entity_id(hass):
            placeholders[light_placeholder] = placeholders["lights"]
    expanded = _expand_action_placeholders(actions, placeholders, "actions")
    await async_validate_actions_config(hass, script_schema(expanded))


async def validate_document(hass, root) -> list[PicoConfig]:
    """Validate every remote before allowing a UI save or import."""
    # Reject YAML-only objects before handing a document to HA's JSON storage.
    json.dumps(root, allow_nan=False)
    if not isinstance(root, dict) or not isinstance(root.get("devices"), list):
        raise ValueError("Configuration needs a devices list.")
    defaults = root.get("defaults")
    if defaults is None:
        defaults = {}
    if not isinstance(defaults, dict):
        raise ValueError("Shared defaults must be a mapping.")
    if defaults.get("mode", "single") not in MODES:
        raise ValueError("Choose a supported run mode in shared defaults.")
    limit = defaults.get("max", 10)
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 1:
        raise ValueError("The shared run limit must be a positive integer.")
    severity = defaults.get("max_exceeded", "warning")
    if not isinstance(severity, str) or severity.lower() not in LOG_LEVELS:
        raise ValueError("Choose a supported rejection log level in shared defaults.")
    if "continue_on_error" in defaults:
        raise ValueError("Continue on error belongs to an action, not shared defaults.")
    for key in ("stop_tap", "stop_hold", "stop_double_tap", "middle_button"):
        if key in defaults and defaults[key] != CYCLE_ACTION:
            await validate_actions(hass, defaults[key])
    if "color_palette" in defaults:
        normalize_palette(defaults["color_palette"])
    configs = []
    seen = set()
    for raw in root["devices"]:
        if not isinstance(raw, dict):
            raise ValueError("Each Pico must be a mapping.")
        conf = parse_pico_config(hass, defaults, raw)
        if conf.device_id in seen:
            raise ValueError("The same Pico cannot be added more than once.")
        seen.add(conf.device_id)
        for actions in (
            conf.middle_button,
            *conf.buttons.values(),
            *conf.overrides.values(),
        ):
            await validate_actions(hass, actions, {})
        configs.append(conf)
    return configs


async def import_document(hass, root) -> dict[str, Any]:
    """Copy YAML only after validating all remotes; pin names to registry IDs."""
    copied = deepcopy(root)
    configs = await validate_document(hass, copied)
    for raw, conf in zip(copied["devices"], configs, strict=True):
        raw["device_id"] = conf.device_id
        if "type" in raw:
            raw["type"] = conf.type
    return copied
