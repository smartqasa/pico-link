from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from .coordinator import SonarrDataT as SonarrDataT, SonarrDataUpdateCoordinator as SonarrDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class SonarrEntity(CoordinatorEntity[SonarrDataUpdateCoordinator[SonarrDataT]]):
    _attr_has_entity_name: bool
    coordinator: Incomplete
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: SonarrDataUpdateCoordinator[SonarrDataT], description: EntityDescription) -> None: ...
