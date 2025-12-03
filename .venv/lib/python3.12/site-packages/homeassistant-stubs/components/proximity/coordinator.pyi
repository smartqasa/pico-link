from .const import ATTR_DIR_OF_TRAVEL as ATTR_DIR_OF_TRAVEL, ATTR_DIST_TO as ATTR_DIST_TO, ATTR_IN_IGNORED_ZONE as ATTR_IN_IGNORED_ZONE, ATTR_NEAREST as ATTR_NEAREST, CONF_IGNORED_ZONES as CONF_IGNORED_ZONES, CONF_TOLERANCE as CONF_TOLERANCE, CONF_TRACKED_ENTITIES as CONF_TRACKED_ENTITIES, DEFAULT_DIR_OF_TRAVEL as DEFAULT_DIR_OF_TRAVEL, DEFAULT_DIST_TO_ZONE as DEFAULT_DIST_TO_ZONE, DEFAULT_NEAREST as DEFAULT_NEAREST, DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, ATTR_NAME as ATTR_NAME, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, CONF_ZONE as CONF_ZONE
from homeassistant.core import Event as Event, EventStateChangedData as EventStateChangedData, HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from homeassistant.util.location import distance as distance

_LOGGER: Incomplete
type ProximityConfigEntry = ConfigEntry[ProximityDataUpdateCoordinator]

@dataclass
class StateChangedData:
    entity_id: str
    old_state: State | None
    new_state: State | None

@dataclass
class ProximityData:
    proximity: dict[str, str | int | None]
    entities: dict[str, dict[str, str | int | None]]

DEFAULT_PROXIMITY_DATA: dict[str, str | int | None]

class ProximityDataUpdateCoordinator(DataUpdateCoordinator[ProximityData]):
    config_entry: ProximityConfigEntry
    ignored_zone_ids: list[str]
    tracked_entities: list[str]
    tolerance: int
    proximity_zone_id: str
    proximity_zone_name: str
    unit_of_measurement: str
    entity_mapping: dict[str, list[str]]
    data: Incomplete
    state_change_data: StateChangedData | None
    def __init__(self, hass: HomeAssistant, friendly_name: str, config: ConfigType) -> None: ...
    @callback
    def async_add_entity_mapping(self, tracked_entity_id: str, entity_id: str) -> None: ...
    async def async_check_proximity_state_change(self, event: Event[EventStateChangedData]) -> None: ...
    async def async_check_tracked_entity_change(self, event: Event[er.EventEntityRegistryUpdatedData]) -> None: ...
    def _calc_distance_to_zone(self, zone: State, device: State, latitude: float | None, longitude: float | None) -> int | None: ...
    def _calc_direction_of_travel(self, zone: State, device: State, old_latitude: float | None, old_longitude: float | None, new_latitude: float | None, new_longitude: float | None) -> str | None: ...
    async def _async_update_data(self) -> ProximityData: ...
    def _create_removed_tracked_entity_issue(self, entity_id: str) -> None: ...
