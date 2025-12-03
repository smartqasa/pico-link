from . import websocket_api as websocket_api
from .const import DOMAIN as DOMAIN
from .data import async_get_manager as async_get_manager
from _typeshed import Incomplete
from homeassistant.components import frontend as frontend
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import discovery as discovery
from homeassistant.helpers.typing import ConfigType as ConfigType

CONFIG_SCHEMA: Incomplete

async def is_configured(hass: HomeAssistant) -> bool: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
