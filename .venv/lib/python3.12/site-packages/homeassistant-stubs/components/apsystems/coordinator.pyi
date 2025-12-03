from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from APsystemsEZ1 import APsystemsEZ1M as APsystemsEZ1M, ReturnAlarmInfo as ReturnAlarmInfo, ReturnOutputData as ReturnOutputData
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

@dataclass
class ApSystemsSensorData:
    output_data: ReturnOutputData
    alarm_info: ReturnAlarmInfo

class ApSystemsDataCoordinator(DataUpdateCoordinator[ApSystemsSensorData]):
    api: Incomplete
    def __init__(self, hass: HomeAssistant, api: APsystemsEZ1M) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> ApSystemsSensorData: ...
