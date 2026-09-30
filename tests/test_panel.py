"""Exercise the panel's real authenticated API and configuration ownership."""

from copy import deepcopy
from unittest.mock import AsyncMock, patch

import pytest
from homeassistant.config_entries import ConfigEntryDisabler
from homeassistant.helpers import device_registry as dr
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.pico_link.const import DOMAIN
from custom_components.pico_link.panel import async_setup_panel, panel_state
from custom_components.pico_link.ui_config import entry_config


async def request(client, message):
    await client.send_json(message)
    return await client.receive_json()


@pytest.fixture
async def panel(hass, registry_pico, register_pico, hass_ws_client):
    device = register_pico(model="Test (Pico3ButtonRaiseLower)")
    entry = MockConfigEntry(
        domain=DOMAIN,
        unique_id=DOMAIN,
        data={
            "devices": [{"device_id": device.id, "lights": ["light.desk"]}],
            "defaults": {},
        },
    )
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    client = await hass_ws_client(hass)
    return client, entry, device


async def test_read_does_not_modify_or_reload(hass, panel):
    client, entry, device = panel
    old = hass.data[DOMAIN]["controllers"][0]
    result = await request(client, {"id": 1, "type": "pico_link/config"})
    assert result["success"]
    state = result["result"]
    assert state["document"] == entry_config(entry)
    assert state["catalog"][0]["id"] == device.id
    assert state["catalog"][0]["type"] == "3BRL"
    assert old is hass.data[DOMAIN]["controllers"][0]


async def test_save_reloads_once_and_preserves_other_actions(
    hass, panel, registry_pico
):
    client, entry, device = panel
    state = panel_state(hass)
    document = deepcopy(state["document"])
    document["devices"][0]["on_tap"] = [
        {
            "action": "light.turn_on",
            "target": {"entity_id": "lights"},
            "data": {"brightness_pct": 42},
        }
    ]
    document["defaults"] = {"mode": "queued", "max": 4}
    old = hass.data[DOMAIN]["controllers"][0]
    result = await request(
        client,
        {
            "id": 1,
            "type": "pico_link/save",
            "revision": state["revision"],
            "document": document,
        },
    )
    assert result["success"]
    await hass.async_block_till_done()
    assert old._unsub_event is None
    assert len(hass.data[DOMAIN]["controllers"]) == 1
    assert entry_config(entry)["devices"] == document["devices"]
    registry_pico.tap("on", device=device.id)
    await registry_pico.drain()
    assert len(registry_pico.calls) == 1
    assert registry_pico.calls[0][2]["brightness_pct"] == 42
    assert registry_pico.calls[0][2]["entity_id"] == ["light.desk"]


@pytest.mark.parametrize("bad", ["duplicate", "actions", "empty_target", "max"])
async def test_invalid_save_preserves_running_config(hass, panel, bad):
    client, entry, _ = panel
    state = panel_state(hass)
    original = entry_config(entry)
    old = hass.data[DOMAIN]["controllers"][0]
    document = deepcopy(original)
    if bad == "duplicate":
        document["devices"] *= 2
    if bad == "actions":
        document["devices"][0]["on_tap"] = [{"nonsense": True}]
    if bad == "empty_target":
        document["devices"][0]["lights"] = []
    if bad == "max":
        document["defaults"]["max"] = 0
    result = await request(
        client,
        {
            "id": 1,
            "type": "pico_link/save",
            "revision": state["revision"],
            "document": document,
        },
    )
    assert not result["success"]
    assert result["error"]["code"] == "invalid_config"
    assert entry_config(entry) == original
    assert hass.data[DOMAIN]["controllers"] == [old]


async def test_two_tabs_cannot_overwrite_each_other(hass, panel):
    client, entry, _ = panel
    state = panel_state(hass)
    document = deepcopy(state["document"])
    document["devices"][0]["hold_time_ms"] = 500
    for number, expected in [(1, True), (2, False)]:
        result = await request(
            client,
            {
                "id": number,
                "type": "pico_link/save",
                "revision": state["revision"],
                "document": document,
            },
        )
        assert result["success"] is expected
    assert result["error"]["code"] == "conflict"
    assert entry_config(entry)["devices"][0]["hold_time_ms"] == 500


async def test_change_during_validation_is_rejected(hass, panel):
    client, entry, _ = panel
    state = panel_state(hass)

    async def concurrent_save(*args):
        document = entry_config(entry)
        document["defaults"]["mode"] = "parallel"
        hass.config_entries.async_update_entry(entry, options=document)

    with patch(
        "custom_components.pico_link.panel.validate_document",
        side_effect=concurrent_save,
    ):
        result = await request(
            client,
            {
                "id": 1,
                "type": "pico_link/save",
                "revision": state["revision"],
                "document": state["document"],
            },
        )
    assert result["error"]["code"] == "conflict"
    assert entry_config(entry)["defaults"]["mode"] == "parallel"


