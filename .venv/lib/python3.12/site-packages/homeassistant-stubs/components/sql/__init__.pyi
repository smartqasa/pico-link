from .const import CONF_COLUMN_NAME as CONF_COLUMN_NAME, CONF_QUERY as CONF_QUERY, DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .util import redact_credentials as redact_credentials
from _typeshed import Incomplete
from homeassistant.components.recorder import CONF_DB_URL as CONF_DB_URL, get_instance as get_instance
from homeassistant.components.sensor import CONF_STATE_CLASS as CONF_STATE_CLASS, DEVICE_CLASSES_SCHEMA as DEVICE_CLASSES_SCHEMA, STATE_CLASSES_SCHEMA as STATE_CLASSES_SCHEMA
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_ICON as CONF_ICON, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import discovery as discovery
from homeassistant.helpers.trigger_template_entity import CONF_AVAILABILITY as CONF_AVAILABILITY, CONF_PICTURE as CONF_PICTURE
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete

def validate_sql_select(value: str) -> str: ...

QUERY_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete

def remove_configured_db_url_if_not_needed(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
