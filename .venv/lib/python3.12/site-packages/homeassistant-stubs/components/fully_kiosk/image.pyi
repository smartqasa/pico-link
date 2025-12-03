from . import FullyKioskConfigEntry as FullyKioskConfigEntry
from .coordinator import FullyKioskDataUpdateCoordinator as FullyKioskDataUpdateCoordinator
from .entity import FullyKioskEntity as FullyKioskEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from fullykiosk import FullyKiosk as FullyKiosk
from homeassistant.components.image import ImageEntity as ImageEntity, ImageEntityDescription as ImageEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

@dataclass(frozen=True, kw_only=True)
class FullyImageEntityDescription(ImageEntityDescription):
    image_fn: Callable[[FullyKiosk], Coroutine[Any, Any, bytes]]

IMAGES: tuple[FullyImageEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: FullyKioskConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FullyImageEntity(FullyKioskEntity, ImageEntity):
    entity_description: FullyImageEntityDescription
    _attr_content_type: str
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FullyKioskDataUpdateCoordinator, description: FullyImageEntityDescription) -> None: ...
    _attr_image_last_updated: Incomplete
    async def async_image(self) -> bytes | None: ...
