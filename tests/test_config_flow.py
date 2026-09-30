"""Exercise real setup/options flows, persistence and controller ownership."""

import asyncio
from copy import deepcopy
from unittest.mock import patch

import pytest
from homeassistant.config_entries import ConfigEntryState
from homeassistant.data_entry_flow import FlowResultType
from homeassistant.helpers.script import DATA_SCRIPTS
from homeassistant.setup import async_setup_component
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.pico_link.const import DOMAIN
from custom_components.pico_link.ui_config import import_document, validate_document


async def advance(hass, result, data=None, *, options=False, menu=None):
    manager = hass.config_entries.options if options else hass.config_entries.flow
    return await manager.async_configure(
        result["flow_id"], {"next_step_id": menu} if menu else data or {}
    )


async def begin(hass):
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": "user"}
    )
    if result.get("step_id") == "method":
        result = await advance(hass, result, {"config_method": "ui"})
    return result


def remote(register_pico, kind="Pico3ButtonRaiseLower", serial="pico"):
    return register_pico(model=f"Test ({kind})", serial=serial)


def doc(device, **extra):
    return {
        "defaults": {},
        "devices": [{"device_id": device.id, "lights": ["light.desk"], **extra}],
    }


@pytest.mark.parametrize(
    "kind", ["Pico2Button", "PaddleSwitchPico", "Pico3ButtonRaiseLower"]
)
async def test_create_entry_controls_once_and_survives_reload(
    hass, registry_pico, register_pico, kind
):
    device = remote(register_pico, kind)
    result = await begin(hass)
    assert result["step_id"] == "editor"
    result = await advance(hass, result, menu="add")
    result = await advance(hass, result, {"device_id": device.id, "type": "automatic"})
    assert result["step_id"] == "assignment"
    result = await advance(hass, result, {"domain": "light"})
    result = await advance(hass, result, {"entities": ["light.desk"]})
    result = await advance(hass, result, menu="done")
    result = await advance(hass, result, menu="save")
    assert DOMAIN not in hass.data or not hass.data[DOMAIN].get("controllers")
    result = await advance(hass, result)
    assert result["type"] is FlowResultType.CREATE_ENTRY
    entry = result["result"]
    await hass.async_block_till_done()
    assert entry.state is ConfigEntryState.LOADED
    assert "type" not in entry.data["devices"][0]
    for _ in range(2):
        registry_pico.tap(
            "on",
            device=device.id,
            kind="3BRL"
            if kind.endswith("RaiseLower")
            else "P2B"
            if kind == "PaddleSwitchPico"
            else "2B",
        )
        await registry_pico.drain()
        assert registry_pico.calls[-1][:2] == ("light", "turn_on")
        assert await hass.config_entries.async_reload(entry.entry_id)
    assert len(registry_pico.calls) == 2
    duplicate = await begin(hass)
    assert duplicate["reason"] == "already_configured"


async def test_explicit_import_preserves_yaml_and_replaces_controller(
    hass, registry_pico, register_pico
):
    device = remote(register_pico)
    raw = {"name": device.name, "lights": "light.desk", "middle_button": "default"}
    defaults = {
        "middle_button": [
            {"action": "scene.turn_on", "target": {"entity_id": "scene.relax"}}
        ]
    }
    assert await registry_pico.setup([raw], defaults)
    snapshot = deepcopy(hass.data[DOMAIN]["yaml_config"])
    old = hass.data[DOMAIN]["controllers"][0]
    result = await begin(hass)
    assert result["step_id"] == "import_yaml"
    result = await advance(hass, result)
    assert old is hass.data[DOMAIN]["controllers"][0]
    result = await advance(hass, result, menu="save")
    result = await advance(hass, result)
    await hass.async_block_till_done()
    entry = result["result"]
    assert entry.state is ConfigEntryState.LOADED
    assert entry.data["devices"][0]["middle_button"] == "default"
    assert entry.data["devices"][0]["device_id"] == device.id
    assert hass.data[DOMAIN]["yaml_config"] == snapshot
    assert old._unsub_event is None
    registry_pico.tap("stop", device=device.id)
    await registry_pico.drain()
    assert len(registry_pico.calls) == 1
    assert registry_pico.calls[0][0] == "scene"


