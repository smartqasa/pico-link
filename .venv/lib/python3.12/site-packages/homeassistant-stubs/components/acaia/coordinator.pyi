from .const import CONF_IS_NEW_STYLE_SCALE as CONF_IS_NEW_STYLE_SCALE
from _typeshed import Incomplete
from aioacaia.acaiascale import AcaiaScale
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

SCAN_INTERVAL: Incomplete
_LOGGER: Incomplete
type AcaiaConfigEntry = ConfigEntry[AcaiaCoordinator]

class AcaiaCoordinator(DataUpdateCoordinator[None]):
    config_entry: AcaiaConfigEntry
    _scale: Incomplete
    def __init__(self, hass: HomeAssistant, entry: AcaiaConfigEntry) -> None: ...
    @property
    def scale(self) -> AcaiaScale: ...
    async def _async_update_data(self) -> None: ...
