from .const import CONF_GCID as CONF_GCID, CONF_READ_ONLY as CONF_READ_ONLY, CONF_REFRESH_TOKEN as CONF_REFRESH_TOKEN, SCAN_INTERVALS as SCAN_INTERVALS
from _typeshed import Incomplete
from bimmer_connected.account import MyBMWAccount
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_REGION as CONF_REGION, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util.ssl import get_default_context as get_default_context

_LOGGER: Incomplete
type BMWConfigEntry = ConfigEntry[BMWDataUpdateCoordinator]

class BMWDataUpdateCoordinator(DataUpdateCoordinator[None]):
    account: MyBMWAccount
    config_entry: BMWConfigEntry
    read_only: bool
    last_update_success: bool
    def __init__(self, hass: HomeAssistant, *, config_entry: BMWConfigEntry) -> None: ...
    async def _async_update_data(self) -> None: ...
    def _update_config_entry_refresh_token(self, refresh_token: str | None) -> None: ...
