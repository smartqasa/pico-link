from .bridge import SamsungTVBridge as SamsungTVBridge, async_get_device_info as async_get_device_info, mac_from_device_info as mac_from_device_info, model_requires_encryption as model_requires_encryption
from .const import CONF_SESSION_ID as CONF_SESSION_ID, CONF_SSDP_MAIN_TV_AGENT_LOCATION as CONF_SSDP_MAIN_TV_AGENT_LOCATION, CONF_SSDP_RENDERING_CONTROL_LOCATION as CONF_SSDP_RENDERING_CONTROL_LOCATION, ENTRY_RELOAD_COOLDOWN as ENTRY_RELOAD_COOLDOWN, LEGACY_PORT as LEGACY_PORT, LOGGER as LOGGER, METHOD_ENCRYPTED_WEBSOCKET as METHOD_ENCRYPTED_WEBSOCKET, METHOD_LEGACY as METHOD_LEGACY, UPNP_SVC_MAIN_TV_AGENT as UPNP_SVC_MAIN_TV_AGENT, UPNP_SVC_RENDERING_CONTROL as UPNP_SVC_RENDERING_CONTROL
from .coordinator import SamsungTVDataUpdateCoordinator as SamsungTVDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Coroutine
from homeassistant.components import ssdp as ssdp
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_METHOD as CONF_METHOD, CONF_MODEL as CONF_MODEL, CONF_PORT as CONF_PORT, CONF_TOKEN as CONF_TOKEN, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.debounce import Debouncer as Debouncer
from typing import Any

PLATFORMS: Incomplete
SamsungTVConfigEntry = ConfigEntry[SamsungTVDataUpdateCoordinator]

@callback
def _async_get_device_bridge(hass: HomeAssistant, data: dict[str, Any]) -> SamsungTVBridge: ...

class DebouncedEntryReloader:
    hass: Incomplete
    entry: Incomplete
    token: Incomplete
    _debounced_reload: Debouncer[Coroutine[Any, Any, None]]
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None: ...
    async def async_call(self, hass: HomeAssistant, entry: ConfigEntry) -> None: ...
    @callback
    def async_shutdown(self) -> None: ...
    async def _async_reload_entry(self) -> None: ...

async def _async_update_ssdp_locations(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: SamsungTVConfigEntry) -> bool: ...
async def _async_create_bridge_with_updated_data(hass: HomeAssistant, entry: ConfigEntry) -> SamsungTVBridge: ...
async def async_unload_entry(hass: HomeAssistant, entry: SamsungTVConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
