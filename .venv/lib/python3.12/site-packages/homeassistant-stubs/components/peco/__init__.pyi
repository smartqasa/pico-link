from .const import CONF_COUNTY as CONF_COUNTY, CONF_PHONE_NUMBER as CONF_PHONE_NUMBER, DOMAIN as DOMAIN, LOGGER as LOGGER, OUTAGE_SCAN_INTERVAL as OUTAGE_SCAN_INTERVAL, SMART_METER_SCAN_INTERVAL as SMART_METER_SCAN_INTERVAL
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from peco import AlertResults as AlertResults, OutageResults as OutageResults
from typing import Final

PLATFORMS: Final[Incomplete]

@dataclass
class PECOCoordinatorData:
    outages: OutageResults
    alerts: AlertResults

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
