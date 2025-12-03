from _typeshed import Incomplete
from homeassistant.components.notify import BaseNotificationService as BaseNotificationService
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_RECIPIENT as CONF_RECIPIENT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Incomplete
DEFAULT_NAME: str
BASE_API_URL: str
PLATFORM_SCHEMA: Incomplete

def get_service(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = None) -> ClickatellNotificationService: ...

class ClickatellNotificationService(BaseNotificationService):
    api_key: str
    recipient: str
    def __init__(self, config: ConfigType) -> None: ...
    def send_message(self, message: str = '', **kwargs: Any) -> None: ...
