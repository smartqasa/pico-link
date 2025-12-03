import asyncio
from .const import API_SENSOR_PAIRED_SENSOR_STATUS as API_SENSOR_PAIRED_SENSOR_STATUS, API_SENSOR_PAIR_DUMP as API_SENSOR_PAIR_DUMP, API_SYSTEM_DIAGNOSTICS as API_SYSTEM_DIAGNOSTICS, API_SYSTEM_ONBOARD_SENSOR_STATUS as API_SYSTEM_ONBOARD_SENSOR_STATUS, API_VALVE_STATUS as API_VALVE_STATUS, API_WIFI_STATUS as API_WIFI_STATUS, CONF_UID as CONF_UID, DOMAIN as DOMAIN, LOGGER as LOGGER, SIGNAL_PAIRED_SENSOR_COORDINATOR_ADDED as SIGNAL_PAIRED_SENSOR_COORDINATOR_ADDED
from .coordinator import GuardianDataUpdateCoordinator as GuardianDataUpdateCoordinator
from _typeshed import Incomplete
from aioguardian import Client
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_FILENAME as CONF_FILENAME, CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_PORT as CONF_PORT, CONF_URL as CONF_URL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send

DATA_PAIRED_SENSOR_MANAGER: str
SERVICE_NAME_PAIR_SENSOR: str
SERVICE_NAME_UNPAIR_SENSOR: str
SERVICE_NAME_UPGRADE_FIRMWARE: str
SERVICES: Incomplete
SERVICE_BASE_SCHEMA: Incomplete
SERVICE_PAIR_UNPAIR_SENSOR_SCHEMA: Incomplete
SERVICE_UPGRADE_FIRMWARE_SCHEMA: Incomplete
PLATFORMS: Incomplete

@dataclass
class GuardianData:
    entry: ConfigEntry
    client: Client
    valve_controller_coordinators: dict[str, GuardianDataUpdateCoordinator]
    paired_sensor_manager: PairedSensorManager

@callback
def async_get_entry_id_for_service_call(hass: HomeAssistant, call: ServiceCall) -> str: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class PairedSensorManager:
    _api_lock: Incomplete
    _client: Incomplete
    _entry: Incomplete
    _hass: Incomplete
    _paired_uids: set[str]
    _sensor_pair_dump_coordinator: Incomplete
    coordinators: dict[str, GuardianDataUpdateCoordinator]
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, client: Client, api_lock: asyncio.Lock, sensor_pair_dump_coordinator: GuardianDataUpdateCoordinator) -> None: ...
    async def async_initialize(self) -> None: ...
    async def async_pair_sensor(self, uid: str) -> None: ...
    async def async_process_latest_paired_sensor_uids(self) -> None: ...
    async def async_unpair_sensor(self, uid: str) -> None: ...
