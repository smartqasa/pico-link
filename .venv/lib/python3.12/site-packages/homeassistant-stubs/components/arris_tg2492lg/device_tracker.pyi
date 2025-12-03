from _typeshed import Incomplete
from arris_tg2492lg import ConnectBox, Device as Device
from homeassistant.components.device_tracker import DeviceScanner as DeviceScanner
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.typing import ConfigType as ConfigType

DEFAULT_HOST: str
PLATFORM_SCHEMA: Incomplete

async def async_get_scanner(hass: HomeAssistant, config: ConfigType) -> ArrisDeviceScanner | None: ...

class ArrisDeviceScanner(DeviceScanner):
    connect_box: Incomplete
    last_results: list[Device]
    def __init__(self, connect_box: ConnectBox) -> None: ...
    async def async_scan_devices(self) -> list[str]: ...
    async def async_get_device_name(self, device: str) -> str | None: ...
    async def _async_update_info(self) -> None: ...
