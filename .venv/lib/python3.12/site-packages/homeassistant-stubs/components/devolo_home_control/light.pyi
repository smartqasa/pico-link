from . import DevoloHomeControlConfigEntry as DevoloHomeControlConfigEntry
from .devolo_multi_level_switch import DevoloMultiLevelSwitchDeviceEntity as DevoloMultiLevelSwitchDeviceEntity
from _typeshed import Incomplete
from devolo_home_control_api.devices.zwave import Zwave as Zwave
from devolo_home_control_api.homecontrol import HomeControl as HomeControl
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: DevoloHomeControlConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DevoloLightDeviceEntity(DevoloMultiLevelSwitchDeviceEntity, LightEntity):
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    _binary_switch_property: Incomplete
    def __init__(self, homecontrol: HomeControl, device_instance: Zwave, element_uid: str) -> None: ...
    @property
    def brightness(self) -> int: ...
    @property
    def is_on(self) -> bool: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
