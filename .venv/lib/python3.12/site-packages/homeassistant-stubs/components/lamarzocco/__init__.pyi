from .const import CONF_USE_BLUETOOTH as CONF_USE_BLUETOOTH, DOMAIN as DOMAIN
from .coordinator import LaMarzoccoConfigEntry as LaMarzoccoConfigEntry, LaMarzoccoConfigUpdateCoordinator as LaMarzoccoConfigUpdateCoordinator, LaMarzoccoFirmwareUpdateCoordinator as LaMarzoccoFirmwareUpdateCoordinator, LaMarzoccoRuntimeData as LaMarzoccoRuntimeData, LaMarzoccoStatisticsUpdateCoordinator as LaMarzoccoStatisticsUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.bluetooth import async_discovered_service_info as async_discovered_service_info
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_MODEL as CONF_MODEL, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_TOKEN as CONF_TOKEN, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_create_clientsession as async_create_clientsession

PLATFORMS: Incomplete
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: LaMarzoccoConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: LaMarzoccoConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: LaMarzoccoConfigEntry) -> bool: ...
