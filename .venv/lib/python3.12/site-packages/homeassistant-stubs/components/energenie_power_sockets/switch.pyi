from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyegps.powerstrip import PowerStrip as PowerStrip
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EGPowerStripSocket(SwitchEntity):
    _attr_device_class: Incomplete
    _attr_has_entity_name: bool
    _attr_translation_key: str
    _dev: Incomplete
    _socket: Incomplete
    _attr_translation_placeholders: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, dev: PowerStrip, socket: int) -> None: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    def update(self) -> None: ...
