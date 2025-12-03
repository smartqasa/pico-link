from .const import CONF_FFMPEG_ARGUMENTS as CONF_FFMPEG_ARGUMENTS, DATA_COORDINATOR as DATA_COORDINATOR, DEFAULT_FFMPEG_ARGUMENTS as DEFAULT_FFMPEG_ARGUMENTS, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from .coordinator import CanaryDataUpdateCoordinator as CanaryDataUpdateCoordinator
from _typeshed import Incomplete
from aiohttp.web import Request as Request, StreamResponse as StreamResponse
from canary.live_stream_api import LiveStreamSession as LiveStreamSession
from canary.model import Device as Device, Location as Location
from homeassistant.components import ffmpeg as ffmpeg
from homeassistant.components.camera import Camera as Camera
from homeassistant.components.ffmpeg import FFmpegManager as FFmpegManager, get_ffmpeg_manager as get_ffmpeg_manager
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_aiohttp_proxy_stream as async_aiohttp_proxy_stream
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Final

FORCE_CAMERA_REFRESH_INTERVAL: Final[Incomplete]
PLATFORM_SCHEMA: Final[Incomplete]
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class CanaryCamera(CoordinatorEntity[CanaryDataUpdateCoordinator], Camera):
    _ffmpeg: FFmpegManager
    _ffmpeg_arguments: Incomplete
    _location_id: Incomplete
    _device: Incomplete
    _live_stream_session: LiveStreamSession | None
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _image: bytes | None
    _expires_at: Incomplete
    def __init__(self, hass: HomeAssistant, coordinator: CanaryDataUpdateCoordinator, location_id: str, device: Device, ffmpeg_args: str) -> None: ...
    @property
    def location(self) -> Location: ...
    @property
    def is_recording(self) -> bool: ...
    @property
    def motion_detection_enabled(self) -> bool: ...
    async def async_camera_image(self, width: int | None = None, height: int | None = None) -> bytes | None: ...
    async def handle_async_mjpeg_stream(self, request: Request) -> StreamResponse | None: ...
    def renew_live_stream_session(self) -> None: ...
