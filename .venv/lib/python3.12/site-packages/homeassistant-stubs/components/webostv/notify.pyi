from .const import ATTR_CONFIG_ENTRY_ID as ATTR_CONFIG_ENTRY_ID, DATA_CONFIG_ENTRY as DATA_CONFIG_ENTRY, DOMAIN as DOMAIN, WEBOSTV_EXCEPTIONS as WEBOSTV_EXCEPTIONS
from _typeshed import Incomplete
from aiowebostv import WebOsClient as WebOsClient
from homeassistant.components.notify import ATTR_DATA as ATTR_DATA, BaseNotificationService as BaseNotificationService
from homeassistant.const import ATTR_ICON as ATTR_ICON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Incomplete

async def async_get_service(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = None) -> BaseNotificationService | None: ...

class LgWebOSNotificationService(BaseNotificationService):
    _client: Incomplete
    def __init__(self, client: WebOsClient) -> None: ...
    async def async_send_message(self, message: str = '', **kwargs: Any) -> None: ...
