from . import RoomID as RoomID
from .const import DOMAIN as DOMAIN, SERVICE_SEND_MESSAGE as SERVICE_SEND_MESSAGE
from _typeshed import Incomplete
from homeassistant.components.notify import ATTR_DATA as ATTR_DATA, ATTR_MESSAGE as ATTR_MESSAGE, ATTR_TARGET as ATTR_TARGET, BaseNotificationService as BaseNotificationService
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

CONF_DEFAULT_ROOM: str
PLATFORM_SCHEMA: Incomplete

def get_service(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = None) -> MatrixNotificationService: ...

class MatrixNotificationService(BaseNotificationService):
    _default_room: Incomplete
    def __init__(self, default_room: RoomID) -> None: ...
    def send_message(self, message: str = '', **kwargs: Any) -> None: ...
