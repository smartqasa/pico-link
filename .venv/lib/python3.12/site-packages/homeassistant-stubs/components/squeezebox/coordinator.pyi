from .const import PLAYER_UPDATE_INTERVAL as PLAYER_UPDATE_INTERVAL, SENSOR_UPDATE_INTERVAL as SENSOR_UPDATE_INTERVAL, SIGNAL_PLAYER_REDISCOVERED as SIGNAL_PLAYER_REDISCOVERED, STATUS_API_TIMEOUT as STATUS_API_TIMEOUT, STATUS_SENSOR_LASTSCAN as STATUS_SENSOR_LASTSCAN, STATUS_SENSOR_NEEDSRESTART as STATUS_SENSOR_NEEDSRESTART, STATUS_SENSOR_RESCAN as STATUS_SENSOR_RESCAN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pysqueezebox import Player as Player, Server as Server
from typing import Any

_LOGGER: Incomplete

class LMSStatusDataUpdateCoordinator(DataUpdateCoordinator):
    lms: Incomplete
    newversion_regex: Incomplete
    def __init__(self, hass: HomeAssistant, lms: Server) -> None: ...
    async def _async_update_data(self) -> dict: ...
    def _prepare_status_data(self, data: dict) -> dict: ...

class SqueezeBoxPlayerUpdateCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    player: Incomplete
    available: bool
    _remove_dispatcher: Callable | None
    server_uuid: Incomplete
    def __init__(self, hass: HomeAssistant, player: Player, server_uuid: str) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
    @callback
    def rediscovered(self, unique_id: str, connected: bool) -> None: ...
