from .const import CONF_LANGUAGE_CODE as CONF_LANGUAGE_CODE, DOMAIN as DOMAIN
from .helpers import async_send_text_commands as async_send_text_commands, default_language_code as default_language_code
from _typeshed import Incomplete
from homeassistant.components.notify import ATTR_TARGET as ATTR_TARGET, BaseNotificationService as BaseNotificationService
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

LANG_TO_BROADCAST_COMMAND: Incomplete

def broadcast_commands(language_code: str) -> tuple[str, str]: ...
async def async_get_service(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = None) -> BaseNotificationService: ...

class BroadcastNotificationService(BaseNotificationService):
    hass: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_send_message(self, message: str = '', **kwargs: Any) -> None: ...
