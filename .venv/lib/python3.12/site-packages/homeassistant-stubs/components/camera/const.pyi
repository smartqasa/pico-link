from . import Camera as Camera
from .prefs import CameraPreferences as CameraPreferences
from enum import StrEnum
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Final

DOMAIN: Final[str]
DATA_COMPONENT: HassKey[EntityComponent[Camera]]
DATA_CAMERA_PREFS: HassKey[CameraPreferences]
PREF_PRELOAD_STREAM: Final[str]
PREF_ORIENTATION: Final[str]
SERVICE_RECORD: Final[str]
CONF_LOOKBACK: Final[str]
CONF_DURATION: Final[str]
CAMERA_STREAM_SOURCE_TIMEOUT: Final[int]
CAMERA_IMAGE_TIMEOUT: Final[int]

class CameraState(StrEnum):
    RECORDING = 'recording'
    STREAMING = 'streaming'
    IDLE = 'idle'

class StreamType(StrEnum):
    HLS = 'hls'
    WEB_RTC = 'web_rtc'
