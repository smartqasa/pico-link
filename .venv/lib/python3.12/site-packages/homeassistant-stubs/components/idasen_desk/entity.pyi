from . import IdasenDeskCoordinator as IdasenDeskCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class IdasenDeskEntity(CoordinatorEntity[IdasenDeskCoordinator]):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _desk: Incomplete
    def __init__(self, unique_id: str, coordinator: IdasenDeskCoordinator) -> None: ...
    @property
    def available(self) -> bool: ...
