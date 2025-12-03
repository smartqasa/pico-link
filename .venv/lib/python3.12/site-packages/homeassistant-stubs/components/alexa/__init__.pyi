from . import flash_briefings as flash_briefings, intent as intent, smart_home as smart_home
from .const import CONF_AUDIO as CONF_AUDIO, CONF_DISPLAY_CATEGORIES as CONF_DISPLAY_CATEGORIES, CONF_DISPLAY_URL as CONF_DISPLAY_URL, CONF_ENDPOINT as CONF_ENDPOINT, CONF_ENTITY_CONFIG as CONF_ENTITY_CONFIG, CONF_FILTER as CONF_FILTER, CONF_LOCALE as CONF_LOCALE, CONF_SUPPORTED_LOCALES as CONF_SUPPORTED_LOCALES, CONF_TEXT as CONF_TEXT, CONF_TITLE as CONF_TITLE, CONF_UID as CONF_UID, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.const import CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_CLIENT_SECRET as CONF_CLIENT_SECRET, CONF_DESCRIPTION as CONF_DESCRIPTION, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import entityfilter as entityfilter
from homeassistant.helpers.typing import ConfigType as ConfigType

CONF_FLASH_BRIEFINGS: str
CONF_SMART_HOME: str
DEFAULT_LOCALE: str
VALID_ENDPOINTS: Incomplete
ALEXA_ENTITY_SCHEMA: Incomplete
SMART_HOME_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
