import asyncio
from .const import CONF_DEVICE_TOKEN as CONF_DEVICE_TOKEN, DEFAULT_TIMEOUT as DEFAULT_TIMEOUT, EXCEPTION_DETAILS as EXCEPTION_DETAILS, EXCEPTION_UNKNOWN as EXCEPTION_UNKNOWN, SYNOLOGY_CONNECTION_EXCEPTIONS as SYNOLOGY_CONNECTION_EXCEPTIONS
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from synology_dsm import SynologyDSM
from synology_dsm.api.core.security import SynoCoreSecurity
from synology_dsm.api.core.system import SynoCoreSystem
from synology_dsm.api.core.upgrade import SynoCoreUpgrade
from synology_dsm.api.core.utilization import SynoCoreUtilization
from synology_dsm.api.dsm.information import SynoDSMInformation
from synology_dsm.api.dsm.network import SynoDSMNetwork as SynoDSMNetwork
from synology_dsm.api.photos import SynoPhotos as SynoPhotos
from synology_dsm.api.storage.storage import SynoStorage
from synology_dsm.api.surveillance_station import SynoSurveillanceStation

LOGGER: Incomplete

class SynoApi:
    dsm: SynologyDSM
    _hass: Incomplete
    _entry: Incomplete
    config_url: Incomplete
    information: SynoDSMInformation | None
    network: SynoDSMNetwork | None
    security: SynoCoreSecurity | None
    storage: SynoStorage | None
    photos: SynoPhotos | None
    surveillance_station: SynoSurveillanceStation | None
    system: SynoCoreSystem | None
    upgrade: SynoCoreUpgrade | None
    utilisation: SynoCoreUtilization | None
    _fetching_entities: dict[str, set[str]]
    _with_information: bool
    _with_security: bool
    _with_storage: bool
    _with_photos: bool
    _with_surveillance_station: bool
    _with_system: bool
    _with_upgrade: bool
    _with_utilisation: bool
    _login_future: asyncio.Future[None] | None
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None: ...
    async def async_login(self) -> None: ...
    async def async_setup(self) -> None: ...
    @callback
    def subscribe(self, api_key: str, unique_id: str) -> Callable[[], None]: ...
    def _setup_api_requests(self) -> None: ...
    async def _fetch_device_configuration(self) -> None: ...
    async def _syno_api_executer(self, api_call: Callable) -> None: ...
    async def async_reboot(self) -> None: ...
    async def async_shutdown(self) -> None: ...
    async def async_unload(self) -> None: ...
    async def async_update(self) -> None: ...
    async def _update(self) -> None: ...

def raise_config_entry_auth_error(err: Exception) -> None: ...
