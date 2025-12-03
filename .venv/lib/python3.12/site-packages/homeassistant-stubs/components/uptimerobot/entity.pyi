from . import UptimeRobotDataUpdateCoordinator as UptimeRobotDataUpdateCoordinator
from .const import ATTRIBUTION as ATTRIBUTION, ATTR_TARGET as ATTR_TARGET, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pyuptimerobot import UptimeRobotMonitor as UptimeRobotMonitor

class UptimeRobotEntity(CoordinatorEntity[UptimeRobotDataUpdateCoordinator]):
    _attr_attribution = ATTRIBUTION
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    entity_description: Incomplete
    _monitor: Incomplete
    _attr_device_info: Incomplete
    _attr_extra_state_attributes: Incomplete
    _attr_unique_id: Incomplete
    api: Incomplete
    def __init__(self, coordinator: UptimeRobotDataUpdateCoordinator, description: EntityDescription, monitor: UptimeRobotMonitor) -> None: ...
    @property
    def _monitors(self) -> list[UptimeRobotMonitor]: ...
    @property
    def monitor(self) -> UptimeRobotMonitor: ...
    @property
    def monitor_available(self) -> bool: ...
