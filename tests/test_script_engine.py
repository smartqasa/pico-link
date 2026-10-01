"""Real HA script execution, per-Pico policies, compatibility and cleanup."""

import asyncio
import logging
from copy import deepcopy
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

import pytest
import voluptuous as vol
from homeassistant.components.media_player import (
    MediaPlayerEntity,
    MediaPlayerEntityFeature,
)
from homeassistant.core import callback
from homeassistant.exceptions import HomeAssistantError, ServiceNotSupported
from homeassistant.helpers import area_registry as ar
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.entity_component import EntityComponent
from homeassistant.helpers.script import DATA_SCRIPTS
from homeassistant.setup import async_setup_component

from custom_components.pico_link.config import parse_pico_config
from custom_components.pico_link.script_runner import PreparedSequence


def action(label, **extra):
    return {
        "alias": label,
        "action": "scene.turn_on",
        "data": {"label": label},
        **extra,
    }


def scene_device(**extra):
    return {
        "device_id": "pico",
        "type": "4B",
        "button_1_tap": [action("one")],
        "button_2_tap": [action("two")],
        "button_3_tap": [action("three")],
        **extra,
    }


async def settle():
    # Permit event dispatch/admission without waiting for deliberately blocked runs.
    await asyncio.sleep(0.02)


def runner(pico):
    return pico.hass.data["pico_link"]["controllers"][0].script_runner


def registered_scripts(hass):
    """Compare object identities across HA's old list and newer dict registry."""
    registry = hass.data[DATA_SCRIPTS]
    return (
        {id(item["instance"]) for item in registry}
        if isinstance(registry, list)
        else set(registry)
    )


@pytest.mark.parametrize("mode", ["single", "parallel", "queued", "restart"])
async def test_policy_inheritance_and_device_precedence(hass, mode):
    raw = scene_device()
    conf = parse_pico_config(hass, {}, raw)
    assert (conf.mode, conf.max, conf.max_exceeded) == ("single", 10, "warning")
    defaults = {"mode": mode, "max": 3, "max_exceeded": "silent"}
    conf = parse_pico_config(hass, defaults, raw)
    assert (conf.mode, conf.max, conf.max_exceeded) == (mode, 3, "silent")
    conf = parse_pico_config(
        hass, defaults, {**raw, "mode": "single", "max": 1, "max_exceeded": "debug"}
    )
    assert (conf.mode, conf.max, conf.max_exceeded) == ("single", 1, "debug")


@pytest.mark.parametrize(
    "key,value",
    [
        ("mode", "bad"),
        ("mode", None),
        ("mode", []),
        ("max", 0),
        ("max", -1),
        ("max", True),
        ("max", 1.5),
        ("max", "2"),
        ("max_exceeded", "quiet"),
        ("max_exceeded", False),
        ("continue_on_error", True),
    ],
)
async def test_invalid_execution_settings_are_rejected(hass, key, value):
    with pytest.raises(ValueError, match=key):
        parse_pico_config(hass, {key: value}, scene_device())


@pytest.mark.parametrize(
    "steps",
    [
        [{"delay": "bad"}],
        [{"choose": [{"sequence": [{"delay": -1}]}]}],
        [{"repeat": {"count": 2, "sequence": [None]}}],
        [{"action": "scene.turn_on", "continue_on_error": "maybe"}],
        [{"unknown": "step"}],
    ],
)
async def test_invalid_script_syntax_is_rejected(hass, steps):
    with pytest.raises(ValueError):
        parse_pico_config(hass, {}, scene_device(button_1_tap=steps))


@pytest.mark.parametrize("mode", ["single", "queued", "parallel"])
@pytest.mark.parametrize("severity", ["warning", "silent"])
async def test_modes_share_limits_across_buttons(pico, caplog, mode, severity):
    gate = asyncio.Event()

    async def block(call):
        await gate.wait()

    pico.register("scene", "turn_on", block)
    assert await pico.setup(
        [scene_device()], {"mode": mode, "max": 2, "max_exceeded": severity}
    )
    pico.tap("button_1", kind="4B")
    await pico.next_call()
    pico.tap("button_2", kind="4B")
    await settle()
    pico.tap("button_3", kind="4B")
    await settle()
    assert len(runner(pico)._runs) == (1 if mode == "single" else 2)
    assert len(pico.calls) == (2 if mode == "parallel" else 1)
    assert ("new custom sequence ignored" in caplog.text) == (severity == "warning")
    gate.set()
    await pico.drain()
    labels = [data["label"] for _, _, data in pico.calls]
    assert labels == (["one"] if mode == "single" else ["one", "two"])
    pico.tap("button_3", kind="4B")
    await pico.drain()
    assert pico.calls[-1][2]["label"] == "three"
    assert not runner(pico)._runs


