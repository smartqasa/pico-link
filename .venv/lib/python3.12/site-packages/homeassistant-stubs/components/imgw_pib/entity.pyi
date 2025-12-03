from .const import ATTRIBUTION as ATTRIBUTION
from .coordinator import ImgwPibDataUpdateCoordinator as ImgwPibDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class ImgwPibEntity(CoordinatorEntity[ImgwPibDataUpdateCoordinator]):
    _attr_attribution = ATTRIBUTION
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: ImgwPibDataUpdateCoordinator) -> None: ...
