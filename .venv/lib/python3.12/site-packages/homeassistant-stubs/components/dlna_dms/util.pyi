from .const import CONF_SOURCE_ID as CONF_SOURCE_ID, DOMAIN as DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.util import slugify as slugify

def generate_source_id(hass: HomeAssistant, name: str) -> str: ...
