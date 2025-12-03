from .const import LOGGER as LOGGER, SCAN_INTERVAL_MINUTES as SCAN_INTERVAL_MINUTES
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from sensoterra.customerapi import CustomerApi as CustomerApi
from sensoterra.probe import Probe, Sensor as Sensor

class SensoterraCoordinator(DataUpdateCoordinator[list[Probe]]):
    api: Incomplete
    add_devices_callback: Callable[[list[Probe]], None] | None
    def __init__(self, hass: HomeAssistant, api: CustomerApi) -> None: ...
    async def _async_update_data(self) -> list[Probe]: ...
    def get_sensor(self, id: str | None) -> Sensor | None: ...
