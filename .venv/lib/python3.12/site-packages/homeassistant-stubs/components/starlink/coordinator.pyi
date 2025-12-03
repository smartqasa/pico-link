from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from starlink_grpc import AlertDict as AlertDict, LocationDict as LocationDict, ObstructionDict as ObstructionDict, PowerDict as PowerDict, StatusDict as StatusDict, UsageDict as UsageDict

_LOGGER: Incomplete

@dataclass
class StarlinkData:
    location: LocationDict
    sleep: tuple[int, int, bool]
    status: StatusDict
    obstruction: ObstructionDict
    alert: AlertDict
    usage: UsageDict
    consumption: PowerDict

class StarlinkUpdateCoordinator(DataUpdateCoordinator[StarlinkData]):
    channel_context: Incomplete
    timezone: Incomplete
    def __init__(self, hass: HomeAssistant, name: str, url: str) -> None: ...
    def _get_starlink_data(self) -> StarlinkData: ...
    async def _async_update_data(self) -> StarlinkData: ...
    async def async_stow_starlink(self, stow: bool) -> None: ...
    async def async_reboot_starlink(self) -> None: ...
    async def async_set_sleep_schedule_enabled(self, sleep_schedule: bool) -> None: ...
    async def async_set_sleep_start(self, start: int) -> None: ...
    async def async_set_sleep_duration(self, end: int) -> None: ...
