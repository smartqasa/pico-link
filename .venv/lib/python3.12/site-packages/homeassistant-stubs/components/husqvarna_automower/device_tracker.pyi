from . import AutomowerConfigEntry as AutomowerConfigEntry
from .coordinator import AutomowerDataUpdateCoordinator as AutomowerDataUpdateCoordinator
from .entity import AutomowerBaseEntity as AutomowerBaseEntity
from _typeshed import Incomplete
from homeassistant.components.device_tracker import TrackerEntity as TrackerEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: AutomowerConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AutomowerDeviceTrackerEntity(AutomowerBaseEntity, TrackerEntity):
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, mower_id: str, coordinator: AutomowerDataUpdateCoordinator) -> None: ...
    @property
    def latitude(self) -> float: ...
    @property
    def longitude(self) -> float: ...
