from .const import TYPE_EMPTY_VALUE as TYPE_EMPTY_VALUE
from .data import ProtectData as ProtectData, ProtectDeviceType as ProtectDeviceType, UFPConfigEntry as UFPConfigEntry
from .entity import PermRequired as PermRequired, ProtectDeviceEntity as ProtectDeviceEntity, ProtectEntityDescription as ProtectEntityDescription, ProtectSetableKeysMixin as ProtectSetableKeysMixin, T as T, async_all_device_entities as async_all_device_entities
from .utils import async_get_light_motion_current as async_get_light_motion_current
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Sequence
from dataclasses import dataclass
from enum import Enum
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Final
from uiprotect.api import ProtectApiClient as ProtectApiClient
from uiprotect.data import Camera, Doorlock, Light, ModelType, ProtectAdoptableDeviceModel as ProtectAdoptableDeviceModel, Sensor, Viewer

_LOGGER: Incomplete
_KEY_LIGHT_MOTION: str
HDR_MODES: Incomplete
INFRARED_MODES: Incomplete
CHIME_TYPES: Incomplete
MOUNT_TYPES: Incomplete
LIGHT_MODE_MOTION: str
LIGHT_MODE_MOTION_DARK: str
LIGHT_MODE_DARK: str
LIGHT_MODE_OFF: str
LIGHT_MODES: Incomplete
LIGHT_MODE_TO_SETTINGS: Incomplete
MOTION_MODE_TO_LIGHT_MODE: Incomplete
DEVICE_RECORDING_MODES: Incomplete
DEVICE_CLASS_LCD_MESSAGE: Final[str]

@dataclass(frozen=True, kw_only=True)
class ProtectSelectEntityDescription(ProtectSetableKeysMixin[T], SelectEntityDescription):
    ufp_options: list[dict[str, Any]] | None = ...
    ufp_options_fn: Callable[[ProtectApiClient], list[dict[str, Any]]] | None = ...
    ufp_enum_type: type[Enum] | None = ...

def _get_viewer_options(api: ProtectApiClient) -> list[dict[str, Any]]: ...
def _get_doorbell_options(api: ProtectApiClient) -> list[dict[str, Any]]: ...
def _get_paired_camera_options(api: ProtectApiClient) -> list[dict[str, Any]]: ...
def _get_viewer_current(obj: Viewer) -> str: ...
def _get_doorbell_current(obj: Camera) -> str | None: ...
async def _set_light_mode(obj: Light, mode: str) -> None: ...
async def _set_paired_camera(obj: Light | Sensor | Doorlock, camera_id: str) -> None: ...
async def _set_doorbell_message(obj: Camera, message: str) -> None: ...
async def _set_liveview(obj: Viewer, liveview_id: str) -> None: ...

CAMERA_SELECTS: tuple[ProtectSelectEntityDescription, ...]
LIGHT_SELECTS: tuple[ProtectSelectEntityDescription, ...]
SENSE_SELECTS: tuple[ProtectSelectEntityDescription, ...]
DOORLOCK_SELECTS: tuple[ProtectSelectEntityDescription, ...]
VIEWER_SELECTS: tuple[ProtectSelectEntityDescription, ...]
_MODEL_DESCRIPTIONS: dict[ModelType, Sequence[ProtectEntityDescription]]

async def async_setup_entry(hass: HomeAssistant, entry: UFPConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ProtectSelects(ProtectDeviceEntity, SelectEntity):
    device: Camera | Light | Viewer
    entity_description: ProtectSelectEntityDescription
    _state_attrs: Incomplete
    def __init__(self, data: ProtectData, device: Camera | Light | Viewer, description: ProtectSelectEntityDescription) -> None: ...
    _attr_current_option: Incomplete
    @callback
    def _async_update_device_from_protect(self, device: ProtectDeviceType) -> None: ...
    _attr_options: Incomplete
    _hass_to_unifi_options: Incomplete
    _unifi_to_hass_options: Incomplete
    @callback
    def _async_set_options(self, data: ProtectData, description: ProtectSelectEntityDescription) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
