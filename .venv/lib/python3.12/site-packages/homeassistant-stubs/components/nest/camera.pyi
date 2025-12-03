import datetime
import functools
from .device_info import NestDeviceInfo as NestDeviceInfo
from .types import NestConfigEntry as NestConfigEntry
from _typeshed import Incomplete
from abc import ABC
from collections.abc import Awaitable, Callable as Callable
from google_nest_sdm.camera_traits import CameraLiveStreamTrait, RtspStream as RtspStream, WebRtcStream as WebRtcStream
from google_nest_sdm.device import Device as Device
from homeassistant.components.camera import Camera as Camera, CameraEntityFeature as CameraEntityFeature, WebRTCAnswer as WebRTCAnswer, WebRTCClientConfiguration as WebRTCClientConfiguration, WebRTCSendMessage as WebRTCSendMessage
from homeassistant.components.stream import CONF_EXTRA_PART_WAIT_TIME as CONF_EXTRA_PART_WAIT_TIME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_point_in_utc_time as async_track_point_in_utc_time
from homeassistant.util.dt import utcnow as utcnow
from webrtc_models import RTCIceCandidateInit as RTCIceCandidateInit

_LOGGER: Incomplete
PLACEHOLDER: Incomplete
STREAM_EXPIRATION_BUFFER: Incomplete
MIN_REFRESH_BACKOFF_INTERVAL: Incomplete
MAX_REFRESH_BACKOFF_INTERVAL: Incomplete
BACKOFF_MULTIPLIER: float

async def async_setup_entry(hass: HomeAssistant, entry: NestConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class StreamRefresh:
    _hass: Incomplete
    _unsub: Callable[[], None] | None
    _min_refresh_interval: Incomplete
    _refresh_cb: Incomplete
    def __init__(self, hass: HomeAssistant, expires_at: datetime.datetime, refresh_cb: Callable[[], Awaitable[datetime.datetime | None]]) -> None: ...
    def unsub(self) -> None: ...
    async def _handle_refresh(self, _: datetime.datetime) -> None: ...
    def _schedule_stream_refresh(self, refresh_time: datetime.datetime) -> None: ...

class NestCameraBaseEntity(Camera, ABC):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_is_streaming: bool
    _attr_supported_features: Incomplete
    _device: Incomplete
    _attr_device_info: Incomplete
    _attr_brand: Incomplete
    _attr_model: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, device: Device) -> None: ...
    async def async_added_to_hass(self) -> None: ...

class NestRTSPEntity(NestCameraBaseEntity):
    _rtsp_stream: RtspStream | None
    _rtsp_live_stream_trait: CameraLiveStreamTrait
    _create_stream_url_lock: Incomplete
    _refresh_unsub: Callable[[], None] | None
    def __init__(self, device: Device) -> None: ...
    @property
    def use_stream_for_stills(self) -> bool: ...
    @property
    def available(self) -> bool: ...
    async def stream_source(self) -> str | None: ...
    stream: Incomplete
    async def _async_refresh_stream(self) -> datetime.datetime | None: ...
    async def async_will_remove_from_hass(self) -> None: ...

class NestWebRTCEntity(NestCameraBaseEntity):
    _webrtc_sessions: dict[str, WebRtcStream]
    _refresh_unsub: dict[str, Callable[[], None]]
    def __init__(self, device: Device) -> None: ...
    async def _async_refresh_stream(self, session_id: str) -> datetime.datetime | None: ...
    async def async_camera_image(self, width: int | None = None, height: int | None = None) -> bytes | None: ...
    @classmethod
    @functools.cache
    def placeholder_image(cls) -> bytes: ...
    async def async_handle_async_webrtc_offer(self, offer_sdp: str, session_id: str, send_message: WebRTCSendMessage) -> None: ...
    async def async_on_webrtc_candidate(self, session_id: str, candidate: RTCIceCandidateInit) -> None: ...
    @callback
    def close_webrtc_session(self, session_id: str) -> None: ...
    @callback
    def _async_get_webrtc_client_configuration(self) -> WebRTCClientConfiguration: ...
    async def async_will_remove_from_hass(self) -> None: ...
