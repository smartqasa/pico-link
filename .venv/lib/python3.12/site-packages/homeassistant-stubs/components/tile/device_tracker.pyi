from . import TileData as TileData
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.device_tracker import AsyncSeeCallback as AsyncSeeCallback, TrackerEntity as TrackerEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from homeassistant.util.dt import as_utc as as_utc
from pytile.tile import Tile as Tile

_LOGGER: Incomplete
ATTR_ALTITUDE: str
ATTR_CONNECTION_STATE: str
ATTR_IS_DEAD: str
ATTR_IS_LOST: str
ATTR_LAST_LOST_TIMESTAMP: str
ATTR_LAST_TIMESTAMP: str
ATTR_RING_STATE: str
ATTR_TILE_NAME: str
ATTR_VOIP_STATE: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
async def async_setup_scanner(hass: HomeAssistant, config: ConfigType, async_see: AsyncSeeCallback, discovery_info: DiscoveryInfoType | None = None) -> bool: ...

class TileDeviceTracker(CoordinatorEntity[DataUpdateCoordinator[None]], TrackerEntity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_translation_key: str
    _attr_extra_state_attributes: Incomplete
    _attr_unique_id: Incomplete
    _entry: Incomplete
    _tile: Incomplete
    def __init__(self, entry: ConfigEntry, coordinator: DataUpdateCoordinator[None], tile: Tile) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    _attr_longitude: Incomplete
    _attr_latitude: Incomplete
    _attr_location_accuracy: Incomplete
    @callback
    def _update_from_latest_data(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
