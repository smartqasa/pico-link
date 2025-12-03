from _typeshed import Incomplete
from homeassistant import config_entries as config_entries, setup as setup
from homeassistant.components import persistent_notification as persistent_notification
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START, Platform as Platform, UnitOfSoundPressure as UnitOfSoundPressure
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.helpers.discovery import async_load_platform as async_load_platform
from homeassistant.helpers.typing import ConfigType as ConfigType

DOMAIN: str
COMPONENTS_WITH_CONFIG_ENTRY_DEMO_PLATFORM: Incomplete
COMPONENTS_WITH_DEMO_PLATFORM: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def finish_setup(hass: HomeAssistant, config: ConfigType) -> None: ...
