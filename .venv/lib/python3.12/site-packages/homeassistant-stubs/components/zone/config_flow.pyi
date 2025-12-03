from .const import DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigFlow as ConfigFlow

class ZoneConfigFlow(ConfigFlow, domain=DOMAIN): ...
