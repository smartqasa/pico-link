from . import device_name_for_push_id as device_name_for_push_id, devices_with_push as devices_with_push, enabled_push_ids as enabled_push_ids
from _typeshed import Incomplete
from homeassistant.components.notify import ATTR_DATA as ATTR_DATA, ATTR_MESSAGE as ATTR_MESSAGE, ATTR_TARGET as ATTR_TARGET, ATTR_TITLE as ATTR_TITLE, ATTR_TITLE_DEFAULT as ATTR_TITLE_DEFAULT, BaseNotificationService as BaseNotificationService
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Incomplete
PUSH_URL: str

def log_rate_limits(hass: HomeAssistant, target: str, resp: dict[str, Any], level: int = 20) -> None: ...
def get_service(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = None) -> iOSNotificationService | None: ...

class iOSNotificationService(BaseNotificationService):
    def __init__(self) -> None: ...
    @property
    def targets(self) -> dict[str, str]: ...
    def send_message(self, message: str = '', **kwargs: Any) -> None: ...
