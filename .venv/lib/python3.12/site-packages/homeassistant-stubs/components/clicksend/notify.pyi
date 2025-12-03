from _typeshed import Incomplete
from homeassistant.components.notify import BaseNotificationService as BaseNotificationService
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_RECIPIENT as CONF_RECIPIENT, CONF_SENDER as CONF_SENDER, CONF_USERNAME as CONF_USERNAME, CONTENT_TYPE_JSON as CONTENT_TYPE_JSON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Incomplete
BASE_API_URL: str
DEFAULT_SENDER: str
TIMEOUT: int
HEADERS: Incomplete
PLATFORM_SCHEMA: Incomplete

def get_service(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = None) -> ClicksendNotificationService | None: ...

class ClicksendNotificationService(BaseNotificationService):
    username: str
    api_key: str
    recipients: list[str]
    sender: str
    def __init__(self, config: ConfigType) -> None: ...
    def send_message(self, message: str = '', **kwargs: Any) -> None: ...

def _authenticate(config: ConfigType) -> bool: ...
