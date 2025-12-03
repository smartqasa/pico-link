from .const import ATTR_ATTACHMENTS as ATTR_ATTACHMENTS, ATTR_EVENT as ATTR_EVENT, CONF_DEVICE_KEY as CONF_DEVICE_KEY, CONF_SALT as CONF_SALT
from _typeshed import Incomplete
from homeassistant.components.notify import ATTR_DATA as ATTR_DATA, ATTR_TITLE as ATTR_TITLE, ATTR_TITLE_DEFAULT as ATTR_TITLE_DEFAULT, BaseNotificationService as BaseNotificationService
from homeassistant.const import CONF_EVENT as CONF_EVENT, CONF_PASSWORD as CONF_PASSWORD
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Incomplete

async def async_get_service(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = None) -> SimplePushNotificationService | None: ...

class SimplePushNotificationService(BaseNotificationService):
    _device_key: str
    _event: str | None
    _password: str | None
    _salt: str | None
    def __init__(self, config: dict[str, Any]) -> None: ...
    def send_message(self, message: str, **kwargs: Any) -> None: ...
