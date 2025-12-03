from . import SynoApi as SynoApi
from .const import CONF_SNAPSHOT_QUALITY as CONF_SNAPSHOT_QUALITY, DEFAULT_SNAPSHOT_QUALITY as DEFAULT_SNAPSHOT_QUALITY, DOMAIN as DOMAIN, SIGNAL_CAMERA_SOURCE_CHANGED as SIGNAL_CAMERA_SOURCE_CHANGED
from .coordinator import SynologyDSMCameraUpdateCoordinator as SynologyDSMCameraUpdateCoordinator
from .entity import SynologyDSMBaseEntity as SynologyDSMBaseEntity, SynologyDSMEntityDescription as SynologyDSMEntityDescription
from .models import SynologyDSMData as SynologyDSMData
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.camera import Camera as Camera, CameraEntityDescription as CameraEntityDescription, CameraEntityFeature as CameraEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from synology_dsm.api.surveillance_station import SynoCamera as SynoCamera

_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class SynologyDSMCameraEntityDescription(CameraEntityDescription, SynologyDSMEntityDescription):
    camera_id: int

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SynoDSMCamera(SynologyDSMBaseEntity[SynologyDSMCameraUpdateCoordinator], Camera):
    _attr_supported_features: Incomplete
    entity_description: SynologyDSMCameraEntityDescription
    snapshot_quality: Incomplete
    def __init__(self, api: SynoApi, coordinator: SynologyDSMCameraUpdateCoordinator, camera_id: int) -> None: ...
    @property
    def camera_data(self) -> SynoCamera: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def available(self) -> bool: ...
    @property
    def is_recording(self) -> bool: ...
    @property
    def motion_detection_enabled(self) -> bool: ...
    def _listen_source_updates(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_camera_image(self, width: int | None = None, height: int | None = None) -> bytes | None: ...
    async def stream_source(self) -> str | None: ...
    async def async_enable_motion_detection(self) -> None: ...
    async def async_disable_motion_detection(self) -> None: ...
