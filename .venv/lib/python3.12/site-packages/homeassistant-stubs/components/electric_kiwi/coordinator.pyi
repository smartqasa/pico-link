from _typeshed import Incomplete
from electrickiwi_api import ElectricKiwiApi as ElectricKiwiApi
from electrickiwi_api.model import AccountBalance, Hop, HopIntervals as HopIntervals
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
ACCOUNT_SCAN_INTERVAL: Incomplete
HOP_SCAN_INTERVAL: Incomplete

class ElectricKiwiAccountDataCoordinator(DataUpdateCoordinator[AccountBalance]):
    _ek_api: Incomplete
    def __init__(self, hass: HomeAssistant, ek_api: ElectricKiwiApi) -> None: ...
    async def _async_update_data(self) -> AccountBalance: ...

class ElectricKiwiHOPDataCoordinator(DataUpdateCoordinator[Hop]):
    _ek_api: Incomplete
    hop_intervals: HopIntervals | None
    def __init__(self, hass: HomeAssistant, ek_api: ElectricKiwiApi) -> None: ...
    def get_hop_options(self) -> dict[str, int]: ...
    async def async_update_hop(self, hop_interval: int) -> Hop: ...
    async def _async_update_data(self) -> Hop: ...
