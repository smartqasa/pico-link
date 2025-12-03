from . import RingConfigEntry as RingConfigEntry
from .coordinator import RingDataCoordinator as RingDataCoordinator
from .entity import RingDeviceT as RingDeviceT, RingEntity as RingEntity, exception_wrap as exception_wrap
from _typeshed import Incomplete
from aiohttp import web as web
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components import ffmpeg as ffmpeg
from homeassistant.components.camera import Camera as Camera, CameraEntityDescription as CameraEntityDescription, CameraEntityFeature as CameraEntityFeature, RTCIceCandidateInit as RTCIceCandidateInit, WebRTCAnswer as WebRTCAnswer, WebRTCCandidate as WebRTCCandidate, WebRTCError as WebRTCError, WebRTCSendMessage as WebRTCSendMessage
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.aiohttp_client import async_aiohttp_proxy_stream as async_aiohttp_proxy_stream
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from ring_doorbell import RingDoorBell
from ring_doorbell.webrtcstream import RingWebRtcMessage as RingWebRtcMessage
from typing import Any, Generic

FORCE_REFRESH_INTERVAL: Incomplete
MOTION_DETECTION_CAPABILITY: str
_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class RingCameraEntityDescription(CameraEntityDescription, Generic[RingDeviceT]):
    exists_fn: Callable[[RingDoorBell], bool]
    live_stream: bool
    motion_detection: bool

CAMERA_DESCRIPTIONS: tuple[RingCameraEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: RingConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RingCam(RingEntity[RingDoorBell], Camera):
    entity_description: Incomplete
    _ffmpeg_manager: Incomplete
    _last_event: dict[str, Any] | None
    _last_video_id: int | None
    _video_url: str | None
    _images: dict[tuple[int | None, int | None], bytes]
    _expires_at: Incomplete
    _attr_unique_id: Incomplete
    _attr_motion_detection_enabled: Incomplete
    def __init__(self, device: RingDoorBell, coordinator: RingDataCoordinator, description: RingCameraEntityDescription, *, ffmpeg_manager: ffmpeg.FFmpegManager) -> None: ...
    _device: Incomplete
    @callback
    def _handle_coordinator_update(self) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    async def async_camera_image(self, width: int | None = None, height: int | None = None) -> bytes | None: ...
    async def handle_async_mjpeg_stream(self, request: web.Request) -> web.StreamResponse | None: ...
    async def async_handle_async_webrtc_offer(self, offer_sdp: str, session_id: str, send_message: WebRTCSendMessage) -> None: ...
    async def async_on_webrtc_candidate(self, session_id: str, candidate: RTCIceCandidateInit) -> None: ...
    @callback
    def close_webrtc_session(self, session_id: str) -> None: ...
    async def async_update(self) -> None: ...
    @exception_wrap
    async def _async_get_video(self) -> str | None: ...
    @exception_wrap
    async def _async_set_motion_detection_enabled(self, new_state: bool) -> None: ...
    async def async_enable_motion_detection(self) -> None: ...
    async def async_disable_motion_detection(self) -> None: ...
