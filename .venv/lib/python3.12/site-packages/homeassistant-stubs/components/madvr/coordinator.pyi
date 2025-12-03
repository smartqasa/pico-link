from . import MadVRConfigEntry as MadVRConfigEntry
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from madvr.madvr import Madvr as Madvr
from typing import Any

_LOGGER: Incomplete

class MadVRCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    config_entry: MadVRConfigEntry
    mac: Incomplete
    client: Incomplete
    data: Incomplete
    def __init__(self, hass: HomeAssistant, client: Madvr) -> None: ...
    def handle_push_data(self, data: dict[str, Any]) -> None: ...
    async def handle_coordinator_load(self) -> None: ...
