from .const import LOGGER as LOGGER
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from streamlabswater.streamlabswater import StreamlabsClient as StreamlabsClient

@dataclass(slots=True)
class StreamlabsData:
    is_away: bool
    name: str
    daily_usage: float
    monthly_usage: float
    yearly_usage: float

class StreamlabsCoordinator(DataUpdateCoordinator[dict[str, StreamlabsData]]):
    client: Incomplete
    def __init__(self, hass: HomeAssistant, client: StreamlabsClient) -> None: ...
    async def _async_update_data(self) -> dict[str, StreamlabsData]: ...
    def _update_data(self) -> dict[str, StreamlabsData]: ...
