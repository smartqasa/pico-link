from . import DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigFlow as ConfigFlow

class AladdinConnectConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
