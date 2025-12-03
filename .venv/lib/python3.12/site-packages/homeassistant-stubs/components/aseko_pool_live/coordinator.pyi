from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from aioaseko import Aseko as Aseko, Unit
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

_LOGGER: Incomplete
type AsekoConfigEntry = ConfigEntry[AsekoDataUpdateCoordinator]

class AsekoDataUpdateCoordinator(DataUpdateCoordinator[dict[str, Unit]]):
    _aseko: Incomplete
    def __init__(self, hass: HomeAssistant, aseko: Aseko) -> None: ...
    async def _async_update_data(self) -> dict[str, Unit]: ...