async def test_restart_cancels_previous_button_and_only_runs_latest(pico):
    cancelled = asyncio.Event()

    async def block_first(call):
        if call.data["label"] == "one":
            try:
                await asyncio.Event().wait()
            finally:
                cancelled.set()

    pico.register("scene", "turn_on", block_first)
    assert await pico.setup(
        [scene_device(button_1_tap=[action("one"), action("stale")])],
        {"mode": "restart"},
    )
    pico.tap("button_1", kind="4B")
    await pico.next_call()
    pico.tap("button_2", kind="4B")
    await pico.drain()
    assert cancelled.is_set()
    assert [data["label"] for _, _, data in pico.calls] == ["one", "two"]
    assert not runner(pico)._runs


async def test_restart_burst_does_not_interrupt_cancellation_cleanup(pico):
    assert await pico.setup(
        [scene_device(button_1_tap=[{"delay": 5}, action("stale")])],
        {"mode": "restart"},
    )
    for _ in range(30):
        pico.tap("button_1", kind="4B")
    pico.tap("button_2", kind="4B")
    await pico.drain()
    assert [data["label"] for _, _, data in pico.calls] == ["two"]
    assert not runner(pico)._runs
    assert all(
        not script.is_running
        for prepared in runner(pico).sequences.values()
        for script in prepared.scripts
    )


async def test_restart_native_off_cancels_delayed_custom_on(pico):
    assert await pico.setup(
        [
            {
                "device_id": "pico",
                "type": "3BRL",
                "lights": "light.test",
                "mode": "restart",
                "on_tap": [action("started"), {"delay": 1}, action("stale")],
            }
        ]
    )
    pico.tap("on")
    await pico.next_call()
    pico.tap("off")
    await pico.drain()
    assert [service for _, service, _ in pico.calls] == ["turn_on", "turn_off"]
    assert pico.calls[-1][0] == "light"
    assert not runner(pico)._runs


async def test_native_controls_are_not_ignored_by_single_mode(pico):
    assert await pico.setup(
        [
            {
                "device_id": "pico",
                "type": "3BRL",
                "lights": "light.test",
                "stop_tap": [action("started"), {"delay": 0.05}, action("finished")],
            }
        ]
    )
    pico.tap("stop")
    await pico.next_call()
    pico.tap("off")
    await pico.drain()
    assert pico.calls[1][0:2] == ("light", "turn_off")
    assert pico.calls[2][2]["label"] == "finished"


async def test_different_picos_have_independent_admission(pico):
    gate = asyncio.Event()

    async def block(call):
        if call.data["label"] == "blocked":
            await gate.wait()

    pico.register("scene", "turn_on", block)
    assert await pico.setup(
        [
            scene_device(button_1_tap=[action("blocked")]),
            scene_device(device_id="other"),
        ]
    )
    pico.tap("button_1", kind="4B")
    await pico.next_call()
    pico.tap("button_2", kind="4B", device="other")
    assert (await pico.next_call())[2]["label"] == "two"
    gate.set()
    await pico.drain()


async def test_variables_choose_repeat_delay_and_nested_placeholders(pico):
    steps = [
        {"variables": {"count": 2}},
        {
            "choose": [
                {
                    "conditions": "{{ count == 2 }}",
                    "sequence": [
                        {
                            "repeat": {
                                "count": "{{ count }}",
                                "sequence": [
                                    {"delay": {"milliseconds": 1}},
                                    {
                                        "action": "light.turn_on",
                                        "target": {"entity_id": "lights"},
                                        "data": {
                                            "brightness_pct": "{{ repeat.index * 10 }}"
                                        },
                                    },
                                ],
                            }
                        },
                    ],
                }
            ],
            "default": [action("wrong")],
        },
    ]
    original = deepcopy(steps)
    assert await pico.setup(
        [
            {
                "device_id": "pico",
                "type": "3BRL",
                "lights": ["light.desk", "light.wall"],
                "stop_tap": steps,
            }
        ]
    )
    pico.tap("stop")
    await pico.drain()
    assert [data["brightness_pct"] for _, _, data in pico.calls] == [10, 20]
    assert all(
        data["entity_id"] == ["light.desk", "light.wall"] for _, _, data in pico.calls
    )
    assert steps == original


