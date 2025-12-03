from .const import DOMAIN as DOMAIN
from .coordinator import RoborockDataUpdateCoordinator as RoborockDataUpdateCoordinator, RoborockDataUpdateCoordinatorA01 as RoborockDataUpdateCoordinatorA01
from _typeshed import Incomplete
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from roborock.api import RoborockClient as RoborockClient
from roborock.command_cache import CacheableAttribute as CacheableAttribute
from roborock.containers import Consumable as Consumable, Status
from roborock.roborock_message import RoborockDataProtocol
from roborock.roborock_typing import RoborockCommand
from roborock.version_1_apis.roborock_client_v1 import AttributeCache as AttributeCache, RoborockClientV1 as RoborockClientV1
from roborock.version_1_apis.roborock_mqtt_client_v1 import RoborockMqttClientV1 as RoborockMqttClientV1
from roborock.version_a01_apis import RoborockClientA01 as RoborockClientA01
from typing import Any

class RoborockEntity(Entity):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _api: Incomplete
    def __init__(self, unique_id: str, device_info: DeviceInfo, api: RoborockClient) -> None: ...

class RoborockEntityV1(RoborockEntity):
    _api: RoborockClientV1
    def __init__(self, unique_id: str, device_info: DeviceInfo, api: RoborockClientV1) -> None: ...
    def get_cache(self, attribute: CacheableAttribute) -> AttributeCache: ...
    async def send(self, command: RoborockCommand | str, params: dict[str, Any] | list[Any] | int | None = None) -> dict: ...
    @property
    def api(self) -> RoborockClientV1: ...

class RoborockEntityA01(RoborockEntity):
    _api: RoborockClientA01
    def __init__(self, unique_id: str, device_info: DeviceInfo, api: RoborockClientA01) -> None: ...

class RoborockCoordinatedEntityV1(RoborockEntityV1, CoordinatorEntity[RoborockDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    listener_requests: Incomplete
    def __init__(self, unique_id: str, coordinator: RoborockDataUpdateCoordinator, listener_request: list[RoborockDataProtocol] | RoborockDataProtocol | None = None) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    @property
    def _device_status(self) -> Status: ...
    @property
    def cloud_api(self) -> RoborockMqttClientV1: ...
    async def send(self, command: RoborockCommand | str, params: dict[str, Any] | list[Any] | int | None = None) -> dict: ...
    def _update_from_listener(self, value: Status | Consumable) -> None: ...

class RoborockCoordinatedEntityA01(RoborockEntityA01, CoordinatorEntity[RoborockDataUpdateCoordinatorA01]):
    _attr_unique_id: Incomplete
    def __init__(self, unique_id: str, coordinator: RoborockDataUpdateCoordinatorA01) -> None: ...
