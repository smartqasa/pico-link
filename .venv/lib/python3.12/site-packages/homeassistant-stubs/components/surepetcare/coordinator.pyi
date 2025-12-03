from .const import ATTR_FLAP_ID as ATTR_FLAP_ID, ATTR_LOCATION as ATTR_LOCATION, ATTR_LOCK_STATE as ATTR_LOCK_STATE, ATTR_PET_NAME as ATTR_PET_NAME, DOMAIN as DOMAIN, SURE_API_TIMEOUT as SURE_API_TIMEOUT
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_TOKEN as CONF_TOKEN, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from surepy import SurepyEntity

_LOGGER: Incomplete
SCAN_INTERVAL: Incomplete

class SurePetcareDataCoordinator(DataUpdateCoordinator[dict[int, SurepyEntity]]):
    surepy: Incomplete
    lock_states_callbacks: Incomplete
    def __init__(self, entry: ConfigEntry, hass: HomeAssistant) -> None: ...
    async def _async_update_data(self) -> dict[int, SurepyEntity]: ...
    async def handle_set_lock_state(self, call: ServiceCall) -> None: ...
    def get_pets(self) -> dict[str, int]: ...
    async def handle_set_pet_location(self, call: ServiceCall) -> None: ...
