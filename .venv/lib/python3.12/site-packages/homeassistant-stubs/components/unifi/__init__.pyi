from .const import PLATFORMS as PLATFORMS, UNIFI_WIRELESS_CLIENTS as UNIFI_WIRELESS_CLIENTS
from .errors import AuthenticationRequired as AuthenticationRequired, CannotConnect as CannotConnect
from .hub import UnifiHub as UnifiHub, get_unifi_api as get_unifi_api
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from aiounifi.models.client import Client as Client
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.typing import ConfigType as ConfigType

type UnifiConfigEntry = ConfigEntry[UnifiHub]
SAVE_DELAY: int
STORAGE_KEY: str
STORAGE_VERSION: int
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: UnifiConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: UnifiConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: UnifiConfigEntry, device_entry: DeviceEntry) -> bool: ...

class UnifiWirelessClients:
    hass: Incomplete
    data: dict[str, dict[str, list[str]] | list[str]]
    wireless_clients: set[str]
    _store: Store
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_load(self) -> None: ...
    @callback
    def is_wireless(self, client: Client) -> bool: ...
    @callback
    def update_clients(self, clients: set[Client]) -> None: ...
    @callback
    def _data_to_save(self) -> dict[str, dict[str, list[str]] | list[str]]: ...
    def __contains__(self, obj_id: int | str) -> bool: ...
