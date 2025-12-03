from .const import ATTR_BITRATE as ATTR_BITRATE, ATTR_CHANNEL_ID as ATTR_CHANNEL_ID, ATTR_FPS as ATTR_FPS, ATTR_HEIGHT as ATTR_HEIGHT, ATTR_WIDTH as ATTR_WIDTH, DOMAIN as DOMAIN
from .data import ProtectData as ProtectData, ProtectDeviceType as ProtectDeviceType, UFPConfigEntry as UFPConfigEntry
from .entity import ProtectDeviceEntity as ProtectDeviceEntity
from .utils import get_camera_base_name as get_camera_base_name
from _typeshed import Incomplete
from collections.abc import Generator
from homeassistant.components.camera import Camera as Camera, CameraEntityFeature as CameraEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity
from uiprotect.data import Camera as UFPCamera, CameraChannel as CameraChannel, ProtectAdoptableDeviceModel as ProtectAdoptableDeviceModel

_LOGGER: Incomplete

@callback
def _create_rtsp_repair(hass: HomeAssistant, entry: UFPConfigEntry, data: ProtectData, camera: UFPCamera) -> None: ...
@callback
def _get_camera_channels(hass: HomeAssistant, entry: UFPConfigEntry, data: ProtectData, ufp_device: UFPCamera | None = None) -> Generator[tuple[UFPCamera, CameraChannel, bool]]: ...
def _async_camera_entities(hass: HomeAssistant, entry: UFPConfigEntry, data: ProtectData, ufp_device: UFPCamera | None = None) -> list[ProtectDeviceEntity]: ...
async def async_setup_entry(hass: HomeAssistant, entry: UFPConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

_DISABLE_FEATURE: Incomplete
_ENABLE_FEATURE: Incomplete

class ProtectCamera(ProtectDeviceEntity, Camera):
    device: UFPCamera
    _state_attrs: Incomplete
    channel: Incomplete
    _secure: Incomplete
    _disable_stream: Incomplete
    _last_image: bytes | None
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    _attr_entity_registry_enabled_default: Incomplete
    def __init__(self, data: ProtectData, camera: UFPCamera, channel: CameraChannel, is_default: bool, secure: bool, disable_stream: bool) -> None: ...
    _attr_supported_features: Incomplete
    _stream_source: Incomplete
    @callback
    def _async_set_stream_source(self) -> None: ...
    _attr_motion_detection_enabled: Incomplete
    _attr_is_recording: Incomplete
    _attr_available: Incomplete
    _attr_extra_state_attributes: Incomplete
    @callback
    def _async_update_device_from_protect(self, device: ProtectDeviceType) -> None: ...
    async def async_camera_image(self, width: int | None = None, height: int | None = None) -> bytes | None: ...
    async def stream_source(self) -> str | None: ...
    async def async_enable_motion_detection(self) -> None: ...
    async def async_disable_motion_detection(self) -> None: ...
