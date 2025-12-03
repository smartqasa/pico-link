from .const import DOMAIN as DOMAIN
from .coordinator import OverkizDataUpdateCoordinator as OverkizDataUpdateCoordinator
from .executor import OverkizExecutor as OverkizExecutor
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pyoverkiz.models import Device as Device

class OverkizEntity(CoordinatorEntity[OverkizDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_name: str | None
    device_url: Incomplete
    base_device_url: Incomplete
    index_device_url: Incomplete
    executor: Incomplete
    _attr_assumed_state: Incomplete
    _attr_available: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, device_url: str, coordinator: OverkizDataUpdateCoordinator) -> None: ...
    @property
    def is_sub_device(self) -> bool: ...
    @property
    def device(self) -> Device: ...
    def generate_device_info(self) -> DeviceInfo: ...

class OverkizDescriptiveEntity(OverkizEntity):
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    def __init__(self, device_url: str, coordinator: OverkizDataUpdateCoordinator, description: EntityDescription) -> None: ...