async def test_if_parallel_and_stop_use_native_script_semantics(pico):
    steps = [
        {
            "if": "{{ true }}",
            "then": [{"parallel": [action("a"), action("b")]}],
            "else": [action("wrong")],
        },
        {"stop": "Finished"},
        action("stale"),
    ]
    assert await pico.setup([scene_device(button_1_tap=steps)])
    pico.tap("button_1", kind="4B")
    await pico.drain()
    assert sorted(data["label"] for _, _, data in pico.calls) == ["a", "b"]


@pytest.mark.parametrize("continue_on_error", [False, True])
async def test_structured_sequence_honors_per_action_error_choice(
    pico, continue_on_error
):
    async def fail(call):
        if call.data["label"] == "failure":
            raise HomeAssistantError("Unavailable")

    pico.register("scene", "turn_on", fail)
    assert await pico.setup(
        [
            scene_device(
                button_1_tap=[
                    action("failure", continue_on_error=continue_on_error),
                    action("later"),
                ]
            )
        ]
    )
    pico.tap("button_1", kind="4B")
    await pico.drain()
    assert len(pico.calls) == (2 if continue_on_error else 1)
    pico.tap("button_2", kind="4B")
    await pico.drain()
    assert pico.calls[-1][2]["label"] == "two"


@pytest.mark.parametrize("failure", ["missing", "unexpected"])
async def test_legacy_list_continues_even_for_errors_native_continue_does_not_cover(
    pico, failure
):
    async def fail(call):
        raise RuntimeError("Unexpected provider failure")

    pico.register("scene", "turn_on", fail)
    first = "scene.missing" if failure == "missing" else "scene.turn_on"
    assert await pico.setup(
        [
            scene_device(
                button_1_tap=[
                    {"action": first},
                    {"action": "script.turn_on"},
                ]
            )
        ]
    )
    pico.tap("button_1", kind="4B")
    await pico.drain()
    assert pico.calls[-1][:2] == ("script", "turn_on")


@pytest.mark.parametrize("continue_on_timeout", [False, True])
async def test_wait_timeout_and_false_condition(pico, continue_on_timeout):
    assert await pico.setup(
        [
            scene_device(
                button_1_tap=[
                    {
                        "wait_template": "{{ false }}",
                        "timeout": 0.01,
                        "continue_on_timeout": continue_on_timeout,
                    },
                    action("after_wait"),
                    {"condition": "template", "value_template": "{{ false }}"},
                    action("stale"),
                ]
            )
        ]
    )
    pico.tap("button_1", kind="4B")
    await pico.drain()
    assert len(pico.calls) == int(continue_on_timeout)


@pytest.mark.parametrize("mode", ["queued", "parallel", "restart", "single"])
async def test_shutdown_cancels_waits_queues_and_removes_registered_scripts(pico, mode):
    assert await pico.setup(
        [
            scene_device(
                button_1_tap=[
                    action("start"),
                    {"wait_template": "{{ false }}"},
                    action("stale"),
                ]
            )
        ],
        {"mode": mode},
    )
    engine = runner(pico)
    scripts = [
        script for prepared in engine.sequences.values() for script in prepared.scripts
    ]
    registered = registered_scripts(pico.hass)
    pico.tap("button_1", kind="4B")
    await pico.next_call()
    pico.tap("button_1", kind="4B")
    await settle()
    assert registered_scripts(pico.hass) == registered
    await pico.stop()
    assert not engine.sequences and not engine._runs
    assert not any(script.is_running for script in scripts)
    assert all(id(script) not in registered_scripts(pico.hass) for script in scripts)
    assert all(data["label"] == "start" for _, _, data in pico.calls)


async def test_completed_runs_reuse_script_objects(pico):
    assert await pico.setup([scene_device()])
    initial = registered_scripts(pico.hass)
    for _ in range(15):
        pico.tap("button_1", kind="4B")
        await pico.drain()
    assert len(pico.calls) == 15
    assert registered_scripts(pico.hass) == initial
    assert not runner(pico)._runs


