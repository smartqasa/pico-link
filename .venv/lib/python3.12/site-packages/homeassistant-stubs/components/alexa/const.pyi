from _typeshed import Incomplete
from collections import OrderedDict
from homeassistant.components import climate as climate
from homeassistant.const import UnitOfTemperature as UnitOfTemperature

DOMAIN: str
EVENT_ALEXA_SMART_HOME: str
CONF_UID: str
CONF_TITLE: str
CONF_AUDIO: str
CONF_TEXT: str
CONF_DISPLAY_URL: str
CONF_FILTER: str
CONF_ENTITY_CONFIG: str
CONF_ENDPOINT: str
CONF_LOCALE: str
ATTR_UID: str
ATTR_UPDATE_DATE: str
ATTR_TITLE_TEXT: str
ATTR_STREAM_URL: str
ATTR_MAIN_TEXT: str
ATTR_REDIRECTION_URL: str
SYN_RESOLUTION_MATCH: str
DATE_FORMAT: str
API_DIRECTIVE: str
API_ENDPOINT: str
API_EVENT: str
API_CONTEXT: str
API_HEADER: str
API_PAYLOAD: str
API_SCOPE: str
API_CHANGE: str
API_PASSWORD: str
CONF_DISPLAY_CATEGORIES: str
CONF_SUPPORTED_LOCALES: Incomplete
API_TEMP_UNITS: Incomplete
API_THERMOSTAT_MODES: OrderedDict[str, str]
API_THERMOSTAT_MODES_CUSTOM: Incomplete
API_THERMOSTAT_PRESETS: Incomplete
PRESET_MODE_NA: str
STORAGE_ACCESS_TOKEN: str
STORAGE_REFRESH_TOKEN: str

class Cause:
    APP_INTERACTION: str
    PHYSICAL_INTERACTION: str
    PERIODIC_POLL: str
    RULE_TRIGGER: str
    VOICE_INTERACTION: str

class Inputs:
    VALID_SOURCE_NAME_MAP: Incomplete
    VALID_SOUND_MODE_MAP: Incomplete
