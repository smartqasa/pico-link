from .api import AuthenticatedMonzoAPI as AuthenticatedMonzoAPI
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

_LOGGER: Incomplete

@dataclass
class MonzoData:
    accounts: list[dict[str, Any]]
    pots: list[dict[str, Any]]

class MonzoCoordinator(DataUpdateCoordinator[MonzoData]):
    api: Incomplete
    def __init__(self, hass: HomeAssistant, api: AuthenticatedMonzoAPI) -> None: ...
    async def _async_update_data(self) -> MonzoData: ...
