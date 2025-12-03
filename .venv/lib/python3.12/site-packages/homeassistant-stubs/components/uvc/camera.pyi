from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.camera import Camera as Camera, CameraEntityFeature as CameraEntityFeature
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import PlatformNotReady as PlatformNotReady
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util.dt import utc_from_timestamp as utc_from_timestamp
from typing import Any
from uvcclient.camera import UVCCameraClient as UVCCameraClient
from uvcclient.nvr import UVCRemote as UVCRemote

_LOGGER: Incomplete
CONF_NVR: str
CONF_KEY: str
DEFAULT_PASSWORD: str
DEFAULT_PORT: int
DEFAULT_SSL: bool
PLATFORM_SCHEMA: Incomplete

def setup_platform(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class UnifiVideoCamera(Camera):
    _attr_should_poll: bool
    _attr_brand: str
    _attr_is_streaming: bool
    _caminfo: dict[str, Any]
    _nvr: Incomplete
    _uuid: Incomplete
    _attr_name: Incomplete
    _password: Incomplete
    _connect_addr: str | None
    _camera: UVCCameraClient | None
    def __init__(self, camera: UVCRemote, uuid: str, name: str, password: str) -> None: ...
    @property
    def supported_features(self) -> CameraEntityFeature: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def is_recording(self) -> bool: ...
    @property
    def motion_detection_enabled(self) -> bool: ...
    @property
    def model(self) -> str: ...
    def _login(self) -> bool: ...
    def camera_image(self, width: int | None = None, height: int | None = None) -> bytes | None: ...
    def set_motion_detection(self, mode: bool) -> None: ...
    def enable_motion_detection(self) -> None: ...
    def disable_motion_detection(self) -> None: ...
    async def stream_source(self) -> str | None: ...
    def update(self) -> None: ...

def timestamp_ms_to_date(epoch_ms: int) -> datetime | None: ...
