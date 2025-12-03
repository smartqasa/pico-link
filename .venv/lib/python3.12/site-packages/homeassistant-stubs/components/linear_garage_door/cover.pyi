from .const import DOMAIN as DOMAIN
from .coordinator import LinearUpdateCoordinator as LinearUpdateCoordinator
from .entity import LinearEntity as LinearEntity
from _typeshed import Incomplete
from homeassistant.components.cover import CoverDeviceClass as CoverDeviceClass, CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

SUPPORTED_SUBDEVICES: Incomplete
PARALLEL_UPDATES: int
SCAN_INTERVAL: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LinearCoverEntity(LinearEntity, CoverEntity):
    _attr_supported_features: Incomplete
    _attr_name: Incomplete
    _attr_device_class: Incomplete
    @property
    def is_closed(self) -> bool: ...
    @property
    def is_opened(self) -> bool: ...
    @property
    def is_opening(self) -> bool: ...
    @property
    def is_closing(self) -> bool: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
