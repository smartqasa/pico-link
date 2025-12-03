from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from .coordinator import LockData as LockData, SchlageDataUpdateCoordinator as SchlageDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pyschlage.lock import Lock as Lock

class SchlageEntity(CoordinatorEntity[SchlageDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    device_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: SchlageDataUpdateCoordinator, device_id: str) -> None: ...
    @property
    def _lock_data(self) -> LockData: ...
    @property
    def _lock(self) -> Lock: ...
    @property
    def available(self) -> bool: ...
