from .const import CONF_CITY as CONF_CITY, CONF_GEOGRAPHIES as CONF_GEOGRAPHIES, CONF_INTEGRATION_TYPE as CONF_INTEGRATION_TYPE, DOMAIN as DOMAIN, INTEGRATION_TYPE_GEOGRAPHY_COORDS as INTEGRATION_TYPE_GEOGRAPHY_COORDS, INTEGRATION_TYPE_GEOGRAPHY_NAME as INTEGRATION_TYPE_GEOGRAPHY_NAME, INTEGRATION_TYPE_NODE_PRO as INTEGRATION_TYPE_NODE_PRO, LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import Mapping
from datetime import timedelta
from homeassistant.components import automation as automation
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_COUNTRY as CONF_COUNTRY, CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_SHOW_ON_MAP as CONF_SHOW_ON_MAP, CONF_STATE as CONF_STATE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

type AirVisualConfigEntry = ConfigEntry[DataUpdateCoordinator]
DOMAIN_AIRVISUAL_PRO: str
PLATFORMS: Incomplete
DEFAULT_ATTRIBUTION: str

@callback
def async_get_cloud_api_update_interval(hass: HomeAssistant, api_key: str, num_consumers: int) -> timedelta: ...
@callback
def async_get_cloud_coordinators_by_api_key(hass: HomeAssistant, api_key: str) -> list[DataUpdateCoordinator]: ...
@callback
def async_get_geography_id(geography_dict: Mapping[str, Any]) -> str: ...
@callback
def async_sync_geo_coordinator_update_intervals(hass: HomeAssistant, api_key: str) -> None: ...
@callback
def _standardize_geography_config_entry(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: AirVisualConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: AirVisualConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AirVisualConfigEntry) -> bool: ...
async def async_reload_entry(hass: HomeAssistant, entry: AirVisualConfigEntry) -> None: ...
