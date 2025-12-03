from .const import ATTR_COLOR as ATTR_COLOR, ATTR_DURATION as ATTR_DURATION, ATTR_FONTSIZE as ATTR_FONTSIZE, ATTR_ICON as ATTR_ICON, ATTR_ICON_AUTH as ATTR_ICON_AUTH, ATTR_ICON_AUTH_DIGEST as ATTR_ICON_AUTH_DIGEST, ATTR_ICON_PASSWORD as ATTR_ICON_PASSWORD, ATTR_ICON_PATH as ATTR_ICON_PATH, ATTR_ICON_URL as ATTR_ICON_URL, ATTR_ICON_USERNAME as ATTR_ICON_USERNAME, ATTR_IMAGE as ATTR_IMAGE, ATTR_IMAGE_AUTH as ATTR_IMAGE_AUTH, ATTR_IMAGE_AUTH_DIGEST as ATTR_IMAGE_AUTH_DIGEST, ATTR_IMAGE_PASSWORD as ATTR_IMAGE_PASSWORD, ATTR_IMAGE_PATH as ATTR_IMAGE_PATH, ATTR_IMAGE_URL as ATTR_IMAGE_URL, ATTR_IMAGE_USERNAME as ATTR_IMAGE_USERNAME, ATTR_INTERRUPT as ATTR_INTERRUPT, ATTR_POSITION as ATTR_POSITION, ATTR_TRANSPARENCY as ATTR_TRANSPARENCY, DEFAULT_TIMEOUT as DEFAULT_TIMEOUT, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.notify import ATTR_DATA as ATTR_DATA, ATTR_TITLE as ATTR_TITLE, ATTR_TITLE_DEFAULT as ATTR_TITLE_DEFAULT, BaseNotificationService as BaseNotificationService
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from io import BufferedReader
from notifications_android_tv import Notifications
from typing import Any

_LOGGER: Incomplete

async def async_get_service(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = None) -> NFAndroidTVNotificationService | None: ...

class NFAndroidTVNotificationService(BaseNotificationService):
    notify: Incomplete
    is_allowed_path: Incomplete
    def __init__(self, notify: Notifications, is_allowed_path: Any) -> None: ...
    def send_message(self, message: str, **kwargs: Any) -> None: ...
    def load_file(self, url: str | None = None, local_path: str | None = None, username: str | None = None, password: str | None = None, auth: str | None = None) -> BufferedReader | bytes | None: ...
