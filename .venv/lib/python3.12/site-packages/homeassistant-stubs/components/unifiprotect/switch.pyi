from .data import ProtectData as ProtectData, ProtectDeviceType as ProtectDeviceType, UFPConfigEntry as UFPConfigEntry
from .entity import BaseProtectEntity as BaseProtectEntity, PermRequired as PermRequired, ProtectDeviceEntity as ProtectDeviceEntity, ProtectEntityDescription as ProtectEntityDescription, ProtectIsOnEntity as ProtectIsOnEntity, ProtectNVREntity as ProtectNVREntity, ProtectSetableKeysMixin as ProtectSetableKeysMixin, T as T, async_all_device_entities as async_all_device_entities
from _typeshed import Incomplete
from collections.abc import Sequence
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from typing import Any
from uiprotect.data import Camera, ModelType, ProtectAdoptableDeviceModel as ProtectAdoptableDeviceModel

ATTR_PREV_MIC: str
ATTR_PREV_RECORD: str

@dataclass(frozen=True, kw_only=True)
class ProtectSwitchEntityDescription(ProtectSetableKeysMixin[T], SwitchEntityDescription): ...

async def _set_highfps(obj: Camera, value: bool) -> None: ...

CAMERA_SWITCHES: tuple[ProtectSwitchEntityDescription, ...]
PRIVACY_MODE_SWITCH: Incomplete
SENSE_SWITCHES: tuple[ProtectSwitchEntityDescription, ...]
LIGHT_SWITCHES: tuple[ProtectSwitchEntityDescription, ...]
DOORLOCK_SWITCHES: tuple[ProtectSwitchEntityDescription, ...]
VIEWER_SWITCHES: tuple[ProtectSwitchEntityDescription, ...]
NVR_SWITCHES: tuple[ProtectSwitchEntityDescription, ...]
_MODEL_DESCRIPTIONS: dict[ModelType, Sequence[ProtectEntityDescription]]
_PRIVACY_DESCRIPTIONS: dict[ModelType, Sequence[ProtectEntityDescription]]

class ProtectBaseSwitch(ProtectIsOnEntity):
    entity_description: ProtectSwitchEntityDescription
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class ProtectSwitch(ProtectDeviceEntity, ProtectBaseSwitch, SwitchEntity):
    entity_description: ProtectSwitchEntityDescription

class ProtectNVRSwitch(ProtectNVREntity, ProtectBaseSwitch, SwitchEntity):
    entity_description: ProtectSwitchEntityDescription

class ProtectPrivacyModeSwitch(RestoreEntity, ProtectSwitch):
    device: Camera
    entity_description: ProtectSwitchEntityDescription
    _previous_mic_level: Incomplete
    _previous_record_mode: Incomplete
    def __init__(self, data: ProtectData, device: Camera, description: ProtectSwitchEntityDescription) -> None: ...
    _attr_extra_state_attributes: Incomplete
    @callback
    def _update_previous_attr(self) -> None: ...
    @callback
    def _async_update_device_from_protect(self, device: ProtectDeviceType) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_added_to_hass(self) -> None: ...

async def async_setup_entry(hass: HomeAssistant, entry: UFPConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
