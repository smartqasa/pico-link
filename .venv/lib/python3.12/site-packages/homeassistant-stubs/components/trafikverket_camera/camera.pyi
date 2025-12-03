from . import TVCameraConfigEntry as TVCameraConfigEntry
from .const import ATTR_DESCRIPTION as ATTR_DESCRIPTION, ATTR_TYPE as ATTR_TYPE
from .coordinator import TVDataUpdateCoordinator as TVDataUpdateCoordinator
from .entity import TrafikverketCameraEntity as TrafikverketCameraEntity
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components.camera import Camera as Camera
from homeassistant.const import ATTR_LOCATION as ATTR_LOCATION
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: TVCameraConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TVCamera(TrafikverketCameraEntity, Camera):
    _unrecorded_attributes: Incomplete
    _attr_name: Incomplete
    _attr_translation_key: str
    coordinator: TVDataUpdateCoordinator
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: TVDataUpdateCoordinator, entry_id: str) -> None: ...
    async def async_camera_image(self, width: int | None = None, height: int | None = None) -> bytes | None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any] | None: ...
