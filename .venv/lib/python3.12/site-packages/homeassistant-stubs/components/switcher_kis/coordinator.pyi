from .const import DOMAIN as DOMAIN, MAX_UPDATE_INTERVAL_SEC as MAX_UPDATE_INTERVAL_SEC, SIGNAL_DEVICE_ADD as SIGNAL_DEVICE_ADD
from _typeshed import Incomplete
from aioswitcher.device import SwitcherBase
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_TOKEN as CONF_TOKEN
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import update_coordinator as update_coordinator
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send

_LOGGER: Incomplete

class SwitcherDataUpdateCoordinator(update_coordinator.DataUpdateCoordinator[SwitcherBase]):
    config_entry: ConfigEntry
    data: Incomplete
    token: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, device: SwitcherBase) -> None: ...
    async def _async_update_data(self) -> SwitcherBase: ...
    @property
    def model(self) -> str: ...
    @property
    def device_id(self) -> str: ...
    @property
    def mac_address(self) -> str: ...
    @callback
    def async_setup(self) -> None: ...
