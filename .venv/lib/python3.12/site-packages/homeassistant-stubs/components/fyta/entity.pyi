from . import FytaConfigEntry as FytaConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import FytaCoordinator as FytaCoordinator
from _typeshed import Incomplete
from fyta_cli.fyta_models import Plant as Plant
from homeassistant.components.sensor import SensorEntityDescription as SensorEntityDescription
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class FytaPlantEntity(CoordinatorEntity[FytaCoordinator]):
    _attr_has_entity_name: bool
    plant_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: FytaCoordinator, entry: FytaConfigEntry, description: SensorEntityDescription, plant_id: int) -> None: ...
    @property
    def plant(self) -> Plant: ...
    @property
    def available(self) -> bool: ...
