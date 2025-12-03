from . import ATTR_BRIGHTNESS_PCT as ATTR_BRIGHTNESS_PCT, ATTR_COLOR_TEMP_KELVIN as ATTR_COLOR_TEMP_KELVIN, ATTR_RGB_COLOR as ATTR_RGB_COLOR
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.const import SERVICE_TURN_ON as SERVICE_TURN_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import intent as intent

_LOGGER: Incomplete
INTENT_SET: str

async def async_setup_intents(hass: HomeAssistant) -> None: ...
