from . import AxisConfigEntry as AxisConfigEntry
from .const import DEFAULT_STREAM_PROFILE as DEFAULT_STREAM_PROFILE, DEFAULT_VIDEO_SOURCE as DEFAULT_VIDEO_SOURCE
from .entity import AxisEntity as AxisEntity
from .hub import AxisHub as AxisHub
from _typeshed import Incomplete
from homeassistant.components.camera import CameraEntityFeature as CameraEntityFeature
from homeassistant.components.mjpeg import MjpegCamera as MjpegCamera, filter_urllib3_logging as filter_urllib3_logging
from homeassistant.const import HTTP_DIGEST_AUTHENTICATION as HTTP_DIGEST_AUTHENTICATION
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, config_entry: AxisConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AxisCamera(AxisEntity, MjpegCamera):
    _attr_supported_features: Incomplete
    _still_image_url: str
    _mjpeg_url: str
    _stream_source: str
    def __init__(self, hub: AxisHub) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _generate_sources(self) -> None: ...
    @property
    def image_source(self) -> str: ...
    @property
    def mjpeg_source(self) -> str: ...
    async def stream_source(self) -> str: ...
    def generate_options(self, skip_stream_profile: bool = False, add_video_codec_h264: bool = False) -> str: ...
