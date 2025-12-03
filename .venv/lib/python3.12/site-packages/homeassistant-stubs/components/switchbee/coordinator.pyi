from .const import DOMAIN as DOMAIN, SCAN_INTERVAL_SEC as SCAN_INTERVAL_SEC
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from switchbee.api import CentralUnitPolling as CentralUnitPolling, CentralUnitWsRPC
from switchbee.device import SwitchBeeBaseDevice

_LOGGER: Incomplete

class SwitchBeeCoordinator(DataUpdateCoordinator[Mapping[int, SwitchBeeBaseDevice]]):
    api: CentralUnitPolling | CentralUnitWsRPC
    _reconnect_counts: int
    unique_id: Incomplete
    def __init__(self, hass: HomeAssistant, swb_api: CentralUnitPolling | CentralUnitWsRPC) -> None: ...
    @callback
    def _async_handle_update(self, push_data: dict) -> None: ...
    async def _async_update_data(self) -> Mapping[int, SwitchBeeBaseDevice]: ...
