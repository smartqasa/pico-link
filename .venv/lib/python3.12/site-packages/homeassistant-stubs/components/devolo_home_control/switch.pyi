from . import DevoloHomeControlConfigEntry as DevoloHomeControlConfigEntry
from .entity import DevoloDeviceEntity as DevoloDeviceEntity
from _typeshed import Incomplete
from devolo_home_control_api.devices.zwave import Zwave as Zwave
from devolo_home_control_api.homecontrol import HomeControl as HomeControl
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: DevoloHomeControlConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DevoloSwitch(DevoloDeviceEntity, SwitchEntity):
    _attr_name: Incomplete
    _binary_switch_property: Incomplete
    _attr_is_on: Incomplete
    def __init__(self, homecontrol: HomeControl, device_instance: Zwave, element_uid: str) -> None: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
    def _sync(self, message: tuple) -> None: ...
