from .const import DOMAIN as DOMAIN, InputSource as InputSource, OPTION_INPUT_SOURCES as OPTION_INPUT_SOURCES
from .receiver import Receiver as Receiver, async_interview as async_interview
from .services import DATA_MP_ENTITIES as DATA_MP_ENTITIES, async_register_services as async_register_services
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.typing import ConfigType as ConfigType

PLATFORMS: Incomplete
CONFIG_SCHEMA: Incomplete

@dataclass
class OnkyoData:
    receiver: Receiver
    sources: dict[InputSource, str]
type OnkyoConfigEntry = ConfigEntry[OnkyoData]

async def async_setup(hass: HomeAssistant, _: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: OnkyoConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: OnkyoConfigEntry) -> bool: ...
async def update_listener(hass: HomeAssistant, entry: OnkyoConfigEntry) -> None: ...
