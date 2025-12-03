from . import Stream as Stream
from .const import EXT_X_START_LL_HLS as EXT_X_START_LL_HLS, EXT_X_START_NON_LL_HLS as EXT_X_START_NON_LL_HLS, FORMAT_CONTENT_TYPE as FORMAT_CONTENT_TYPE, HLS_PROVIDER as HLS_PROVIDER, MAX_SEGMENTS as MAX_SEGMENTS, NUM_PLAYLIST_SEGMENTS as NUM_PLAYLIST_SEGMENTS
from .core import IdleTimer as IdleTimer, PROVIDERS as PROVIDERS, Segment as Segment, StreamOutput as StreamOutput, StreamSettings as StreamSettings, StreamView as StreamView
from .fmp4utils import get_codec_string as get_codec_string, transform_init as transform_init
from _typeshed import Incomplete
from aiohttp import web
from homeassistant.components.camera import DynamicStreamSettings as DynamicStreamSettings
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

@callback
def async_setup_hls(hass: HomeAssistant) -> str: ...

class HlsStreamOutput(StreamOutput):
    _target_duration: Incomplete
    def __init__(self, hass: HomeAssistant, idle_timer: IdleTimer, stream_settings: StreamSettings, dynamic_stream_settings: DynamicStreamSettings) -> None: ...
    @property
    def name(self) -> str: ...
    def cleanup(self) -> None: ...
    @property
    def target_duration(self) -> float: ...
    @callback
    def _async_put(self, segment: Segment) -> None: ...
    def discontinuity(self) -> None: ...
    @callback
    def _async_discontinuity(self) -> None: ...

class HlsMasterPlaylistView(StreamView):
    url: str
    name: str
    cors_allowed: bool
    @staticmethod
    def render(track: StreamOutput) -> str: ...
    async def handle(self, request: web.Request, stream: Stream, sequence: str, part_num: str) -> web.Response: ...

class HlsPlaylistView(StreamView):
    url: str
    name: str
    cors_allowed: bool
    @classmethod
    def render(cls, track: HlsStreamOutput) -> str: ...
    @staticmethod
    def bad_request(blocking: bool, target_duration: float) -> web.Response: ...
    @staticmethod
    def not_found(blocking: bool, target_duration: float) -> web.Response: ...
    async def handle(self, request: web.Request, stream: Stream, sequence: str, part_num: str) -> web.Response: ...

class HlsInitView(StreamView):
    url: str
    name: str
    cors_allowed: bool
    async def handle(self, request: web.Request, stream: Stream, sequence: str, part_num: str) -> web.Response: ...

class HlsPartView(StreamView):
    url: str
    name: str
    cors_allowed: bool
    async def handle(self, request: web.Request, stream: Stream, sequence: str, part_num: str) -> web.Response: ...

class HlsSegmentView(StreamView):
    url: str
    name: str
    cors_allowed: bool
    async def handle(self, request: web.Request, stream: Stream, sequence: str, part_num: str) -> web.StreamResponse: ...
