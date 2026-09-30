"""Admin-only custom panel using the existing configuration document."""

from __future__ import annotations

import asyncio
import hashlib
import json
from collections.abc import Mapping
from copy import deepcopy
from pathlib import Path

import voluptuous as vol
from homeassistant.components import panel_custom, websocket_api
from homeassistant.components.http import StaticPathConfig
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers import area_registry as ar
from homeassistant.helpers import device_registry as dr
from homeassistant.loader import async_get_integration

from .const import DOMAIN
from .ui_config import (
    DEVICE_SETTINGS,
    NUMBERS,
    entry_config,
    import_document,
    remote_type,
    validate_document,
)

ERRORS = (ValueError, TypeError, vol.Invalid, HomeAssistantError)


def revision(hass) -> str:
    """Include entry identity and source so stale tabs cannot overwrite changes."""
    entries = hass.config_entries.async_entries(DOMAIN)
    state = [
        hass.data.get(DOMAIN, {}).get("config_method"),
        [(e.entry_id, e.disabled_by, entry_config(e)) for e in entries],
    ]
    return hashlib.sha256(json.dumps(state, sort_keys=True).encode()).hexdigest()


def panel_state(hass) -> dict:
    entries = hass.config_entries.async_entries(DOMAIN)
    entry = entries[0] if entries else None
    runtime = hass.data.get(DOMAIN, {})
    yaml_mode = runtime.get("config_method") == "yaml"
    document = entry_config(entry) if entry else {"defaults": {}, "devices": []}
    lutron = {e.entry_id for e in hass.config_entries.async_entries("lutron_caseta")}
    devices = dr.async_get(hass).devices
    areas = ar.async_get(hass)
    catalog = []
    for device in devices.values() if isinstance(devices, Mapping) else devices:
        if not device.config_entries.intersection(lutron):
            continue
        try:
            kind = remote_type(hass, {"device_id": device.id})
        except ERRORS:
            kind = None
        area = areas.async_get_area(device.area_id) if device.area_id else None
        catalog.append(
            {
                "id": device.id,
                "name": device.name_by_user or device.name or "Unnamed Lutron device",
                "model": device.model,
                "type": kind,
                "area": area.name if area else "",
            }
        )
    return {
        "document": document,
        "revision": revision(hass),
        "configured": entry is not None,
        "read_only": yaml_mode or bool(entry and entry.disabled_by),
        "reason": "yaml"
        if yaml_mode
        else "disabled"
        if entry and entry.disabled_by
        else None,
        "yaml_available": isinstance(runtime.get("yaml_config"), dict)
        and bool(runtime["yaml_config"].get("devices")),
        "catalog": sorted(catalog, key=lambda d: (d["name"].casefold(), d["id"])),
        "numbers": NUMBERS,
        "device_settings": DEVICE_SETTINGS,
    }


async def async_setup_panel(hass) -> None:
    runtime = hass.data.setdefault(DOMAIN, {})
    if not runtime.get("panel_api"):
        for command in (ws_config, ws_import, ws_save):
            websocket_api.async_register_command(hass, command)
        runtime["panel_api"] = True
        runtime["panel_lock"] = asyncio.Lock()
    # A headless installation needs no frontend, but keeps the same controllers.
    if "frontend" not in hass.config.components or runtime.get("panel_registered"):
        return
    integration = await async_get_integration(hass, DOMAIN)
    await hass.http.async_register_static_paths(
        [
            StaticPathConfig(
                "/pico_link_static", str(Path(__file__).parent / "frontend"), False
            )
        ]
    )
    await panel_custom.async_register_panel(
        hass,
        frontend_url_path="pico-link",
        webcomponent_name="pico-link-panel",
        sidebar_title="Pico Link",
        sidebar_icon="mdi:remote",
        module_url=f"/pico_link_static/pico-link-panel.js?v={integration.version}",
        require_admin=True,
        config_panel_domain=DOMAIN,
    )
    runtime["panel_registered"] = True


@websocket_api.websocket_command({vol.Required("type"): "pico_link/config"})
@websocket_api.require_admin
def ws_config(hass, connection, msg):
    connection.send_result(msg["id"], panel_state(hass))


@websocket_api.websocket_command({vol.Required("type"): "pico_link/import"})
@websocket_api.require_admin
@websocket_api.async_response
async def ws_import(hass, connection, msg):
    """Return a draft only. Import never writes a file or stops YAML controllers."""
    try:
        source = deepcopy(hass.data[DOMAIN].get("yaml_config") or {})
        source.setdefault("devices", [])
        document = await import_document(hass, source)
    except ERRORS as err:
        connection.send_error(msg["id"], "invalid_config", str(err))
        return
    connection.send_result(msg["id"], {"document": document})


@websocket_api.websocket_command(
    {
        vol.Required("type"): "pico_link/save",
        vol.Required("document"): dict,
        vol.Required("revision"): str,
    }
)
@websocket_api.require_admin
@websocket_api.async_response
async def ws_save(hass, connection, msg):
    """Validate the full draft and reject concurrent or inactive-source writes."""
    async with hass.data[DOMAIN]["panel_lock"]:
        state = panel_state(hass)
        if state["read_only"]:
            connection.send_error(
                msg["id"],
                "read_only",
                "UI settings are inactive. Select UI configuration and enable Pico Link first.",
            )
            return
        if msg["revision"] != state["revision"]:
            connection.send_error(
                msg["id"],
                "conflict",
                "Settings changed in another editor. Reload the saved settings before editing again.",
            )
            return
        try:
            document = deepcopy(msg["document"])
            document["config_method"] = "ui"
            await validate_document(hass, document)
        except ERRORS as err:
            connection.send_error(msg["id"], "invalid_config", str(err))
            return
        # Validation can yield. Recheck changes from a setup/options flow too.
        if msg["revision"] != revision(hass):
            connection.send_error(
                msg["id"],
                "conflict",
                "Settings changed while validating. Reload the saved settings and try again.",
            )
            return
        entries = hass.config_entries.async_entries(DOMAIN)
        if entries:
            hass.config_entries.async_update_entry(entries[0], options=document)
        else:
            result = await hass.config_entries.flow.async_init(
                DOMAIN, context={"source": "panel"}, data=document
            )
            if result["type"] != "create_entry":
                connection.send_error(
                    msg["id"],
                    "setup_failed",
                    "Pico Link setup could not finish. Reload and try again.",
                )
                return
        connection.send_result(msg["id"], panel_state(hass))
