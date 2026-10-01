"""Run Pico Link through HA setup, events and services, without real hardware."""

import asyncio

import pytest
from homeassistant.const import EVENT_HOMEASSISTANT_STOP
from homeassistant.helpers import device_registry as dr
from homeassistant.setup import async_setup_component
from pytest_homeassistant_custom_component.common import (
    MockConfigEntry,
    MockModule,
    mock_integration,
)

EVENT = "lutron_caseta_button_event"
HARDWARE_TYPES = {
    "P2B": "PaddleSwitchPico",
    "2B": "Pico2Button",
    "3BRL": "Pico3ButtonRaiseLower",
    "4B": "Pico4ButtonScene",
}
SERVICES = {
    "light": ("turn_on", "turn_off"),
    "cover": ("open_cover", "close_cover", "stop_cover", "set_cover_position"),
    "fan": ("set_percentage", "turn_off", "set_direction"),
    "media_player": (
        "media_play_pause",
        "media_next_track",
        "volume_set",
        "volume_mute",
    ),
    "switch": ("turn_on", "turn_off"),
    "scene": ("turn_on",),
    "script": ("turn_on",),
}


class PicoHarness:
    """Record outgoing service calls while running the actual integration."""

    def __init__(self, hass, register_detected=None):
        self.hass = hass
        self.register_detected = register_detected
        self.device_ids = {}
        self.calls = []
        self.received = asyncio.Queue()
        for domain, services in SERVICES.items():
            for service in services:
                self.register(domain, service)

    def register(self, domain, service, handler=None):
        async def record(call):
            item = (call.domain, call.service, dict(call.data))
            self.calls.append(item)
            self.received.put_nowait(item)
            if handler is not None:
                await handler(call)

        self.hass.services.async_register(domain, service, record)

    async def setup(self, devices, defaults=None):
        """Use short, real timers; tests do not replace gesture calculations."""
        if self.register_detected is not None:
            resolved = []
            for raw in devices:
                if isinstance(raw, dict) and raw.get("type") in HARDWARE_TYPES:
                    raw = dict(raw)
                    kind = raw.pop("type")
                    alias = raw["device_id"]
                    if alias not in self.device_ids:
                        device = self.register_detected(
                            model=f"Test model ({HARDWARE_TYPES[kind]})", serial=alias
                        )
                        self.device_ids[alias] = device.id
                    raw["device_id"] = self.device_ids[alias]
                resolved.append(raw)
            devices = resolved
        return await async_setup_component(
            self.hass,
            "pico_link",
            {
                "pico_link": {
                    "defaults": {
                        "hold_time_ms": 100,
                        "step_time_ms": 100,
                        **(defaults or {}),
                    },
                    "devices": devices,
                }
            },
        )

    def fire(self, button, action="press", *, device="pico", kind="3BRL", **data):
        self.hass.bus.async_fire(
            EVENT,
            {
                "device_id": self.device_ids.get(device, device),
                "type": HARDWARE_TYPES[kind],
                "button_type": button,
                "action": action,
                **data,
            },
        )

    def tap(self, button, **kwargs):
        self.fire(button, "press", **kwargs)
        self.fire(button, "release", **kwargs)

    async def next_call(self):
        return await asyncio.wait_for(self.received.get(), timeout=3)

    async def drain(self):
        await asyncio.wait_for(self.hass.async_block_till_done(), timeout=5)

    async def stop(self):
        self.hass.bus.async_fire(EVENT_HOMEASSISTANT_STOP)
        await self.drain()


@pytest.fixture(params=["explicit", "detected"])
def type_setting(request):
    """Exercise existing button behavior with both ways of selecting a profile."""
    return request.param


@pytest.fixture
def register_pico(hass):
    """Create real registry records using the Lutron model field format."""
    entries = {}

    def register(*, model, serial="pico", name="Test Pico", domain="lutron_caseta"):
        if domain not in entries:
            entry = MockConfigEntry(domain=domain)
            entry.add_to_hass(hass)
            entries[domain] = entry
        return dr.async_get(hass).async_get_or_create(
            config_entry_id=entries[domain].entry_id,
            identifiers={(domain, serial)},
            name=name,
            model=model,
        )

    return register


@pytest.fixture
async def pico(hass, enable_custom_integrations, type_setting, register_pico):
    """Fake only the Lutron bridge and device services, not Pico Link."""
    mock_integration(hass, MockModule("lutron_caseta"))
    await async_setup_component(hass, "light", {})
    harness = PicoHarness(hass, register_pico if type_setting == "detected" else None)
    yield harness
    await harness.stop()


@pytest.fixture
async def registry_pico(hass, enable_custom_integrations):
    """Use exact device configurations for detection and explicit-type tests."""
    mock_integration(hass, MockModule("lutron_caseta"))
    await async_setup_component(hass, "light", {})
    harness = PicoHarness(hass)
    yield harness
    await harness.stop()
