from .const import SIGNAL_DEVICE_ADD as SIGNAL_DEVICE_ADD
from .coordinator import SwitcherDataUpdateCoordinator as SwitcherDataUpdateCoordinator
from .entity import SwitcherEntity as SwitcherEntity
from _typeshed import Incomplete
from homeassistant.components.cover import ATTR_POSITION as ATTR_POSITION, CoverDeviceClass as CoverDeviceClass, CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

API_SET_POSITON: str
API_STOP: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SwitcherBaseCoverEntity(SwitcherEntity, CoverEntity):
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    _cover_id: int
    @callback
    def _handle_coordinator_update(self) -> None: ...
    _attr_current_cover_position: Incomplete
    _attr_is_closed: Incomplete
    _attr_is_closing: Incomplete
    _attr_is_opening: Incomplete
    def _update_data(self) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_set_cover_position(self, **kwargs: Any) -> None: ...
    async def async_stop_cover(self, **kwargs: Any) -> None: ...

class SwitcherSingleCoverEntity(SwitcherBaseCoverEntity):
    _attr_name: Incomplete
    _cover_id: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SwitcherDataUpdateCoordinator, cover_id: int) -> None: ...

class SwitcherMultiCoverEntity(SwitcherBaseCoverEntity):
    _attr_translation_key: str
    _cover_id: Incomplete
    _attr_translation_placeholders: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SwitcherDataUpdateCoordinator, cover_id: int) -> None: ...
