from . import RenaultConfigEntry as RenaultConfigEntry
from .entity import RenaultDataEntity as RenaultDataEntity, RenaultDataEntityDescription as RenaultDataEntityDescription
from dataclasses import dataclass
from homeassistant.components.device_tracker import TrackerEntity as TrackerEntity, TrackerEntityDescription as TrackerEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from renault_api.kamereon.models import KamereonVehicleLocationData

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class RenaultTrackerEntityDescription(TrackerEntityDescription, RenaultDataEntityDescription): ...

async def async_setup_entry(hass: HomeAssistant, config_entry: RenaultConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RenaultDeviceTracker(RenaultDataEntity[KamereonVehicleLocationData], TrackerEntity):
    entity_description: RenaultTrackerEntityDescription
    @property
    def latitude(self) -> float | None: ...
    @property
    def longitude(self) -> float | None: ...

DEVICE_TRACKER_TYPES: tuple[RenaultTrackerEntityDescription, ...]
