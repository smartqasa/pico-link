from .const import DOMAIN as DOMAIN
from .coordinator import BMWDataUpdateCoordinator as BMWDataUpdateCoordinator
from _typeshed import Incomplete
from bimmer_connected.vehicle import MyBMWVehicle as MyBMWVehicle
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class BMWBaseEntity(CoordinatorEntity[BMWDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    vehicle: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: BMWDataUpdateCoordinator, vehicle: MyBMWVehicle) -> None: ...
    async def async_added_to_hass(self) -> None: ...
