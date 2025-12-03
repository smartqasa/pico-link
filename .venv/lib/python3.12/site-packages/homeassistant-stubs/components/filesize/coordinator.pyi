import os
import pathlib
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete

class FileSizeCoordinator(DataUpdateCoordinator[dict[str, int | float | datetime]]):
    path: pathlib.Path
    _unresolved_path: Incomplete
    def __init__(self, hass: HomeAssistant, unresolved_path: str) -> None: ...
    def _get_full_path(self) -> pathlib.Path: ...
    def _update(self) -> os.stat_result: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> dict[str, float | int | datetime]: ...
