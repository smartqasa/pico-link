from . import DevoloHomeControlConfigEntry as DevoloHomeControlConfigEntry
from .devolo_multi_level_switch import DevoloMultiLevelSwitchDeviceEntity as DevoloMultiLevelSwitchDeviceEntity
from _typeshed import Incomplete
from homeassistant.components.cover import CoverDeviceClass as CoverDeviceClass, CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: DevoloHomeControlConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DevoloCoverDeviceEntity(DevoloMultiLevelSwitchDeviceEntity, CoverEntity):
    _attr_supported_features: Incomplete
    _attr_device_class: Incomplete
    @property
    def current_cover_position(self) -> int: ...
    @property
    def is_closed(self) -> bool: ...
    def open_cover(self, **kwargs: Any) -> None: ...
    def close_cover(self, **kwargs: Any) -> None: ...
    def set_cover_position(self, **kwargs: Any) -> None: ...
