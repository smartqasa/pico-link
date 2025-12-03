from .const import CONF_INDEX as CONF_INDEX, CONF_SELECT as CONF_SELECT, DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .coordinator import ScrapeCoordinator as ScrapeCoordinator
from _typeshed import Incomplete
from homeassistant.components.rest import RESOURCE_SCHEMA as RESOURCE_SCHEMA, create_rest_data_from_config as create_rest_data_from_config
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ATTRIBUTE as CONF_ATTRIBUTE, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import discovery as discovery
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from homeassistant.helpers.trigger_template_entity import CONF_AVAILABILITY as CONF_AVAILABILITY, TEMPLATE_SENSOR_BASE_SCHEMA as TEMPLATE_SENSOR_BASE_SCHEMA
from homeassistant.helpers.typing import ConfigType as ConfigType

type ScrapeConfigEntry = ConfigEntry[ScrapeCoordinator]
SENSOR_SCHEMA: Incomplete
COMBINED_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ScrapeConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_remove_config_entry_device(hass: HomeAssistant, entry: ConfigEntry, device: DeviceEntry) -> bool: ...
