from . import DevoloHomeControlConfigEntry as DevoloHomeControlConfigEntry
from .devolo_multi_level_switch import DevoloMultiLevelSwitchDeviceEntity as DevoloMultiLevelSwitchDeviceEntity
from _typeshed import Incomplete
from devolo_home_control_api.devices.zwave import Zwave as Zwave
from devolo_home_control_api.homecontrol import HomeControl as HomeControl
from homeassistant.components.siren import ATTR_TONE as ATTR_TONE, SirenEntity as SirenEntity, SirenEntityFeature as SirenEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: DevoloHomeControlConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DevoloSirenDeviceEntity(DevoloMultiLevelSwitchDeviceEntity, SirenEntity):
    _attr_supported_features: Incomplete
    _attr_available_tones: Incomplete
    _default_tone: Incomplete
    def __init__(self, homecontrol: HomeControl, device_instance: Zwave, element_uid: str) -> None: ...
    @property
    def is_on(self) -> bool: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
    def _generic_message(self, message: tuple) -> None: ...
