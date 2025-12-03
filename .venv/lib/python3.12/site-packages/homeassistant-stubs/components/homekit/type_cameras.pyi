import asyncio
from .accessories import HomeDriver as HomeDriver, TYPES as TYPES
from .const import CHAR_MOTION_DETECTED as CHAR_MOTION_DETECTED, CONF_AUDIO_CODEC as CONF_AUDIO_CODEC, CONF_AUDIO_MAP as CONF_AUDIO_MAP, CONF_AUDIO_PACKET_SIZE as CONF_AUDIO_PACKET_SIZE, CONF_LINKED_MOTION_SENSOR as CONF_LINKED_MOTION_SENSOR, CONF_MAX_FPS as CONF_MAX_FPS, CONF_MAX_HEIGHT as CONF_MAX_HEIGHT, CONF_MAX_WIDTH as CONF_MAX_WIDTH, CONF_STREAM_ADDRESS as CONF_STREAM_ADDRESS, CONF_STREAM_COUNT as CONF_STREAM_COUNT, CONF_STREAM_SOURCE as CONF_STREAM_SOURCE, CONF_SUPPORT_AUDIO as CONF_SUPPORT_AUDIO, CONF_VIDEO_CODEC as CONF_VIDEO_CODEC, CONF_VIDEO_MAP as CONF_VIDEO_MAP, CONF_VIDEO_PACKET_SIZE as CONF_VIDEO_PACKET_SIZE, CONF_VIDEO_PROFILE_NAMES as CONF_VIDEO_PROFILE_NAMES, DEFAULT_AUDIO_CODEC as DEFAULT_AUDIO_CODEC, DEFAULT_AUDIO_MAP as DEFAULT_AUDIO_MAP, DEFAULT_AUDIO_PACKET_SIZE as DEFAULT_AUDIO_PACKET_SIZE, DEFAULT_MAX_FPS as DEFAULT_MAX_FPS, DEFAULT_MAX_HEIGHT as DEFAULT_MAX_HEIGHT, DEFAULT_MAX_WIDTH as DEFAULT_MAX_WIDTH, DEFAULT_STREAM_COUNT as DEFAULT_STREAM_COUNT, DEFAULT_SUPPORT_AUDIO as DEFAULT_SUPPORT_AUDIO, DEFAULT_VIDEO_CODEC as DEFAULT_VIDEO_CODEC, DEFAULT_VIDEO_MAP as DEFAULT_VIDEO_MAP, DEFAULT_VIDEO_PACKET_SIZE as DEFAULT_VIDEO_PACKET_SIZE, DEFAULT_VIDEO_PROFILE_NAMES as DEFAULT_VIDEO_PROFILE_NAMES, SERV_MOTION_SENSOR as SERV_MOTION_SENSOR
from .doorbell import HomeDoorbellAccessory as HomeDoorbellAccessory
from .util import pid_is_alive as pid_is_alive, state_changed_event_is_same_state as state_changed_event_is_same_state
from _typeshed import Incomplete
from homeassistant.components import camera as camera
from homeassistant.components.ffmpeg import get_ffmpeg_manager as get_ffmpeg_manager
from homeassistant.const import STATE_ON as STATE_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import Event as Event, EventStateChangedData as EventStateChangedData, HassJobType as HassJobType, HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event, async_track_time_interval as async_track_time_interval
from homeassistant.util.async_ import create_eager_task as create_eager_task
from pyhap.camera import Camera as PyhapCamera
from pyhap.util import callback as pyhap_callback
from typing import Any

_LOGGER: Incomplete
VIDEO_OUTPUT: str
AUDIO_OUTPUT: str
SLOW_RESOLUTIONS: Incomplete
RESOLUTIONS: Incomplete
FFMPEG_WATCH_INTERVAL: Incomplete
FFMPEG_LOGGER: str
FFMPEG_WATCHER: str
FFMPEG_PID: str
SESSION_ID: str
CONFIG_DEFAULTS: Incomplete

class Camera(HomeDoorbellAccessory, PyhapCamera):
    _ffmpeg: Incomplete
    _char_motion_detected: Incomplete
    linked_motion_sensor: str | None
    motion_is_event: bool
    def __init__(self, hass: HomeAssistant, driver: HomeDriver, name: str, entity_id: str, aid: int, config: dict[str, Any]) -> None: ...
    @pyhap_callback
    @callback
    def run(self) -> None: ...
    @callback
    def _async_update_motion_state_event(self, event: Event[EventStateChangedData]) -> None: ...
    @callback
    def _async_update_motion_state(self, old_state: State | None, new_state: State) -> None: ...
    @callback
    def async_update_state(self, new_state: State | None) -> None: ...
    async def _async_get_stream_source(self) -> str | None: ...
    async def start_stream(self, session_info: dict[str, Any], stream_config: dict[str, Any]) -> bool: ...
    async def _async_log_stderr_stream(self, stderr_reader: asyncio.StreamReader) -> None: ...
    async def _async_ffmpeg_watch(self, session_id: str) -> bool: ...
    @callback
    def _async_stop_ffmpeg_watch(self, session_id: str) -> None: ...
    @callback
    def async_stop(self) -> None: ...
    async def stop_stream(self, session_info: dict[str, Any]) -> None: ...
    async def reconfigure_stream(self, session_info: dict[str, Any], stream_config: dict[str, Any]) -> bool: ...
    async def async_get_snapshot(self, image_size: dict[str, int]) -> bytes: ...
