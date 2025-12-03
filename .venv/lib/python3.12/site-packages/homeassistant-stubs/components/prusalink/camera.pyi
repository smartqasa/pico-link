from .const import DOMAIN as DOMAIN
from .coordinator import JobUpdateCoordinator as JobUpdateCoordinator
from .entity import PrusaLinkEntity as PrusaLinkEntity
from _typeshed import Incomplete
from homeassistant.components.camera import Camera as Camera
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PrusaLinkJobPreviewEntity(PrusaLinkEntity, Camera):
    last_path: str
    last_image: bytes
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: JobUpdateCoordinator) -> None: ...
    @property
    def available(self) -> bool: ...
    async def async_camera_image(self, width: int | None = None, height: int | None = None) -> bytes | None: ...
