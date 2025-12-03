from . import CoverDeviceClass as CoverDeviceClass, DOMAIN as DOMAIN, INTENT_CLOSE_COVER as INTENT_CLOSE_COVER, INTENT_OPEN_COVER as INTENT_OPEN_COVER
from homeassistant.const import SERVICE_CLOSE_COVER as SERVICE_CLOSE_COVER, SERVICE_OPEN_COVER as SERVICE_OPEN_COVER
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import intent as intent

async def async_setup_intents(hass: HomeAssistant) -> None: ...
