import logging
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from datetime import timedelta
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from renault_api.kamereon.models import KamereonVehicleDataAttributes
from typing import TypeVar

T = TypeVar('T', bound=KamereonVehicleDataAttributes)
_PARALLEL_SEMAPHORE: Incomplete

class RenaultDataUpdateCoordinator(DataUpdateCoordinator[T]):
    update_method: Callable[[], Awaitable[T]]
    access_denied: bool
    not_supported: bool
    _has_already_worked: bool
    def __init__(self, hass: HomeAssistant, logger: logging.Logger, *, name: str, update_interval: timedelta, update_method: Callable[[], Awaitable[T]]) -> None: ...
    update_interval: Incomplete
    async def _async_update_data(self) -> T: ...
    async def async_config_entry_first_refresh(self) -> None: ...
