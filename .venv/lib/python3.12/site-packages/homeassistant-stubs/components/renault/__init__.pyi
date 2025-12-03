from .const import CONF_LOCALE as CONF_LOCALE, DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .renault_hub import RenaultHub as RenaultHub
from .services import setup_services as setup_services
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.typing import ConfigType as ConfigType

CONFIG_SCHEMA: Incomplete
type RenaultConfigEntry = ConfigEntry[RenaultHub]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: RenaultConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: RenaultConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: RenaultConfigEntry, device_entry: dr.DeviceEntry) -> bool: ...
