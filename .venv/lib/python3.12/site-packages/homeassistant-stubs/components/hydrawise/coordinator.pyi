from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, MAIN_SCAN_INTERVAL as MAIN_SCAN_INTERVAL, WATER_USE_SCAN_INTERVAL as WATER_USE_SCAN_INTERVAL
from _typeshed import Incomplete
from dataclasses import dataclass, field
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from homeassistant.util.dt import now as now
from pydrawise import Hydrawise as Hydrawise
from pydrawise.schema import Controller as Controller, ControllerWaterUseSummary as ControllerWaterUseSummary, Sensor as Sensor, User as User, Zone as Zone

@dataclass
class HydrawiseData:
    user: User
    controllers: dict[int, Controller] = field(default_factory=dict)
    zones: dict[int, Zone] = field(default_factory=dict)
    sensors: dict[int, Sensor] = field(default_factory=dict)
    daily_water_summary: dict[int, ControllerWaterUseSummary] = field(default_factory=dict)

@dataclass
class HydrawiseUpdateCoordinators:
    main: HydrawiseMainDataUpdateCoordinator
    water_use: HydrawiseWaterUseDataUpdateCoordinator

class HydrawiseDataUpdateCoordinator(DataUpdateCoordinator[HydrawiseData]):
    api: Hydrawise

class HydrawiseMainDataUpdateCoordinator(HydrawiseDataUpdateCoordinator):
    api: Incomplete
    def __init__(self, hass: HomeAssistant, api: Hydrawise) -> None: ...
    async def _async_update_data(self) -> HydrawiseData: ...

class HydrawiseWaterUseDataUpdateCoordinator(HydrawiseDataUpdateCoordinator):
    _main_coordinator: HydrawiseMainDataUpdateCoordinator
    api: Incomplete
    def __init__(self, hass: HomeAssistant, api: Hydrawise, main_coordinator: HydrawiseMainDataUpdateCoordinator) -> None: ...
    async def _async_update_data(self) -> HydrawiseData: ...
