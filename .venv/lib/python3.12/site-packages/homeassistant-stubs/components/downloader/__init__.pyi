from .const import ATTR_FILENAME as ATTR_FILENAME, ATTR_OVERWRITE as ATTR_OVERWRITE, ATTR_SUBDIR as ATTR_SUBDIR, ATTR_URL as ATTR_URL, CONF_DOWNLOAD_DIR as CONF_DOWNLOAD_DIR, DOMAIN as DOMAIN, DOWNLOAD_COMPLETED_EVENT as DOWNLOAD_COMPLETED_EVENT, DOWNLOAD_FAILED_EVENT as DOWNLOAD_FAILED_EVENT, SERVICE_DOWNLOAD_FILE as SERVICE_DOWNLOAD_FILE, _LOGGER as _LOGGER
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.helpers.service import async_register_admin_service as async_register_admin_service
from homeassistant.util import raise_if_invalid_filename as raise_if_invalid_filename, raise_if_invalid_path as raise_if_invalid_path

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
