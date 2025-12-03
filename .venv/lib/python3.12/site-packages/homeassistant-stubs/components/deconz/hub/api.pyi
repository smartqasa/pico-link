from ..const import LOGGER as LOGGER
from ..errors import AuthenticationRequired as AuthenticationRequired, CannotConnect as CannotConnect
from .config import DeconzConfig as DeconzConfig
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import aiohttp_client as aiohttp_client
from pydeconz import DeconzSession

async def get_deconz_api(hass: HomeAssistant, config_entry: ConfigEntry) -> DeconzSession: ...
