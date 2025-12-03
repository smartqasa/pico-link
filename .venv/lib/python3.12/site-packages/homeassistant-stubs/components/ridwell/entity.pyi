from .const import DOMAIN as DOMAIN
from .coordinator import RidwellDataUpdateCoordinator as RidwellDataUpdateCoordinator
from _typeshed import Incomplete
from aioridwell.model import RidwellAccount as RidwellAccount, RidwellPickupEvent as RidwellPickupEvent
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class RidwellEntity(CoordinatorEntity[RidwellDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _account: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: RidwellDataUpdateCoordinator, account: RidwellAccount) -> None: ...
    @property
    def next_pickup_event(self) -> RidwellPickupEvent: ...
