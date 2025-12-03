from .const import CONF_STORAGE_KEY as CONF_STORAGE_KEY, CONF_TODO_LIST_NAME as CONF_TODO_LIST_NAME
from .store import LocalTodoListStore as LocalTodoListStore
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.util import slugify as slugify

PLATFORMS: list[Platform]
STORAGE_PATH: str
type LocalTodoConfigEntry = ConfigEntry[LocalTodoListStore]

async def async_setup_entry(hass: HomeAssistant, entry: LocalTodoConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_remove_entry(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
