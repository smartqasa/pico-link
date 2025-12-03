from .const import LOGGER as LOGGER
from .entity import MatterEntity as MatterEntity
from .helpers import get_matter as get_matter
from .models import MatterDiscoverySchema as MatterDiscoverySchema
from _typeshed import Incomplete
from enum import IntEnum
from homeassistant.components.cover import ATTR_POSITION as ATTR_POSITION, ATTR_TILT_POSITION as ATTR_TILT_POSITION, CoverDeviceClass as CoverDeviceClass, CoverEntity as CoverEntity, CoverEntityDescription as CoverEntityDescription, CoverEntityFeature as CoverEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

OPERATIONAL_STATUS_MASK: int
TYPE_MAP: Incomplete

class OperationalStatus(IntEnum):
    COVERING_IS_CURRENTLY_NOT_MOVING = 0
    COVERING_IS_CURRENTLY_OPENING = 1
    COVERING_IS_CURRENTLY_CLOSING = 2
    RESERVED = 3

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MatterCover(MatterEntity, CoverEntity):
    entity_description: CoverEntityDescription
    @property
    def is_closed(self) -> bool | None: ...
    async def async_stop_cover(self, **kwargs: Any) -> None: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    async def async_set_cover_position(self, **kwargs: Any) -> None: ...
    async def async_set_cover_tilt_position(self, **kwargs: Any) -> None: ...
    async def send_device_command(self, command: Any) -> None: ...
    _attr_is_opening: bool
    _attr_is_closing: bool
    _attr_current_cover_position: Incomplete
    _attr_current_cover_tilt_position: Incomplete
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    @callback
    def _update_from_device(self) -> None: ...

DISCOVERY_SCHEMAS: Incomplete
