import dataclasses
from .const import DOMAIN as DOMAIN, REQUEST_TIMEOUT as REQUEST_TIMEOUT, UPDATE_INTERVAL as UPDATE_INTERVAL
from _typeshed import Incomplete
from homeassistant.components.hassio import get_supervisor_info as get_supervisor_info
from homeassistant.const import __version__ as __version__
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.hassio import is_hassio as is_hassio
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

_LOGGER: Incomplete

@dataclasses.dataclass(slots=True, frozen=True)
class IntegrationAlert:
    alert_id: str
    integration: str
    filename: str
    date_updated: str | None
    @property
    def issue_id(self) -> str: ...

class AlertUpdateCoordinator(DataUpdateCoordinator[dict[str, IntegrationAlert]]):
    ha_version: Incomplete
    supervisor: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def _async_update_data(self) -> dict[str, IntegrationAlert]: ...
