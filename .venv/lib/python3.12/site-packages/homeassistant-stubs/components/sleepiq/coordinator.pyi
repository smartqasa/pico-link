from _typeshed import Incomplete
from asyncsleepiq import AsyncSleepIQ as AsyncSleepIQ
from dataclasses import dataclass
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

_LOGGER: Incomplete
UPDATE_INTERVAL: Incomplete
LONGER_UPDATE_INTERVAL: Incomplete

class SleepIQDataUpdateCoordinator(DataUpdateCoordinator[None]):
    client: Incomplete
    def __init__(self, hass: HomeAssistant, client: AsyncSleepIQ, username: str) -> None: ...
    async def _async_update_data(self) -> None: ...

class SleepIQPauseUpdateCoordinator(DataUpdateCoordinator[None]):
    client: Incomplete
    def __init__(self, hass: HomeAssistant, client: AsyncSleepIQ, username: str) -> None: ...
    async def _async_update_data(self) -> None: ...

@dataclass
class SleepIQData:
    data_coordinator: SleepIQDataUpdateCoordinator
    pause_coordinator: SleepIQPauseUpdateCoordinator
    client: AsyncSleepIQ