async def test_cancel_import_leaves_yaml_running(hass, registry_pico, register_pico):
    device = remote(register_pico)
    await registry_pico.setup(doc(device)["devices"])
    old = hass.data[DOMAIN]["controllers"][0]
    result = await begin(hass)
    result = await advance(hass, result)
    hass.config_entries.flow.async_abort(result["flow_id"])
    assert not hass.config_entries.async_entries(DOMAIN)
    assert hass.data[DOMAIN]["controllers"] == [old]


@pytest.mark.parametrize("bad", ["missing", "duplicate", "actions"])
async def test_import_fails_as_a_whole(hass, registry_pico, register_pico, bad):
    device = remote(register_pico)
    root = doc(device)
    if bad == "missing":
        root["devices"].append({"name": "Does not exist", "lights": "light.desk"})
    elif bad == "duplicate":
        root["devices"] *= 2
    else:
        root["defaults"]["stop_hold"] = [{"invalid": True}]
    await async_setup_component(hass, DOMAIN, {DOMAIN: root})
    result = await begin(hass)
    result = await advance(hass, result)
    assert result["step_id"] == "import_yaml"
    assert result["errors"]["base"] == "invalid_config"
    assert not hass.config_entries.async_entries(DOMAIN)


async def configured(hass, device, **extra):
    entry = MockConfigEntry(domain=DOMAIN, unique_id=DOMAIN, data=doc(device, **extra))
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()
    return entry


async def test_options_save_reload_and_cancel(hass, registry_pico, register_pico):
    device = remote(register_pico)
    entry = await configured(hass, device)
    old = hass.data[DOMAIN]["controllers"][0]
    result = await hass.config_entries.options.async_init(entry.entry_id)
    result = await advance(hass, result, options=True, menu="edit")
    result = await advance(hass, result, {"remote": "0"}, options=True)
    result = await advance(hass, result, options=True, menu="button")
    result = await advance(
        hass, result, {"button": "on", "gesture": "tap"}, options=True
    )
    result = await advance(hass, result, {"behavior": "custom"}, options=True)
    actions = [
        {
            "if": [{"condition": "template", "value_template": "{{ true }}"}],
            "then": [
                {"action": "scene.turn_on", "target": {"entity_id": "scene.work"}}
            ],
        }
    ]
    result = await advance(hass, result, {"actions": actions}, options=True)
    result = await advance(hass, result, options=True, menu="done")
    assert old is hass.data[DOMAIN]["controllers"][0]
    assert not entry.options
    result = await advance(hass, result, options=True, menu="save")
    result = await advance(hass, result, options=True)
    await hass.async_block_till_done()
    assert old._unsub_event is None
    assert entry.options["devices"][0]["on_tap"] == actions
    registry_pico.tap("on", device=device.id)
    await registry_pico.drain()
    assert [call[0] for call in registry_pico.calls] == ["scene"]
    snapshot = deepcopy(dict(entry.options))
    result = await hass.config_entries.options.async_init(entry.entry_id)
    result = await advance(hass, result, options=True, menu="remove")
    result = await advance(hass, result, {"remote": "0"}, options=True)
    result = await advance(hass, result, options=True)
    hass.config_entries.options.async_abort(result["flow_id"])
    assert dict(entry.options) == snapshot


async def test_ui_entry_prevents_leftover_yaml_startup(
    hass, registry_pico, register_pico
):
    device = remote(register_pico)
    entry = MockConfigEntry(domain=DOMAIN, unique_id=DOMAIN, data=doc(device))
    entry.add_to_hass(hass)
    assert await async_setup_component(
        hass,
        DOMAIN,
        {
            DOMAIN: {
                "devices": [
                    {"device_id": "different", "type": "3BRL", "lights": "light.other"}
                ]
            }
        },
    )
    await hass.async_block_till_done()
    assert len(hass.data[DOMAIN]["controllers"]) == 1
    assert hass.data[DOMAIN]["controllers"][0].conf.device_id == device.id


async def test_unload_cancels_wait_and_releases_scripts(
    hass, registry_pico, register_pico
):
    device = remote(register_pico)
    entry = await configured(
        hass,
        device,
        on_tap=[
            {"delay": 60},
            {"action": "light.turn_on", "target": {"entity_id": "light.late"}},
        ],
    )
    registry_pico.tap("on", device=device.id)
    await asyncio.sleep(0.03)
    assert await hass.config_entries.async_unload(entry.entry_id)
    await registry_pico.drain()
    assert not registry_pico.calls
    assert not hass.data[DOMAIN].get("controllers")
    assert not hass.data.get(DATA_SCRIPTS)
    registry_pico.tap("on", device=device.id)
    await registry_pico.drain()
    assert not registry_pico.calls


