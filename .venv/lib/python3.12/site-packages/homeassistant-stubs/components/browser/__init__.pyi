from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.helpers.typing import ConfigType as ConfigType

ATTR_URL: str
ATTR_URL_DEFAULT: str
DOMAIN: str
SERVICE_BROWSE_URL: str
SERVICE_BROWSE_URL_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete

def _browser_url(service: ServiceCall) -> None: ...
def setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
