from .const import DOMAIN as DOMAIN
from .models import RoborockA01HassDeviceInfo as RoborockA01HassDeviceInfo, RoborockHassDeviceInfo as RoborockHassDeviceInfo, RoborockMapInfo as RoborockMapInfo
from _typeshed import Incomplete
from homeassistant.const import ATTR_CONNECTIONS as ATTR_CONNECTIONS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util import slugify as slugify
from propcache import cached_property
from roborock import HomeDataRoom as HomeDataRoom
from roborock.containers import HomeDataDevice as HomeDataDevice, HomeDataProduct as HomeDataProduct, NetworkInfo as NetworkInfo
from roborock.roborock_message import RoborockDyadDataProtocol, RoborockZeoProtocol
from roborock.roborock_typing import DeviceProp
from roborock.version_1_apis.roborock_local_client_v1 import RoborockLocalClientV1
from roborock.version_1_apis.roborock_mqtt_client_v1 import RoborockMqttClientV1 as RoborockMqttClientV1
from roborock.version_a01_apis import RoborockClientA01 as RoborockClientA01

SCAN_INTERVAL: Incomplete
_LOGGER: Incomplete

class RoborockDataUpdateCoordinator(DataUpdateCoordinator[DeviceProp]):
    roborock_device_info: Incomplete
    api: RoborockLocalClientV1 | RoborockMqttClientV1
    cloud_api: Incomplete
    device_info: Incomplete
    current_map: int | None
    maps: dict[int, RoborockMapInfo]
    _home_data_rooms: Incomplete
    def __init__(self, hass: HomeAssistant, device: HomeDataDevice, device_networking: NetworkInfo, product_info: HomeDataProduct, cloud_api: RoborockMqttClientV1, home_data_rooms: list[HomeDataRoom]) -> None: ...
    async def verify_api(self) -> None: ...
    async def release(self) -> None: ...
    async def _update_device_prop(self) -> None: ...
    async def _async_update_data(self) -> DeviceProp: ...
    def _set_current_map(self) -> None: ...
    async def get_maps(self) -> None: ...
    async def get_rooms(self) -> None: ...
    @cached_property
    def duid(self) -> str: ...
    @cached_property
    def duid_slug(self) -> str: ...

class RoborockDataUpdateCoordinatorA01(DataUpdateCoordinator[dict[RoborockDyadDataProtocol | RoborockZeoProtocol, StateType]]):
    api: Incomplete
    device_info: Incomplete
    request_protocols: list[RoborockDyadDataProtocol | RoborockZeoProtocol]
    roborock_device_info: Incomplete
    def __init__(self, hass: HomeAssistant, device: HomeDataDevice, product_info: HomeDataProduct, api: RoborockClientA01) -> None: ...
    async def _async_update_data(self) -> dict[RoborockDyadDataProtocol | RoborockZeoProtocol, StateType]: ...
    async def release(self) -> None: ...
    @cached_property
    def duid(self) -> str: ...
    @cached_property
    def duid_slug(self) -> str: ...