async def test_failed_setup_cleans_up_partial_controllers(
    hass, registry_pico, register_pico
):
    first = remote(register_pico)
    second = remote(register_pico, serial="second")
    root = doc(first)
    root["devices"] += doc(second)["devices"]
    entry = MockConfigEntry(domain=DOMAIN, unique_id=DOMAIN, data=root)
    entry.add_to_hass(hass)
    from custom_components.pico_link.controller import PicoController

    real_start = PicoController.async_start

    async def fail_second(ctrl):
        if ctrl.conf.device_id == second.id:
            raise ValueError("test setup failure")
        await real_start(ctrl)

    with patch.object(PicoController, "async_start", fail_second):
        assert not await hass.config_entries.async_setup(entry.entry_id)
    assert entry.state is ConfigEntryState.SETUP_RETRY
    registry_pico.tap("on", device=first.id)
    await registry_pico.drain()
    assert not registry_pico.calls


async def test_non_json_import_rejected(hass, register_pico):
    root = doc(remote(register_pico))
    root["devices"][0]["on_tap"] = [{"variables": {"value": object()}}]
    with pytest.raises(TypeError):
        await import_document(hass, root)


async def test_explicit_yaml_wins_over_saved_ui(hass, registry_pico, register_pico):
    device = remote(register_pico)
    entry = MockConfigEntry(domain=DOMAIN, unique_id=DOMAIN, data=doc(device))
    entry.add_to_hass(hass)
    yaml = doc(device)
    yaml["config_method"] = "yaml"
    yaml["devices"][0]["lights"] = ["light.yaml"]
    assert await async_setup_component(hass, DOMAIN, {DOMAIN: yaml})
    await hass.async_block_till_done()
    registry_pico.tap("on", device=device.id)
    await registry_pico.drain()
    assert len(registry_pico.calls) == 1
    assert registry_pico.calls[0][2]["entity_id"] == ["light.yaml"]
    result = await hass.config_entries.options.async_init(entry.entry_id)
    assert result["reason"] == "yaml_selected"
    assert await hass.config_entries.async_unload(entry.entry_id)
    assert hass.data[DOMAIN]["controllers"]


async def test_explicit_ui_waits_for_saved_configuration(
    hass, registry_pico, register_pico
):
    root = doc(remote(register_pico))
    root["config_method"] = "ui"
    assert await async_setup_component(hass, DOMAIN, {DOMAIN: root})
    assert not hass.data[DOMAIN].get("controllers")
    assert (await begin(hass))["step_id"] == "import_yaml"


async def test_method_choice_defaults_ui_and_yaml_creates_no_entry(hass, registry_pico):
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": "user"}
    )
    assert result["step_id"] == "method"
    assert result["data_schema"]({}) == {"config_method": "ui"}
    result = await advance(hass, result, {"config_method": "yaml"})
    assert result["reason"] == "yaml_selected"
    assert not hass.config_entries.async_entries(DOMAIN)


async def test_invalid_method_is_not_silently_ignored(hass, registry_pico):
    assert not await async_setup_component(
        hass, DOMAIN, {DOMAIN: {"config_method": "typo", "devices": []}}
    )


async def test_action_validation_preserves_raw_templates(hass, register_pico):
    root = doc(
        remote(register_pico),
        stop_tap=[
            {
                "action": "light.turn_on",
                "target": {"entity_id": "lights"},
                "data": {"brightness_pct": "{{ 50 }}"},
            }
        ],
    )
    snapshot = deepcopy(root)
    await validate_document(hass, root)
    assert root == snapshot


