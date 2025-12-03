import pyevilgenius
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

UPDATE_INTERVAL: int

class EvilGeniusUpdateCoordinator(DataUpdateCoordinator[dict]):
    info: dict
    product: dict | None
    client: Incomplete
    def __init__(self, hass: HomeAssistant, name: str, client: pyevilgenius.EvilGeniusDevice) -> None: ...
    @property
    def device_name(self) -> str: ...
    @property
    def product_name(self) -> str | None: ...
    async def _async_update_data(self) -> dict: ...
