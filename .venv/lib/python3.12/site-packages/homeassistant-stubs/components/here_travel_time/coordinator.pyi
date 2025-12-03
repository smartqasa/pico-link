from .const import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN, ROUTE_MODE_FASTEST as ROUTE_MODE_FASTEST
from .model import HERETravelTimeConfig as HERETravelTimeConfig, HERETravelTimeData as HERETravelTimeData
from _typeshed import Incomplete
from datetime import datetime, time
from homeassistant.const import UnitOfLength as UnitOfLength
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.location import find_coordinates as find_coordinates
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util.unit_conversion import DistanceConverter as DistanceConverter
from typing import Any

BACKOFF_MULTIPLIER: float
_LOGGER: Incomplete

class HERERoutingDataUpdateCoordinator(DataUpdateCoordinator[HERETravelTimeData]):
    _api: Incomplete
    config: Incomplete
    def __init__(self, hass: HomeAssistant, api_key: str, config: HERETravelTimeConfig) -> None: ...
    update_interval: Incomplete
    async def _async_update_data(self) -> HERETravelTimeData: ...
    def _parse_routing_response(self, response: dict[str, Any]) -> HERETravelTimeData: ...

class HERETransitDataUpdateCoordinator(DataUpdateCoordinator[HERETravelTimeData | None]):
    _api: Incomplete
    config: Incomplete
    def __init__(self, hass: HomeAssistant, api_key: str, config: HERETravelTimeConfig) -> None: ...
    update_interval: Incomplete
    async def _async_update_data(self) -> HERETravelTimeData | None: ...
    def _parse_transit_response(self, response: dict[str, Any]) -> HERETravelTimeData: ...

def prepare_parameters(hass: HomeAssistant, config: HERETravelTimeConfig) -> tuple[list[str], list[str], str | None, str | None]: ...
def build_hass_attribution(sections: list[dict[str, Any]]) -> str | None: ...
def next_datetime(simple_time: time) -> datetime: ...
