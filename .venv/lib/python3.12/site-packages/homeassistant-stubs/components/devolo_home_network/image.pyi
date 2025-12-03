from . import DevoloHomeNetworkConfigEntry as DevoloHomeNetworkConfigEntry
from .const import IMAGE_GUEST_WIFI as IMAGE_GUEST_WIFI, SWITCH_GUEST_WIFI as SWITCH_GUEST_WIFI
from .coordinator import DevoloDataUpdateCoordinator as DevoloDataUpdateCoordinator
from .entity import DevoloCoordinatorEntity as DevoloCoordinatorEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from devolo_plc_api.device_api import WifiGuestAccessGet
from homeassistant.components.image import ImageEntity as ImageEntity, ImageEntityDescription as ImageEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class DevoloImageEntityDescription(ImageEntityDescription):
    image_func: Callable[[WifiGuestAccessGet], bytes]

IMAGE_TYPES: dict[str, DevoloImageEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: DevoloHomeNetworkConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DevoloImageEntity(DevoloCoordinatorEntity[WifiGuestAccessGet], ImageEntity):
    _attr_content_type: str
    entity_description: DevoloImageEntityDescription
    _attr_image_last_updated: Incomplete
    _data: Incomplete
    def __init__(self, entry: DevoloHomeNetworkConfigEntry, coordinator: DevoloDataUpdateCoordinator[WifiGuestAccessGet], description: DevoloImageEntityDescription) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    async def async_image(self) -> bytes | None: ...
