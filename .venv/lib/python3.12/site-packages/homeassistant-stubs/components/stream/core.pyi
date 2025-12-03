import asyncio
import datetime
import numpy as np
from . import Stream as Stream
from .const import ATTR_STREAMS as ATTR_STREAMS, DOMAIN as DOMAIN, SEGMENT_DURATION_ADJUSTER as SEGMENT_DURATION_ADJUSTER, TARGET_SEGMENT_DURATION_NON_LL_HLS as TARGET_SEGMENT_DURATION_NON_LL_HLS
from _typeshed import Incomplete
from aiohttp import web
from av import Packet as Packet, VideoCodecContext as VideoCodecContext
from collections import deque
from collections.abc import Callable as Callable, Coroutine, Iterable
from dataclasses import dataclass, field
from enum import IntEnum
from homeassistant.components.camera import DynamicStreamSettings as DynamicStreamSettings
from homeassistant.components.http import HomeAssistantView as HomeAssistantView, KEY_HASS as KEY_HASS
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.util.decorator import Registry as Registry
from typing import Any

_LOGGER: Incomplete
PROVIDERS: Registry[str, type[StreamOutput]]

class Orientation(IntEnum):
    NO_TRANSFORM = 1
    MIRROR = 2
    ROTATE_180 = 3
    FLIP = 4
    ROTATE_LEFT_AND_FLIP = 5
    ROTATE_LEFT = 6
    ROTATE_RIGHT_AND_FLIP = 7
    ROTATE_RIGHT = 8

@dataclass(slots=True)
class StreamSettings:
    ll_hls: bool
    min_segment_duration: float
    part_target_duration: float
    hls_advance_part_limit: int
    hls_part_timeout: float

STREAM_SETTINGS_NON_LL_HLS: Incomplete

@dataclass(slots=True)
class Part:
    duration: float
    has_keyframe: bool
    data: bytes

@dataclass(slots=True)
class Segment:
    sequence: int
    init: bytes
    stream_id: int
    start_time: datetime.datetime
    _stream_outputs: Iterable[StreamOutput]
    duration: float = ...
    parts: list[Part] = field(default_factory=list)
    hls_playlist_template: list[str] = field(default_factory=list)
    hls_playlist_parts: list[str] = field(default_factory=list)
    hls_num_parts_rendered: int = ...
    hls_playlist_complete: bool = ...
    def __post_init__(self) -> None: ...
    @property
    def complete(self) -> bool: ...
    @property
    def data_size_with_init(self) -> int: ...
    @property
    def data_size(self) -> int: ...
    @callback
    def async_add_part(self, part: Part, duration: float) -> None: ...
    def get_data(self) -> bytes: ...
    def _render_hls_template(self, last_stream_id: int, render_parts: bool) -> str: ...
    def render_hls(self, last_stream_id: int, render_parts: bool, add_hint: bool) -> str: ...

class IdleTimer:
    _hass: Incomplete
    _timeout: Incomplete
    _callback: Incomplete
    _unsub: CALLBACK_TYPE | None
    idle: bool
    def __init__(self, hass: HomeAssistant, timeout: int, idle_callback: Callable[[], Coroutine[Any, Any, None]]) -> None: ...
    def start(self) -> None: ...
    def awake(self) -> None: ...
    def clear(self) -> None: ...
    @callback
    def fire(self, _now: datetime.datetime) -> None: ...

class StreamOutput:
    _hass: Incomplete
    idle_timer: Incomplete
    stream_settings: Incomplete
    dynamic_stream_settings: Incomplete
    _event: Incomplete
    _part_event: Incomplete
    _segments: deque[Segment]
    def __init__(self, hass: HomeAssistant, idle_timer: IdleTimer, stream_settings: StreamSettings, dynamic_stream_settings: DynamicStreamSettings, deque_maxlen: int | None = None) -> None: ...
    @property
    def name(self) -> str | None: ...
    @property
    def idle(self) -> bool: ...
    @property
    def last_sequence(self) -> int: ...
    @property
    def sequences(self) -> list[int]: ...
    @property
    def last_segment(self) -> Segment | None: ...
    def get_segment(self, sequence: int) -> Segment | None: ...
    def get_segments(self) -> deque[Segment]: ...
    async def part_recv(self, timeout: float | None = None) -> bool: ...
    def part_put(self) -> None: ...
    async def recv(self) -> bool: ...
    def put(self, segment: Segment) -> None: ...
    @callback
    def _async_put(self, segment: Segment) -> None: ...
    def cleanup(self) -> None: ...

class StreamView(HomeAssistantView):
    requires_auth: bool
    async def get(self, request: web.Request, token: str, sequence: str = '', part_num: str = '') -> web.StreamResponse: ...
    async def handle(self, request: web.Request, stream: Stream, sequence: str, part_num: str) -> web.StreamResponse: ...

TRANSFORM_IMAGE_FUNCTION: Incomplete

class KeyFrameConverter:
    _packet: Packet | None
    _event: asyncio.Event
    _hass: Incomplete
    _image: bytes | None
    _turbojpeg: Incomplete
    _lock: Incomplete
    _codec_context: VideoCodecContext | None
    _stream_settings: Incomplete
    _dynamic_stream_settings: Incomplete
    def __init__(self, hass: HomeAssistant, stream_settings: StreamSettings, dynamic_stream_settings: DynamicStreamSettings) -> None: ...
    def stash_keyframe_packet(self, packet: Packet) -> None: ...
    def create_codec_context(self, codec_context: VideoCodecContext) -> None: ...
    @staticmethod
    def transform_image(image: np.ndarray, orientation: int) -> np.ndarray: ...
    def _generate_image(self, width: int | None, height: int | None) -> None: ...
    async def async_get_image(self, width: int | None = None, height: int | None = None, wait_for_next_keyframe: bool = False) -> bytes | None: ...
