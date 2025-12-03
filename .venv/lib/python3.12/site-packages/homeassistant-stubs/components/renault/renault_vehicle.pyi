from .const import DOMAIN as DOMAIN
from .coordinator import RenaultDataUpdateCoordinator as RenaultDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable, Coroutine
from dataclasses import dataclass
from datetime import datetime, timedelta
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from renault_api.kamereon import models as models
from renault_api.renault_vehicle import RenaultVehicle as RenaultVehicle
from typing import Any, Concatenate

LOGGER: Incomplete

def with_error_wrapping[**_P, _R](func: Callable[Concatenate[RenaultVehicleProxy, _P], Awaitable[_R]]) -> Callable[Concatenate[RenaultVehicleProxy, _P], Coroutine[Any, Any, _R]]: ...

@dataclass
class RenaultCoordinatorDescription:
    endpoint: str
    key: str
    update_method: Callable[[RenaultVehicle], Callable[[], Awaitable[models.KamereonVehicleDataAttributes]]]
    requires_electricity: bool = ...

class RenaultVehicleProxy:
    hass: Incomplete
    _vehicle: Incomplete
    _details: Incomplete
    _device_info: Incomplete
    coordinators: dict[str, RenaultDataUpdateCoordinator]
    hvac_target_temperature: int
    _scan_interval: Incomplete
    def __init__(self, hass: HomeAssistant, vehicle: RenaultVehicle, details: models.KamereonVehicleDetails, scan_interval: timedelta) -> None: ...
    @property
    def details(self) -> models.KamereonVehicleDetails: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    async def async_initialise(self) -> None: ...
    @with_error_wrapping
    async def set_charge_mode(self, charge_mode: str) -> models.KamereonVehicleChargeModeActionData: ...
    @with_error_wrapping
    async def set_charge_start(self) -> models.KamereonVehicleChargingStartActionData: ...
    @with_error_wrapping
    async def set_charge_stop(self) -> models.KamereonVehicleChargingStartActionData: ...
    @with_error_wrapping
    async def set_ac_stop(self) -> models.KamereonVehicleHvacStartActionData: ...
    @with_error_wrapping
    async def set_ac_start(self, temperature: float, when: datetime | None = None) -> models.KamereonVehicleHvacStartActionData: ...
    @with_error_wrapping
    async def get_hvac_settings(self) -> models.KamereonVehicleHvacSettingsData: ...
    @with_error_wrapping
    async def set_hvac_schedules(self, schedules: list[models.HvacSchedule]) -> models.KamereonVehicleHvacScheduleActionData: ...
    @with_error_wrapping
    async def get_charging_settings(self) -> models.KamereonVehicleChargingSettingsData: ...
    @with_error_wrapping
    async def set_charge_schedules(self, schedules: list[models.ChargeSchedule]) -> models.KamereonVehicleChargeScheduleActionData: ...

COORDINATORS: tuple[RenaultCoordinatorDescription, ...]
