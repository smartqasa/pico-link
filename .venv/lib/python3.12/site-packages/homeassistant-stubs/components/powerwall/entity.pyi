from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, MODEL as MODEL, POWERWALL_API as POWERWALL_API, POWERWALL_BASE_INFO as POWERWALL_BASE_INFO, POWERWALL_COORDINATOR as POWERWALL_COORDINATOR
from .models import BatteryResponse as BatteryResponse, PowerwallData as PowerwallData, PowerwallRuntimeData as PowerwallRuntimeData
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator

class PowerWallEntity(CoordinatorEntity[DataUpdateCoordinator[PowerwallData]]):
    _attr_has_entity_name: bool
    power_wall: Incomplete
    base_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, powerwall_data: PowerwallRuntimeData) -> None: ...
    @property
    def data(self) -> PowerwallData: ...

class BatteryEntity(CoordinatorEntity[DataUpdateCoordinator[PowerwallData]]):
    _attr_has_entity_name: bool
    serial_number: Incomplete
    power_wall: Incomplete
    base_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, powerwall_data: PowerwallRuntimeData, battery: BatteryResponse) -> None: ...
    @property
    def battery_data(self) -> BatteryResponse: ...
