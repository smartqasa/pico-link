from .const import DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_BROADCAST_ADDRESS as CONF_BROADCAST_ADDRESS, CONF_BROADCAST_PORT as CONF_BROADCAST_PORT, CONF_MAC as CONF_MAC
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
SERVICE_SEND_MAGIC_PACKET: str
WAKE_ON_LAN_SEND_MAGIC_PACKET_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
