from .api import PushBulletNotificationProvider as PushBulletNotificationProvider
from .const import ATTR_FILE as ATTR_FILE, ATTR_FILE_URL as ATTR_FILE_URL, ATTR_URL as ATTR_URL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.notify import ATTR_DATA as ATTR_DATA, ATTR_TARGET as ATTR_TARGET, ATTR_TITLE as ATTR_TITLE, ATTR_TITLE_DEFAULT as ATTR_TITLE_DEFAULT, BaseNotificationService as BaseNotificationService
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from pushbullet import PushBullet as PushBullet
from pushbullet.channel import Channel as Channel
from pushbullet.device import Device as Device
from typing import Any

_LOGGER: Incomplete

async def async_get_service(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = None) -> PushBulletNotificationService | None: ...

class PushBulletNotificationService(BaseNotificationService):
    hass: Incomplete
    pushbullet: Incomplete
    def __init__(self, hass: HomeAssistant, pushbullet: PushBullet) -> None: ...
    @property
    def pbtargets(self) -> dict[str, dict[str, Device | Channel]]: ...
    def send_message(self, message: str, **kwargs: Any) -> None: ...
    def _push_data(self, message: str, title: str, data: dict[str, Any], pusher: PushBullet, email: str | None = None, phonenumber: str | None = None) -> None: ...
