from .const import DOMAIN as DOMAIN
from .coordinator import SolarLogCoordinator as SolarLogCoordinator
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorEntityDescription as SensorEntityDescription
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from homeassistant.util import slugify as slugify

class SolarLogBaseEntity(CoordinatorEntity[SolarLogCoordinator]):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    def __init__(self, coordinator: SolarLogCoordinator, description: SensorEntityDescription) -> None: ...

class SolarLogCoordinatorEntity(SolarLogBaseEntity):
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: SolarLogCoordinator, description: SensorEntityDescription) -> None: ...

class SolarLogInverterEntity(SolarLogBaseEntity):
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    device_id: Incomplete
    def __init__(self, coordinator: SolarLogCoordinator, description: SensorEntityDescription, device_id: int) -> None: ...