@pytest.mark.parametrize("gesture", ["tap", "hold", "double_tap"])
async def test_shared_stop_is_opt_in_and_raw_shortcuts_survive(
    hass, registry_pico, register_pico, gesture
):
    device = remote(register_pico)
    entry = await configured(hass, device)
    result = await hass.config_entries.options.async_init(entry.entry_id)
    result = await advance(hass, result, options=True, menu="defaults")
    result = await advance(hass, result, options=True, menu="shared_stop")
    result = await advance(hass, result, {"gesture": gesture}, options=True)
    actions = [
        {
            "action": "light.turn_on",
            "target": {"entity_id": "lights"},
            "data": {"brightness_pct": 50},
        }
    ]
    result = await advance(hass, result, {"actions": actions}, options=True)
    result = await advance(hass, result, options=True, menu="editor")
    result = await advance(hass, result, options=True, menu="edit")
    result = await advance(hass, result, {"remote": "0"}, options=True)
    result = await advance(hass, result, options=True, menu="button")
    result = await advance(
        hass, result, {"button": "stop", "gesture": gesture}, options=True
    )
    result = await advance(hass, result, {"behavior": "shared"}, options=True)
    result = await advance(hass, result, options=True, menu="done")
    result = await advance(hass, result, options=True, menu="save")
    await advance(hass, result, options=True)
    await hass.async_block_till_done()
    key = "stop_" + gesture
    assert entry.options["defaults"][key] == actions
    assert entry.options["devices"][0][key] == "default"
    conf = hass.data[DOMAIN]["controllers"][0].conf
    assert conf.overrides[key][0]["target"]["entity_id"] == ["light.desk"]


@pytest.mark.parametrize(
    "kind,button", [("Pico4ButtonScene", "button_1"), ("Pico3ButtonRaiseLower", "stop")]
)
async def test_legacy_gesture_can_be_disabled_then_restored(
    hass, registry_pico, register_pico, kind, button
):
    device = remote(register_pico, kind)
    action = [{"action": "scene.turn_on", "target": {"entity_id": "scene.old"}}]
    root = (
        doc(device, middle_button=action)
        if button == "stop"
        else {
            "defaults": {},
            "devices": [
                {"device_id": device.id, "buttons": {"button_1": action, "off": action}}
            ],
        }
    )
    entry = MockConfigEntry(domain=DOMAIN, unique_id=DOMAIN, data=root)
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    for behavior in ("disabled", "normal"):
        result = await hass.config_entries.options.async_init(entry.entry_id)
        result = await advance(hass, result, options=True, menu="edit")
        result = await advance(hass, result, {"remote": "0"}, options=True)
        result = await advance(hass, result, options=True, menu="button")
        result = await advance(
            hass, result, {"button": button, "gesture": "tap"}, options=True
        )
        result = await advance(hass, result, {"behavior": behavior}, options=True)
        result = await advance(hass, result, options=True, menu="done")
        result = await advance(hass, result, options=True, menu="save")
        await advance(hass, result, options=True)
        await hass.async_block_till_done()
        raw = entry.options["devices"][0]
        assert "middle_button" not in raw
        assert button not in raw.get("buttons", {})
        if behavior == "disabled":
            assert raw[button + "_tap"] == []
        else:
            assert button + "_tap" not in raw


async def test_add_scene_pico_requires_actions_and_rejects_duplicate(
    hass, registry_pico, register_pico
):
    device = remote(register_pico, "Pico4ButtonScene")
    result = await begin(hass)
    result = await advance(hass, result, menu="add")
    result = await advance(hass, result, {"device_id": device.id, "type": "automatic"})
    assert result["step_id"] == "remote"
    result = await advance(hass, result, menu="done")
    assert result["errors"]["base"] == "invalid_config"
    result = await advance(hass, result)
    result = await advance(hass, result, menu="button")
    result = await advance(
        hass, result, {"button": "button_1", "gesture": "double_tap"}
    )
    result = await advance(hass, result, {"behavior": "custom"})
    result = await advance(hass, result, {"actions": [{"bad_action": True}]})
    assert result["errors"]["base"] == "invalid_config"
    result = await advance(
        hass,
        result,
        {
            "actions": [
                {"action": "scene.turn_on", "target": {"entity_id": "scene.test"}}
            ]
        },
    )
    result = await advance(hass, result, menu="done")
    result = await advance(hass, result, menu="add")
    result = await advance(hass, result, {"device_id": device.id, "type": "automatic"})
    assert result["errors"]["base"] == "invalid_config"


