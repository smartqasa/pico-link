from . import BMWConfigEntry as BMWConfigEntry
from .const import ATTR_DIRECTION as ATTR_DIRECTION
from .coordinator import BMWDataUpdateCoordinator as BMWDataUpdateCoordinator
from .entity import BMWBaseEntity as BMWBaseEntity
from _typeshed import Incomplete
from bimmer_connected.vehicle import MyBMWVehicle as MyBMWVehicle
from homeassistant.components.device_tracker import TrackerEntity as TrackerEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: BMWConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BMWDeviceTracker(BMWBaseEntity, TrackerEntity):
    _attr_force_update: bool
    _attr_translation_key: str
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: BMWDataUpdateCoordinator, vehicle: MyBMWVehicle) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def latitude(self) -> float | None: ...
    @property
    def longitude(self) -> float | None: ...
