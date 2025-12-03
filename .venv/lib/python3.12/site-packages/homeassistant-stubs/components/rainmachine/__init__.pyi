from .config_flow import get_client_controller as get_client_controller
from .const import CONF_ALLOW_INACTIVE_ZONES_TO_RUN as CONF_ALLOW_INACTIVE_ZONES_TO_RUN, CONF_DEFAULT_ZONE_RUN_TIME as CONF_DEFAULT_ZONE_RUN_TIME, CONF_DURATION as CONF_DURATION, CONF_USE_APP_RUN_TIMES as CONF_USE_APP_RUN_TIMES, DATA_API_VERSIONS as DATA_API_VERSIONS, DATA_MACHINE_FIRMWARE_UPDATE_STATUS as DATA_MACHINE_FIRMWARE_UPDATE_STATUS, DATA_PROGRAMS as DATA_PROGRAMS, DATA_PROVISION_SETTINGS as DATA_PROVISION_SETTINGS, DATA_RESTRICTIONS_CURRENT as DATA_RESTRICTIONS_CURRENT, DATA_RESTRICTIONS_UNIVERSAL as DATA_RESTRICTIONS_UNIVERSAL, DATA_ZONES as DATA_ZONES, DEFAULT_ZONE_RUN as DEFAULT_ZONE_RUN, DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import RainMachineDataUpdateCoordinator as RainMachineDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.update_coordinator import UpdateFailed as UpdateFailed
from homeassistant.util.dt import as_timestamp as as_timestamp, utcnow as utcnow
from homeassistant.util.network import is_ip_address as is_ip_address
from regenmaschine.controller import Controller as Controller

DEFAULT_SSL: bool
PLATFORMS: Incomplete
CONF_CONDITION: str
CONF_DEWPOINT: str
CONF_ET: str
CONF_MAXRH: str
CONF_MAXTEMP: str
CONF_MINRH: str
CONF_MINTEMP: str
CONF_PRESSURE: str
CONF_QPF: str
CONF_RAIN: str
CONF_SECONDS: str
CONF_SOLARRAD: str
CONF_TEMPERATURE: str
CONF_TIMESTAMP: str
CONF_UNITS: str
CONF_VALUE: str
CONF_WEATHER: str
CONF_WIND: str
CV_FLOW_METER_VALID_UNITS: Incomplete
CV_WX_DATA_VALID_PERCENTAGE: Incomplete
CV_WX_DATA_VALID_TEMP_RANGE: Incomplete
CV_WX_DATA_VALID_RAIN_RANGE: Incomplete
CV_WX_DATA_VALID_WIND_SPEED: Incomplete
CV_WX_DATA_VALID_PRESSURE: Incomplete
CV_WX_DATA_VALID_SOLARRAD: Incomplete
SERVICE_NAME_PAUSE_WATERING: str
SERVICE_NAME_PUSH_FLOW_METER_DATA: str
SERVICE_NAME_PUSH_WEATHER_DATA: str
SERVICE_NAME_RESTRICT_WATERING: str
SERVICE_NAME_STOP_ALL: str
SERVICE_NAME_UNPAUSE_WATERING: str
SERVICE_NAME_UNRESTRICT_WATERING: str
SERVICE_SCHEMA: Incomplete
SERVICE_PAUSE_WATERING_SCHEMA: Incomplete
SERVICE_PUSH_FLOW_METER_DATA_SCHEMA: Incomplete
SERVICE_PUSH_WEATHER_DATA_SCHEMA: Incomplete
SERVICE_RESTRICT_WATERING_SCHEMA: Incomplete
COORDINATOR_UPDATE_INTERVAL_MAP: Incomplete
type RainMachineConfigEntry = ConfigEntry[RainMachineData]

@dataclass
class RainMachineData:
    controller: Controller
    coordinators: dict[str, RainMachineDataUpdateCoordinator]

@callback
def async_get_entry_for_service_call(hass: HomeAssistant, call: ServiceCall) -> RainMachineConfigEntry: ...
async def async_update_programs_and_zones(hass: HomeAssistant, entry: RainMachineConfigEntry) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: RainMachineConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: RainMachineConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: RainMachineConfigEntry) -> bool: ...
async def async_reload_entry(hass: HomeAssistant, entry: RainMachineConfigEntry) -> None: ...
