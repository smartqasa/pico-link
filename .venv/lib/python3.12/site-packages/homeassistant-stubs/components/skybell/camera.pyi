from .const import DOMAIN as DOMAIN
from .coordinator import SkybellDataUpdateCoordinator as SkybellDataUpdateCoordinator
from .entity import SkybellEntity as SkybellEntity
from aiohttp import web as web
from homeassistant.components.camera import Camera as Camera, CameraEntityDescription as CameraEntityDescription
from homeassistant.components.ffmpeg import get_ffmpeg_manager as get_ffmpeg_manager
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_aiohttp_proxy_stream as async_aiohttp_proxy_stream
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

CAMERA_TYPES: tuple[CameraEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SkybellCamera(SkybellEntity, Camera):
    def __init__(self, coordinator: SkybellDataUpdateCoordinator, description: EntityDescription) -> None: ...
    async def async_camera_image(self, width: int | None = None, height: int | None = None) -> bytes | None: ...

class SkybellActivityCamera(SkybellCamera):
    async def handle_async_mjpeg_stream(self, request: web.Request) -> web.StreamResponse: ...
