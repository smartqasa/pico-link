from .const import LEASES_REGEX as LEASES_REGEX
from .model import Device as Device
from _typeshed import Incomplete
from homeassistant.components.device_tracker import DeviceScanner as DeviceScanner
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Final

_LOGGER: Final[Incomplete]
PLATFORM_SCHEMA: Final[Incomplete]

def get_scanner(hass: HomeAssistant, config: ConfigType) -> ActiontecDeviceScanner | None: ...

class ActiontecDeviceScanner(DeviceScanner):
    host: str
    username: str
    password: str
    last_results: list[Device]
    success_init: Incomplete
    def __init__(self, config: ConfigType) -> None: ...
    def scan_devices(self) -> list[str]: ...
    def get_device_name(self, device: str) -> str | None: ...
    def _update_info(self) -> bool: ...
    def get_actiontec_data(self) -> list[Device] | None: ...
