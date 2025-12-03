from .const import CONF_POLLING as CONF_POLLING, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from dataclasses import dataclass, field
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_DATE as ATTR_DATE, ATTR_DEVICE_ID as ATTR_DEVICE_ID, ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_TIME as ATTR_TIME, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.dispatcher import dispatcher_send as dispatcher_send
from homeassistant.helpers.typing import ConfigType as ConfigType
from jaraco.abode.client import Client as Abode

SERVICE_SETTINGS: str
SERVICE_CAPTURE_IMAGE: str
SERVICE_TRIGGER_AUTOMATION: str
ATTR_DEVICE_NAME: str
ATTR_DEVICE_TYPE: str
ATTR_EVENT_CODE: str
ATTR_EVENT_NAME: str
ATTR_EVENT_TYPE: str
ATTR_EVENT_UTC: str
ATTR_SETTING: str
ATTR_USER_NAME: str
ATTR_APP_TYPE: str
ATTR_EVENT_BY: str
ATTR_VALUE: str
CONFIG_SCHEMA: Incomplete
CHANGE_SETTING_SCHEMA: Incomplete
CAPTURE_IMAGE_SCHEMA: Incomplete
AUTOMATION_SCHEMA: Incomplete
PLATFORMS: Incomplete

@dataclass
class AbodeSystem:
    abode: Abode
    polling: bool
    entity_ids: set[str | None] = field(default_factory=set)
    logout_listener: CALLBACK_TYPE | None = ...

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
def setup_hass_services(hass: HomeAssistant) -> None: ...
async def setup_hass_events(hass: HomeAssistant) -> None: ...
def setup_abode_events(hass: HomeAssistant) -> None: ...
