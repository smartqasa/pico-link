from .const import DOMAIN as DOMAIN, IS_IN_BED as IS_IN_BED, SLEEP_NUMBER as SLEEP_NUMBER
from .coordinator import SleepIQData as SleepIQData, SleepIQDataUpdateCoordinator as SleepIQDataUpdateCoordinator, SleepIQPauseUpdateCoordinator as SleepIQPauseUpdateCoordinator
from _typeshed import Incomplete
from asyncsleepiq import AsyncSleepIQ
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, PRESSURE as PRESSURE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
PLATFORMS: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def _async_migrate_unique_ids(hass: HomeAssistant, entry: ConfigEntry, gateway: AsyncSleepIQ) -> None: ...
