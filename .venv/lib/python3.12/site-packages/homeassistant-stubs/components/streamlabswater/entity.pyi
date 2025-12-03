from .coordinator import StreamlabsCoordinator as StreamlabsCoordinator, StreamlabsData as StreamlabsData
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class StreamlabsWaterEntity(CoordinatorEntity[StreamlabsCoordinator]):
    _attr_has_entity_name: bool
    _location_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: StreamlabsCoordinator, location_id: str, key: str) -> None: ...
    @property
    def location_data(self) -> StreamlabsData: ...
