from .const import DOMAIN as DOMAIN, NAME as NAME
from homeassistant.components import zeroconf as zeroconf
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import config_entry_flow as config_entry_flow

async def _async_has_devices(hass: HomeAssistant) -> bool: ...