async def test_nested_shorthand_and_service_template(pico):
    assert await pico.setup(
        [
            {
                "device_id": "pico",
                "type": "3BRL",
                "lights": "light.test",
                "stop_tap": [
                    {"variables": {"selected_service": "light.turn_on"}},
                    {
                        "if": "{{ true }}",
                        "then": {
                            "action": "{{ selected_service }}",
                            "target": {"entity_id": "lights"},
                            "data": {"brightness_pct": 42},
                        },
                    },
                ],
            }
        ]
    )
    pico.tap("stop")
    await pico.drain()
    assert pico.calls == [
        ("light", "turn_on", {"entity_id": ["light.test"], "brightness_pct": 42})
    ]


async def test_parallel_templates_do_not_share_variables_between_runs(pico):
    assert await pico.setup(
        [
            scene_device(
                mode="parallel",
                button_1_tap=[
                    {"variables": {"captured": "{{ states('sensor.example') }}"}},
                    {"delay": 0.04},
                    {"action": "scene.turn_on", "data": {"label": "{{ captured }}"}},
                ],
            )
        ]
    )
    pico.hass.states.async_set("sensor.example", "first")
    pico.tap("button_1", kind="4B")
    await settle()
    pico.hass.states.async_set("sensor.example", "second")
    pico.tap("button_1", kind="4B")
    await pico.drain()
    assert [data["label"] for _, _, data in pico.calls] == ["first", "second"]


async def test_wait_for_event_resumes_after_trigger(pico):
    assert await pico.setup(
        [
            scene_device(
                button_1_tap=[
                    action("started"),
                    {
                        "wait_for_trigger": [
                            {"platform": "event", "event_type": "pico_test_resume"}
                        ],
                        "timeout": 5,
                    },
                    action("finished"),
                ]
            )
        ]
    )
    pico.tap("button_1", kind="4B")
    await pico.next_call()
    await settle()
    pico.hass.bus.async_fire("pico_test_resume")
    await pico.drain()
    assert [data["label"] for _, _, data in pico.calls] == ["started", "finished"]


async def test_partial_script_setup_failure_releases_objects_and_allows_other_devices(
    pico, caplog
):
    from custom_components.pico_link import script_runner

    validate = script_runner.async_validate_actions_config

    async def fail_second(hass, sequence):
        if sequence[0].get("alias") == "two":
            raise vol.Invalid("Simulated integration-specific validation failure")
        return await validate(hass, sequence)

    with patch.object(script_runner, "async_validate_actions_config", fail_second):
        assert await pico.setup(
            [
                scene_device(),
                {"device_id": "valid", "type": "2B", "lights": "light.test"},
            ]
        )
    assert len(pico.hass.data["pico_link"]["controllers"]) == 1
    assert not pico.hass.data[DATA_SCRIPTS]
    assert "Simulated integration-specific validation failure" in caplog.text
    pico.tap("on", kind="2B", device="valid")
    await pico.drain()
    assert pico.calls[-1][:2] == ("light", "turn_on")


@pytest.mark.parametrize("registry_type", [list, dict])
async def test_cleanup_adapter_for_ha_without_script_unload(pico, registry_type):
    assert await pico.setup([scene_device()])
    engine = runner(pico)
    await engine.async_close()
    script = SimpleNamespace(async_stop=AsyncMock())
    unrelated = SimpleNamespace()
    if registry_type is list:
        registry = [{"instance": script}, {"instance": unrelated}]
    else:
        registry = {
            id(script): {"instance": script},
            id(unrelated): {"instance": unrelated},
        }
    pico.hass.data[DATA_SCRIPTS] = registry
    engine.sequences[1] = PreparedSequence([script], False, [], "old HA")
    await engine.async_close()
    script.async_stop.assert_awaited_once()
    entries = registry if registry_type is list else registry.values()
    assert [entry["instance"] for entry in entries] == [unrelated]
    # Remove the stand-in before the real HA shutdown handler inspects scripts.
    pico.hass.data[DATA_SCRIPTS] = {}