@pytest.mark.parametrize("reason", ["yaml", "disabled"])
async def test_inactive_source_cannot_be_saved(hass, panel, reason):
    client, entry, _ = panel
    if reason == "yaml":
        hass.data[DOMAIN]["config_method"] = "yaml"
    else:
        await hass.config_entries.async_set_disabled_by(
            entry.entry_id, ConfigEntryDisabler.USER
        )
    state = panel_state(hass)
    assert state["read_only"]
    result = await request(
        client,
        {
            "id": 1,
            "type": "pico_link/save",
            "revision": state["revision"],
            "document": state["document"],
        },
    )
    assert result["error"]["code"] == "read_only"


async def test_import_is_draft_until_explicit_save(
    hass, registry_pico, register_pico, hass_ws_client
):
    device = register_pico(model="Test (Pico3ButtonRaiseLower)")
    await registry_pico.setup(
        [{"name": device.name, "lights": "light.desk", "middle_button": "default"}],
        {
            "middle_button": [
                {"action": "light.turn_on", "target": {"entity_id": "lights"}}
            ]
        },
    )
    old = hass.data[DOMAIN]["controllers"][0]
    yaml = deepcopy(hass.data[DOMAIN]["yaml_config"])
    client = await hass_ws_client(hass)
    result = await request(client, {"id": 1, "type": "pico_link/import"})
    assert result["success"]
    assert hass.data[DOMAIN]["controllers"] == [old]
    assert not hass.config_entries.async_entries(DOMAIN)
    document = result["result"]["document"]
    assert document["devices"][0]["device_id"] == device.id
    result = await request(
        client,
        {
            "id": 2,
            "type": "pico_link/save",
            "revision": panel_state(hass)["revision"],
            "document": document,
        },
    )
    assert result["success"]
    await hass.async_block_till_done()
    assert old._unsub_event is None
    assert hass.data[DOMAIN]["source"] == "ui"
    assert hass.data[DOMAIN]["yaml_config"] == yaml


async def test_remove_missing_remote_and_save_empty(hass, panel):
    client, entry, device = panel
    dr.async_get(hass).async_remove_device(device.id)
    state = panel_state(hass)
    assert not state["catalog"]
    result = await request(
        client,
        {
            "id": 1,
            "type": "pico_link/save",
            "revision": state["revision"],
            "document": {"devices": []},
        },
    )
    assert result["success"]
    await hass.async_block_till_done()
    assert entry_config(entry)["devices"] == []
    assert not hass.data[DOMAIN]["controllers"]


@pytest.mark.parametrize(
    "command", ["pico_link/config", "pico_link/import", "pico_link/save"]
)
async def test_non_admin_cannot_read_or_write(
    hass, panel, hass_ws_client, hass_read_only_access_token, command
):
    _, entry, _ = panel
    client = await hass_ws_client(hass, access_token=hass_read_only_access_token)
    message = {"id": 1, "type": command}
    if command == "pico_link/save":
        message.update(document={"devices": []}, revision=panel_state(hass)["revision"])
    result = await request(client, message)
    assert not result["success"]
    assert result["error"]["code"] == "unauthorized"
    assert entry_config(entry)["devices"]


async def test_register_once_with_admin_restriction(hass, panel):
    hass.config.components.add("frontend")
    with (
        patch.object(
            hass.http, "async_register_static_paths", new_callable=AsyncMock
        ) as paths,
        patch(
            "custom_components.pico_link.panel.panel_custom.async_register_panel",
            new_callable=AsyncMock,
        ) as register,
    ):
        await async_setup_panel(hass)
        await async_setup_panel(hass)
    paths.assert_awaited_once()
    register.assert_awaited_once()
    assert register.call_args.kwargs["require_admin"] is True
    assert register.call_args.kwargs["config_panel_domain"] == DOMAIN


async def test_frontend_setup_goes_to_workspace(hass, registry_pico):
    hass.config.components.add("frontend")
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": "user"}
    )
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {"config_method": "ui"}
    )
    assert result["step_id"] == "workspace"
    with patch(
        "custom_components.pico_link.panel.async_setup_panel", new_callable=AsyncMock
    ):
        result = await hass.config_entries.flow.async_configure(result["flow_id"], {})
        await hass.async_block_till_done()
    assert result["type"] == "create_entry"
    assert entry_config(result["result"])["devices"] == []


async def test_fallback_editor_cannot_overwrite_panel_save(hass, panel):
    client, entry, _ = panel
    editor = await hass.config_entries.options.async_init(entry.entry_id)
    state = panel_state(hass)
    state["document"]["defaults"]["mode"] = "parallel"
    assert (
        await request(
            client,
            {
                "id": 1,
                "type": "pico_link/save",
                "revision": state["revision"],
                "document": state["document"],
            },
        )
    )["success"]
    result = await hass.config_entries.options.async_configure(
        editor["flow_id"], {"next_step_id": "save"}
    )
    assert result["errors"] == {"base": "invalid_config"}
    assert "another editor" in result["description_placeholders"]["detail"]
    assert entry_config(entry)["defaults"]["mode"] == "parallel"
