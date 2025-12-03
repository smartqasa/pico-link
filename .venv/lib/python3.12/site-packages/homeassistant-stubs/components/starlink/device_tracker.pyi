from .const import ATTR_ALTITUDE as ATTR_ALTITUDE, DOMAIN as DOMAIN
from .coordinator import StarlinkData as StarlinkData
from .entity import StarlinkEntity as StarlinkEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.device_tracker import TrackerEntity as TrackerEntity, TrackerEntityDescription as TrackerEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

@dataclass(frozen=True, kw_only=True)
class StarlinkDeviceTrackerEntityDescription(TrackerEntityDescription):
    latitude_fn: Callable[[StarlinkData], float]
    longitude_fn: Callable[[StarlinkData], float]
    altitude_fn: Callable[[StarlinkData], float]

DEVICE_TRACKERS: Incomplete

class StarlinkDeviceTrackerEntity(StarlinkEntity, TrackerEntity):
    entity_description: StarlinkDeviceTrackerEntityDescription
    @property
    def latitude(self) -> float | None: ...
    @property
    def longitude(self) -> float | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