@pytest.mark.parametrize("detached", [True, False])
async def test_external_script_lifecycle_under_parent_restart(pico, detached):
    started, finished = asyncio.Event(), asyncio.Event()
    pico.hass.bus.async_listen("pico_child_started", callback(lambda _: started.set()))
    pico.hass.bus.async_listen(
        "pico_child_finished", callback(lambda _: finished.set())
    )
    assert await async_setup_component(
        pico.hass,
        "script",
        {
            "script": {
                "pico_child": {
                    "sequence": [
                        {"event": "pico_child_started"},
                        {
                            "wait_for_trigger": [
                                {"platform": "event", "event_type": "pico_child_resume"}
                            ]
                        },
                        {"event": "pico_child_finished"},
                    ]
                },
            }
        },
    )
    launch = (
        {"action": "script.turn_on", "target": {"entity_id": "script.pico_child"}}
        if detached
        else {"action": "script.pico_child"}
    )
    assert await pico.setup(
        [
            {
                "device_id": "pico",
                "type": "3BRL",
                "lights": "light.test",
                "mode": "restart",
                "stop_tap": [launch, {"delay": 5}, action("stale")],
            }
        ]
    )
    pico.tap("stop")
    await asyncio.wait_for(started.wait(), 3)
    await settle()
    pico.tap("off")
    assert (await pico.next_call())[:2] == ("light", "turn_off")
    pico.hass.bus.async_fire("pico_child_resume")
    await pico.drain()
    assert finished.is_set() is detached
    assert pico.calls == [("light", "turn_off", {"entity_id": ["light.test"]})]


async def test_area_turn_off_keeps_unsupported_entity_error_and_legacy_continuation(
    pico, caplog
):
    """Broad area commands fail the same way with the old API and the script engine."""
    hass = pico.hass
    assert await async_setup_component(hass, "homeassistant", {})

    class VoicePlayer(MediaPlayerEntity):
        _attr_name = "Voice test"
        _attr_unique_id = "voice-test"
        _attr_should_poll = False
        _attr_supported_features = MediaPlayerEntityFeature.PLAY_MEDIA

    class Television(MediaPlayerEntity):
        _attr_name = "TV test"
        _attr_unique_id = "tv-test"
        _attr_should_poll = False
        _attr_supported_features = MediaPlayerEntityFeature.TURN_OFF
        async_turn_off = AsyncMock()

    component = EntityComponent(logging.getLogger(__name__), "media_player", hass)
    player = VoicePlayer()
    television = Television()
    await component.async_add_entities([player, television])
    component.async_register_entity_service(
        "turn_off", None, "async_turn_off", [MediaPlayerEntityFeature.TURN_OFF]
    )
    office = ar.async_get(hass).async_create("Office")
    entity_registry = er.async_get(hass)
    for entity in (player, television):
        entity_registry.async_update_entity(entity.entity_id, area_id=office.id)
    lamp = entity_registry.async_get_or_create(
        "light", "test", "office-lamp", suggested_object_id="office_lamp"
    )
    entity_registry.async_update_entity(lamp.entity_id, area_id=office.id)
    hass.states.async_set(lamp.entity_id, "on")
    # This is the exact service API used by Pico Link before the script engine.
    with pytest.raises(ServiceNotSupported):
        await hass.services.async_call(
            "homeassistant",
            "turn_off",
            {},
            target={"area_id": office.id},
            blocking=True,
        )
    await pico.drain()
    assert pico.calls == [
        ("light", "turn_off", {"area_id": office.id, "entity_id": [lamp.entity_id]})
    ]
    television.async_turn_off.assert_not_called()
    pico.calls.clear()
    assert await pico.setup(
        [
            scene_device(
                button_1_tap=[
                    {
                        "action": "homeassistant.turn_off",
                        "target": {"area_id": office.id},
                    },
                    {
                        "action": "scene.turn_on",
                        "target": {"entity_id": "scene.after_error"},
                    },
                ]
            )
        ]
    )
    pico.tap("button_1", kind="4B")
    await pico.drain()
    assert "error calling homeassistant.turn_off" in caplog.text
    assert "ServiceNotSupported" in caplog.text
    assert (
        "light",
        "turn_off",
        {"area_id": office.id, "entity_id": [lamp.entity_id]},
    ) in pico.calls
    assert ("scene", "turn_on", {"entity_id": "scene.after_error"}) in pico.calls
    television.async_turn_off.assert_not_called()
    # A domain-specific area target remains indirect: HA skips the unsupported
    # player and still turns off a capable player, without targeting it by ID.
    await hass.services.async_call(
        "media_player", "turn_off", {}, target={"area_id": office.id}, blocking=True
    )
    television.async_turn_off.assert_awaited_once()
    await component.async_remove_entity(player.entity_id)
    await component.async_remove_entity(television.entity_id)
