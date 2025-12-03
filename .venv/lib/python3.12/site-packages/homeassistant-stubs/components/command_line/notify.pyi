from .const import CONF_COMMAND_TIMEOUT as CONF_COMMAND_TIMEOUT
from _typeshed import Incomplete
from homeassistant.components.notify import BaseNotificationService as BaseNotificationService
from homeassistant.const import CONF_COMMAND as CONF_COMMAND
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util.process import kill_subprocess as kill_subprocess
from typing import Any

_LOGGER: Incomplete

def get_service(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = None) -> CommandLineNotificationService | None: ...

class CommandLineNotificationService(BaseNotificationService):
    command: Incomplete
    _timeout: Incomplete
    def __init__(self, command: str, timeout: int) -> None: ...
    def send_message(self, message: str = '', **kwargs: Any) -> None: ...
