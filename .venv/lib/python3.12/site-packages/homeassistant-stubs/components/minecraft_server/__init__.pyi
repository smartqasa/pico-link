import homeassistant.helpers.entity_registry as er
from .api import MinecraftServer as MinecraftServer, MinecraftServerAddressError as MinecraftServerAddressError, MinecraftServerType as MinecraftServerType
from .const import DOMAIN as DOMAIN, KEY_LATENCY as KEY_LATENCY, KEY_MOTD as KEY_MOTD
from .coordinator import MinecraftServerCoordinator as MinecraftServerCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PORT as CONF_PORT, CONF_TYPE as CONF_TYPE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from typing import Any

PLATFORMS: Incomplete
_LOGGER: Incomplete

def load_dnspython_rdata_classes() -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def _async_migrate_device_identifiers(hass: HomeAssistant, config_entry: ConfigEntry, old_unique_id: str | None) -> None: ...
@callback
def _migrate_entity_unique_id(entity_entry: er.RegistryEntry) -> dict[str, Any]: ...
