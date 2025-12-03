from .data import ProtectData as ProtectData, ProtectDeviceType as ProtectDeviceType, UFPConfigEntry as UFPConfigEntry
from .entity import PermRequired as PermRequired, ProtectDeviceEntity as ProtectDeviceEntity, ProtectEntityDescription as ProtectEntityDescription, ProtectSetableKeysMixin as ProtectSetableKeysMixin, T as T, async_all_device_entities as async_all_device_entities
from _typeshed import Incomplete
from collections.abc import Sequence
from dataclasses import dataclass
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from uiprotect.data import Camera as Camera, Doorlock, Light, ModelType, ProtectAdoptableDeviceModel as ProtectAdoptableDeviceModel

@dataclass(frozen=True, kw_only=True)
class ProtectNumberEntityDescription(ProtectSetableKeysMixin[T], NumberEntityDescription):
    ufp_max: int | float
    ufp_min: int | float
    ufp_step: int | float

def _get_pir_duration(obj: Light) -> int: ...
async def _set_pir_duration(obj: Light, value: float) -> None: ...
def _get_auto_close(obj: Doorlock) -> int: ...
async def _set_auto_close(obj: Doorlock, value: float) -> None: ...
def _get_chime_duration(obj: Camera) -> int: ...

CAMERA_NUMBERS: tuple[ProtectNumberEntityDescription, ...]
LIGHT_NUMBERS: tuple[ProtectNumberEntityDescription, ...]
SENSE_NUMBERS: tuple[ProtectNumberEntityDescription, ...]
DOORLOCK_NUMBERS: tuple[ProtectNumberEntityDescription, ...]
CHIME_NUMBERS: tuple[ProtectNumberEntityDescription, ...]
_MODEL_DESCRIPTIONS: dict[ModelType, Sequence[ProtectEntityDescription]]

async def async_setup_entry(hass: HomeAssistant, entry: UFPConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ProtectNumbers(ProtectDeviceEntity, NumberEntity):
    device: Camera | Light
    entity_description: ProtectNumberEntityDescription
    _state_attrs: Incomplete
    _attr_native_max_value: Incomplete
    _attr_native_min_value: Incomplete
    _attr_native_step: Incomplete
    def __init__(self, data: ProtectData, device: Camera | Light, description: ProtectNumberEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    @callback
    def _async_update_device_from_protect(self, device: ProtectDeviceType) -> None: ...
    async def async_set_native_value(self, value: float) -> None: ...
