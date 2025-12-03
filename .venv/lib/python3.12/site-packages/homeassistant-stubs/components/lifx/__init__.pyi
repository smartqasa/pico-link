from .const import DATA_LIFX_MANAGER as DATA_LIFX_MANAGER, DOMAIN as DOMAIN, TARGET_ANY as TARGET_ANY, _LOGGER as _LOGGER
from .coordinator import LIFXUpdateCoordinator as LIFXUpdateCoordinator
from .discovery import async_discover_devices as async_discover_devices, async_trigger_discovery as async_trigger_discovery
from .manager import LIFXManager as LIFXManager
from .migration import async_migrate_entities_devices as async_migrate_entities_devices, async_migrate_legacy_entries as async_migrate_legacy_entries
from .util import async_entry_is_legacy as async_entry_is_legacy, async_get_legacy_entry as async_get_legacy_entry, formatted_serial as formatted_serial
from _typeshed import Incomplete
from aiolifx.aiolifx import Light as Light
from collections.abc import Iterable
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED, Platform as Platform
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.event import async_call_later as async_call_later, async_track_time_interval as async_track_time_interval
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

CONF_SERVER: str
CONF_BROADCAST: str
INTERFACE_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete
PLATFORMS: Incomplete
DISCOVERY_INTERVAL: Incomplete
MIGRATION_INTERVAL: Incomplete
DISCOVERY_COOLDOWN: int

async def async_legacy_migration(hass: HomeAssistant, legacy_entry: ConfigEntry, discovered_devices: Iterable[Light]) -> bool: ...

class LIFXDiscoveryManager:
    hass: Incomplete
    lock: Incomplete
    migrating: Incomplete
    _cancel_discovery: CALLBACK_TYPE | None
    def __init__(self, hass: HomeAssistant, migrating: bool) -> None: ...
    @callback
    def async_setup_discovery_interval(self) -> None: ...
    async def async_discovery(self, *_: Any) -> None: ...

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
