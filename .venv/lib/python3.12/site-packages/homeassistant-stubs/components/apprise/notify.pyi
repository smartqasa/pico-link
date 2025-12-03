import apprise
from _typeshed import Incomplete
from homeassistant.components.notify import ATTR_TARGET as ATTR_TARGET, ATTR_TITLE as ATTR_TITLE, ATTR_TITLE_DEFAULT as ATTR_TITLE_DEFAULT, BaseNotificationService as BaseNotificationService
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Incomplete
CONF_FILE: str
PLATFORM_SCHEMA: Incomplete

def get_service(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = None) -> AppriseNotificationService | None: ...

class AppriseNotificationService(BaseNotificationService):
    apprise: Incomplete
    def __init__(self, a_obj: apprise.Apprise) -> None: ...
    def send_message(self, message: str = '', **kwargs: Any) -> None: ...