@pytest.mark.parametrize("mode", ["single", "restart", "queued", "parallel"])
async def test_ui_run_policy_default_and_override(
    hass, registry_pico, register_pico, mode
):
    device = remote(register_pico)
    entry = await configured(hass, device)
    result = await hass.config_entries.options.async_init(entry.entry_id)
    result = await advance(hass, result, options=True, menu="defaults")
    result = await advance(hass, result, options=True, menu="run")
    result = await advance(
        hass, result, {"mode": mode, "max": 4, "max_exceeded": "silent"}, options=True
    )
    result = await advance(hass, result, options=True, menu="editor")
    result = await advance(hass, result, options=True, menu="edit")
    result = await advance(hass, result, {"remote": "0"}, options=True)
    result = await advance(hass, result, options=True, menu="run")
    result = await advance(
        hass,
        result,
        {"mode": "inherit", "max": 2, "max_exceeded": "inherit"},
        options=True,
    )
    result = await advance(hass, result, options=True, menu="done")
    result = await advance(hass, result, options=True, menu="save")
    await advance(hass, result, options=True)
    await hass.async_block_till_done()
    conf = hass.data[DOMAIN]["controllers"][0].conf
    assert (conf.mode, conf.max, conf.max_exceeded) == (mode, 2, "silent")
    assert "mode" not in entry.options["devices"][0]


async def test_missing_model_can_be_explicitly_selected(
    hass, registry_pico, register_pico
):
    device = remote(register_pico, "unfamiliar")
    result = await begin(hass)
    result = await advance(hass, result, menu="add")
    result = await advance(hass, result, {"device_id": device.id, "type": "automatic"})
    assert result["errors"]["base"] == "invalid_config"
    result = await advance(hass, result, {"device_id": device.id, "type": "2B"})
    assert result["step_id"] == "assignment"


async def test_layout_change_preserves_actions_until_user_removes_them(
    hass, registry_pico, register_pico
):
    device = remote(register_pico)
    root = doc(device, stop_tap=[{"delay": 1}])
    entry = MockConfigEntry(domain=DOMAIN, unique_id=DOMAIN, data=root)
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    result = await hass.config_entries.options.async_init(entry.entry_id)
    result = await advance(hass, result, options=True, menu="edit")
    result = await advance(hass, result, {"remote": "0"}, options=True)
    result = await advance(hass, result, options=True, menu="identity")
    result = await advance(
        hass, result, {"device_id": device.id, "type": "2B"}, options=True
    )
    assert result["errors"]["base"] == "invalid_config"
    assert "stop_tap" in result["description_placeholders"]["detail"]
    result = await advance(
        hass, result, {"device_id": device.id, "type": "automatic"}, options=True
    )
    result = await advance(hass, result, options=True, menu="done")
    result = await advance(hass, result, options=True, menu="save")
    assert not result["errors"]
    assert result["description_placeholders"]["detail"] == ""
    await advance(hass, result, options=True)
    await hass.async_block_till_done()
    assert entry.options["devices"][0]["stop_tap"] == [{"delay": 1}]


@pytest.mark.parametrize(
    "domain,field,key,value",
    [
        ("light", "lights", "light_low_pct", 25),
        ("cover", "covers", "cover_open_pos", 75),
        ("fan", "fans", "fan_on_pct", 50),
        ("media_player", "media_players", "media_player_vol_step", 5),
    ],
)
async def test_domain_settings_and_timing_round_trip(
    hass, registry_pico, register_pico, domain, field, key, value
):
    device = remote(register_pico)
    entry = await configured(hass, device)
    result = await hass.config_entries.options.async_init(entry.entry_id)
    result = await advance(hass, result, options=True, menu="edit")
    result = await advance(hass, result, {"remote": "0"}, options=True)
    result = await advance(hass, result, options=True, menu="assignment")
    result = await advance(hass, result, {"domain": domain}, options=True)
    result = await advance(hass, result, {"entities": [domain + ".test"]}, options=True)
    result = await advance(hass, result, options=True, menu="device_settings")
    result = await advance(
        hass,
        result,
        {key: value, **({"cover_inverted": "yes"} if domain == "cover" else {})},
        options=True,
    )
    result = await advance(hass, result, options=True, menu="timing")
    result = await advance(hass, result, {"double_tap_time_ms": 450}, options=True)
    result = await advance(hass, result, options=True, menu="done")
    result = await advance(hass, result, options=True, menu="save")
    await advance(hass, result, options=True)
    await hass.async_block_till_done()
    conf = hass.data[DOMAIN]["controllers"][0].conf
    assert getattr(conf, key) == value
    assert getattr(conf, field) == [domain + ".test"]
    assert (conf.hold_time_ms, conf.double_tap_time_ms, conf.step_time_ms) == (
        400,
        450,
        650,
    )
    if domain == "cover":
        assert conf.cover_inverted
