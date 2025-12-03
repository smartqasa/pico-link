from .const import ATTR_APPLICATION as ATTR_APPLICATION, ATTR_KEY as ATTR_KEY, ATTR_URL as ATTR_URL, ATTR_VALUE as ATTR_VALUE, DOMAIN as DOMAIN, SERVICE_LOAD_URL as SERVICE_LOAD_URL, SERVICE_SET_CONFIG as SERVICE_SET_CONFIG, SERVICE_START_APPLICATION as SERVICE_START_APPLICATION
from .coordinator import FullyKioskDataUpdateCoordinator as FullyKioskDataUpdateCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError

async def async_setup_services(hass: HomeAssistant) -> None: ...
