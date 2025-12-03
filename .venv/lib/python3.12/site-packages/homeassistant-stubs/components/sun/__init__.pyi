from .const import DOMAIN as DOMAIN, STATE_ABOVE_HORIZON as STATE_ABOVE_HORIZON, STATE_BELOW_HORIZON as STATE_BELOW_HORIZON
from .entity import Sun as Sun, SunConfigEntry as SunConfigEntry
from _typeshed import Incomplete
from homeassistant.config_entries import SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType

CONFIG_SCHEMA: Incomplete
_LOGGER: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: SunConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: SunConfigEntry) -> bool: ...
