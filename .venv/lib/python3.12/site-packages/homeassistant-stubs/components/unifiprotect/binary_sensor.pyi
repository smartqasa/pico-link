import dataclasses
from .data import ProtectData as ProtectData, ProtectDeviceType as ProtectDeviceType, UFPConfigEntry as UFPConfigEntry
from .entity import BaseProtectEntity as BaseProtectEntity, EventEntityMixin as EventEntityMixin, PermRequired as PermRequired, ProtectDeviceEntity as ProtectDeviceEntity, ProtectEntityDescription as ProtectEntityDescription, ProtectEventMixin as ProtectEventMixin, ProtectIsOnEntity as ProtectIsOnEntity, ProtectNVREntity as ProtectNVREntity, async_all_device_entities as async_all_device_entities
from _typeshed import Incomplete
from collections.abc import Sequence
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from uiprotect.data import ModelType, NVR as NVR, ProtectAdoptableDeviceModel as ProtectAdoptableDeviceModel, Sensor as Sensor
from uiprotect.data.nvr import UOSDisk as UOSDisk

_KEY_DOOR: str

@dataclasses.dataclass(frozen=True, kw_only=True)
class ProtectBinaryEntityDescription(ProtectEntityDescription, BinarySensorEntityDescription): ...
@dataclasses.dataclass(frozen=True, kw_only=True)
class ProtectBinaryEventEntityDescription(ProtectEventMixin, BinarySensorEntityDescription): ...

MOUNT_DEVICE_CLASS_MAP: Incomplete
CAMERA_SENSORS: tuple[ProtectBinaryEntityDescription, ...]
LIGHT_SENSORS: tuple[ProtectBinaryEntityDescription, ...]
MOUNTABLE_SENSE_SENSORS: tuple[ProtectBinaryEntityDescription, ...]
SENSE_SENSORS: tuple[ProtectBinaryEntityDescription, ...]
EVENT_SENSORS: tuple[ProtectBinaryEventEntityDescription, ...]
DOORLOCK_SENSORS: tuple[ProtectBinaryEntityDescription, ...]
VIEWER_SENSORS: tuple[ProtectBinaryEntityDescription, ...]
DISK_SENSORS: tuple[ProtectBinaryEntityDescription, ...]
_MODEL_DESCRIPTIONS: dict[ModelType, Sequence[ProtectEntityDescription]]
_MOUNTABLE_MODEL_DESCRIPTIONS: dict[ModelType, Sequence[ProtectEntityDescription]]

class ProtectDeviceBinarySensor(ProtectIsOnEntity, ProtectDeviceEntity, BinarySensorEntity):
    entity_description: ProtectBinaryEntityDescription

class MountableProtectDeviceBinarySensor(ProtectDeviceBinarySensor):
    device: Sensor
    _state_attrs: Incomplete
    _attr_device_class: Incomplete
    @callback
    def _async_update_device_from_protect(self, device: ProtectDeviceType) -> None: ...

class ProtectDiskBinarySensor(ProtectNVREntity, BinarySensorEntity):
    _disk: UOSDisk
    entity_description: ProtectBinaryEntityDescription
    _state_attrs: Incomplete
    def __init__(self, data: ProtectData, device: NVR, description: ProtectBinaryEntityDescription, disk: UOSDisk) -> None: ...
    _attr_available: bool
    _attr_is_on: Incomplete
    @callback
    def _async_update_device_from_protect(self, device: ProtectDeviceType) -> None: ...

class ProtectEventBinarySensor(EventEntityMixin, BinarySensorEntity):
    entity_description: ProtectBinaryEventEntityDescription
    _state_attrs: Incomplete
    _attr_is_on: bool
    _attr_extra_state_attributes: Incomplete
    @callback
    def _set_event_done(self) -> None: ...
    _event: Incomplete
    _event_end: Incomplete
    @callback
    def _async_update_device_from_protect(self, device: ProtectDeviceType) -> None: ...

MODEL_DESCRIPTIONS_WITH_CLASS: Incomplete

@callback
def _async_event_entities(data: ProtectData, ufp_device: ProtectAdoptableDeviceModel | None = None) -> list[ProtectDeviceEntity]: ...
@callback
def _async_nvr_entities(data: ProtectData) -> list[BaseProtectEntity]: ...
async def async_setup_entry(hass: HomeAssistant, entry: UFPConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
