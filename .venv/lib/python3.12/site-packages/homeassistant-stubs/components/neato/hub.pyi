from .const import NEATO_MAP_DATA as NEATO_MAP_DATA, NEATO_PERSISTENT_MAPS as NEATO_PERSISTENT_MAPS, NEATO_ROBOTS as NEATO_ROBOTS
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.util import Throttle as Throttle
from pybotvac import Account as Account
from urllib3.response import HTTPResponse

_LOGGER: Incomplete

class NeatoHub:
    _hass: Incomplete
    my_neato: Account
    def __init__(self, hass: HomeAssistant, neato: Account) -> None: ...
    def update_robots(self) -> None: ...
    def download_map(self, url: str) -> HTTPResponse: ...
    async def async_update_entry_unique_id(self, entry: ConfigEntry) -> str: ...
