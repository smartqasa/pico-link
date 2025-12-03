from .const import CONNECTION_ESTABLISHED_KEY as CONNECTION_ESTABLISHED_KEY, DOMAIN as DOMAIN, VALUE_UNAVAILABLE as VALUE_UNAVAILABLE
from _typeshed import Incomplete
from aiooncue import OncueDevice, OncueSensor as OncueSensor
from homeassistant.const import ATTR_CONNECTIONS as ATTR_CONNECTIONS
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator

class OncueEntity(CoordinatorEntity[DataUpdateCoordinator[dict[str, OncueDevice]]], Entity):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _device_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator[dict[str, OncueDevice]], device_id: str, device: OncueDevice, sensor: OncueSensor, description: EntityDescription) -> None: ...
    @property
    def _oncue_value(self) -> str: ...
    @property
    def available(self) -> bool: ...
