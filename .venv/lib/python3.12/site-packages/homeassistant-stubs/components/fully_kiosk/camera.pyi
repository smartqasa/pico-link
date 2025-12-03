from . import FullyKioskConfigEntry as FullyKioskConfigEntry
from .coordinator import FullyKioskDataUpdateCoordinator as FullyKioskDataUpdateCoordinator
from .entity import FullyKioskEntity as FullyKioskEntity
from _typeshed import Incomplete
from homeassistant.components.camera import Camera as Camera, CameraEntityFeature as CameraEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: FullyKioskConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FullyCameraEntity(FullyKioskEntity, Camera):
    _attr_name: Incomplete
    _attr_supported_features: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FullyKioskDataUpdateCoordinator) -> None: ...
    async def async_camera_image(self, width: int | None = None, height: int | None = None) -> bytes | None: ...
    async def async_turn_on(self) -> None: ...
    async def async_turn_off(self) -> None: ...
    _attr_is_on: Incomplete
    @callback
    def _handle_coordinator_update(self) -> None: ...
