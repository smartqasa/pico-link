from .const import CONF_CHARGING_INTERVAL as CONF_CHARGING_INTERVAL, CONF_CLIMATE_INTERVAL as CONF_CLIMATE_INTERVAL, CONF_FORCE_MILES as CONF_FORCE_MILES, CONF_INTERVAL as CONF_INTERVAL, CONF_VALID_REGIONS as CONF_VALID_REGIONS, DATA_BATTERY as DATA_BATTERY, DATA_CHARGING as DATA_CHARGING, DATA_CLIMATE as DATA_CLIMATE, DATA_LEAF as DATA_LEAF, DATA_PLUGGED_IN as DATA_PLUGGED_IN, DATA_RANGE_AC as DATA_RANGE_AC, DATA_RANGE_AC_OFF as DATA_RANGE_AC_OFF, DEFAULT_CHARGING_INTERVAL as DEFAULT_CHARGING_INTERVAL, DEFAULT_CLIMATE_INTERVAL as DEFAULT_CLIMATE_INTERVAL, DEFAULT_INTERVAL as DEFAULT_INTERVAL, DOMAIN as DOMAIN, INITIAL_UPDATE as INITIAL_UPDATE, MAX_RESPONSE_ATTEMPTS as MAX_RESPONSE_ATTEMPTS, MIN_UPDATE_INTERVAL as MIN_UPDATE_INTERVAL, PYCARWINGS2_SLEEP as PYCARWINGS2_SLEEP, RESTRICTED_BATTERY as RESTRICTED_BATTERY, RESTRICTED_INTERVAL as RESTRICTED_INTERVAL, SIGNAL_UPDATE_LEAF as SIGNAL_UPDATE_LEAF
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_REGION as CONF_REGION, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.helpers.discovery import load_platform as load_platform
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.event import async_track_point_in_utc_time as async_track_point_in_utc_time
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.dt import utcnow as utcnow
from pycarwings2 import Leaf as Leaf
from pycarwings2.responses import CarwingsLatestBatteryStatusResponse as CarwingsLatestBatteryStatusResponse, CarwingsLatestClimateControlStatusResponse as CarwingsLatestClimateControlStatusResponse
from typing import Any

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete
PLATFORMS: Incomplete
SERVICE_UPDATE_LEAF: str
SERVICE_START_CHARGE_LEAF: str
ATTR_VIN: str
UPDATE_LEAF_SCHEMA: Incomplete
START_CHARGE_LEAF_SCHEMA: Incomplete

def setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
def _extract_start_date(battery_info: CarwingsLatestBatteryStatusResponse) -> datetime | None: ...

class LeafDataStore:
    hass: Incomplete
    leaf: Incomplete
    car_config: Incomplete
    force_miles: Incomplete
    data: dict[str, Any]
    next_update: datetime | None
    last_check: datetime | None
    request_in_progress: bool
    last_battery_response: datetime | None
    last_climate_response: datetime | None
    _remove_listener: CALLBACK_TYPE | None
    def __init__(self, hass: HomeAssistant, leaf: Leaf, car_config: dict[str, Any]) -> None: ...
    async def async_update_data(self, now: datetime) -> None: ...
    def get_next_interval(self) -> datetime: ...
    async def async_refresh_data(self, now: datetime) -> None: ...
    async def async_get_battery(self) -> CarwingsLatestBatteryStatusResponse: ...
    async def async_get_climate(self) -> CarwingsLatestClimateControlStatusResponse: ...
    async def async_set_climate(self, toggle: bool) -> bool: ...
    async def async_start_charging(self) -> None: ...
    def schedule_update(self) -> None: ...
