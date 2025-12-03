from .const import CONF_ENABLE_IME as CONF_ENABLE_IME, CONF_ENABLE_IME_DEFAULT_VALUE as CONF_ENABLE_IME_DEFAULT_VALUE
from androidtvremote2 import AndroidTVRemote
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.storage import STORAGE_DIR as STORAGE_DIR

def create_api(hass: HomeAssistant, host: str, enable_ime: bool) -> AndroidTVRemote: ...
def get_enable_ime(entry: ConfigEntry) -> bool: ...
