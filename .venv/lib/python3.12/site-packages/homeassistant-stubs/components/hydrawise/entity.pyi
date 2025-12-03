from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from .coordinator import HydrawiseDataUpdateCoordinator as HydrawiseDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pydrawise.schema import Controller as Controller, Sensor as Sensor, Zone as Zone

class HydrawiseEntity(CoordinatorEntity[HydrawiseDataUpdateCoordinator]):
    _attr_attribution: str
    _attr_has_entity_name: bool
    entity_description: Incomplete
    controller: Incomplete
    zone_id: Incomplete
    sensor_id: Incomplete
    _device_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: HydrawiseDataUpdateCoordinator, description: EntityDescription, controller: Controller, *, zone_id: int | None = None, sensor_id: int | None = None) -> None: ...
    @property
    def zone(self) -> Zone: ...
    @property
    def sensor(self) -> Sensor: ...
    def _update_attrs(self) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    @property
    def available(self) -> bool: ...
