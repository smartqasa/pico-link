from . import DevoloHomeNetworkConfigEntry as DevoloHomeNetworkConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import DevoloDataUpdateCoordinator as DevoloDataUpdateCoordinator
from _typeshed import Incomplete
from devolo_plc_api.device_api import ConnectedStationInfo, NeighborAPInfo, WifiGuestAccessGet
from devolo_plc_api.plcnet_api import DataRate, LogicalNetwork
from homeassistant.const import ATTR_CONNECTIONS as ATTR_CONNECTIONS
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

type _DataType = LogicalNetwork | DataRate | list[ConnectedStationInfo] | list[NeighborAPInfo] | WifiGuestAccessGet | bool | int
class DevoloEntity(Entity):
    _attr_has_entity_name: bool
    device: Incomplete
    entry: Incomplete
    _attr_device_info: Incomplete
    _attr_translation_key: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, entry: DevoloHomeNetworkConfigEntry) -> None: ...

class DevoloCoordinatorEntity[_DataT: _DataType](CoordinatorEntity[DevoloDataUpdateCoordinator[_DataT]], DevoloEntity):
    def __init__(self, entry: DevoloHomeNetworkConfigEntry, coordinator: DevoloDataUpdateCoordinator[_DataT]) -> None: ...
