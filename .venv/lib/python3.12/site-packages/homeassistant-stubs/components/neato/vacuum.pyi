from .const import ACTION as ACTION, ALERTS as ALERTS, ERRORS as ERRORS, MODE as MODE, NEATO_LOGIN as NEATO_LOGIN, NEATO_MAP_DATA as NEATO_MAP_DATA, NEATO_PERSISTENT_MAPS as NEATO_PERSISTENT_MAPS, NEATO_ROBOTS as NEATO_ROBOTS, SCAN_INTERVAL_MINUTES as SCAN_INTERVAL_MINUTES
from .entity import NeatoEntity as NeatoEntity
from .hub import NeatoHub as NeatoHub
from _typeshed import Incomplete
from homeassistant.components.vacuum import ATTR_STATUS as ATTR_STATUS, StateVacuumEntity as StateVacuumEntity, VacuumActivity as VacuumActivity, VacuumEntityFeature as VacuumEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_MODE as ATTR_MODE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pybotvac import Robot as Robot
from typing import Any

_LOGGER: Incomplete
SCAN_INTERVAL: Incomplete
ATTR_CLEAN_START: str
ATTR_CLEAN_STOP: str
ATTR_CLEAN_AREA: str
ATTR_CLEAN_BATTERY_START: str
ATTR_CLEAN_BATTERY_END: str
ATTR_CLEAN_SUSP_COUNT: str
ATTR_CLEAN_SUSP_TIME: str
ATTR_CLEAN_PAUSE_TIME: str
ATTR_CLEAN_ERROR_TIME: str
ATTR_LAUNCHED_FROM: str
ATTR_NAVIGATION: str
ATTR_CATEGORY: str
ATTR_ZONE: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NeatoConnectedVacuum(NeatoEntity, StateVacuumEntity):
    _attr_supported_features: Incomplete
    _attr_name: Incomplete
    _attr_available: bool
    _mapdata: Incomplete
    _robot_has_map: bool
    _robot_maps: Incomplete
    _robot_serial: str
    _attr_unique_id: str
    _status_state: str | None
    _state: dict[str, Any] | None
    _clean_time_start: str | None
    _clean_time_stop: str | None
    _clean_area: float | None
    _clean_battery_start: int | None
    _clean_battery_end: int | None
    _clean_susp_charge_count: int | None
    _clean_susp_time: int | None
    _clean_pause_time: int | None
    _clean_error_time: int | None
    _launched_from: str | None
    _robot_boundaries: list
    _robot_stats: dict[str, Any] | None
    def __init__(self, neato: NeatoHub, robot: Robot, mapdata: dict[str, Any] | None, persistent_maps: dict[str, Any] | None) -> None: ...
    _attr_activity: Incomplete
    _attr_battery_level: Incomplete
    def update(self) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    def start(self) -> None: ...
    def pause(self) -> None: ...
    def return_to_base(self, **kwargs: Any) -> None: ...
    def stop(self, **kwargs: Any) -> None: ...
    def locate(self, **kwargs: Any) -> None: ...
    def clean_spot(self, **kwargs: Any) -> None: ...
    def neato_custom_cleaning(self, mode: str, navigation: str, category: str, zone: str | None = None) -> None: ...
