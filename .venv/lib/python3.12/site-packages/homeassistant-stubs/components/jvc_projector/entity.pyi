from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, NAME as NAME
from .coordinator import JvcProjectorDataUpdateCoordinator as JvcProjectorDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from jvcprojector import JvcProjector as JvcProjector

_LOGGER: Incomplete

class JvcProjectorEntity(CoordinatorEntity[JvcProjectorDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: JvcProjectorDataUpdateCoordinator) -> None: ...
    @property
    def device(self) -> JvcProjector: ...
