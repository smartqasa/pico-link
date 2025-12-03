from .data import ProtectDeviceType as ProtectDeviceType, UFPConfigEntry as UFPConfigEntry
from .entity import PermRequired as PermRequired, ProtectDeviceEntity as ProtectDeviceEntity, ProtectEntityDescription as ProtectEntityDescription, ProtectSetableKeysMixin as ProtectSetableKeysMixin, T as T, async_all_device_entities as async_all_device_entities
from _typeshed import Incomplete
from collections.abc import Sequence
from dataclasses import dataclass
from homeassistant.components.text import TextEntity as TextEntity, TextEntityDescription as TextEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from uiprotect.data import Camera as Camera, ModelType, ProtectAdoptableDeviceModel as ProtectAdoptableDeviceModel

@dataclass(frozen=True, kw_only=True)
class ProtectTextEntityDescription(ProtectSetableKeysMixin[T], TextEntityDescription): ...

def _get_doorbell_current(obj: Camera) -> str | None: ...
async def _set_doorbell_message(obj: Camera, message: str) -> None: ...

CAMERA: tuple[ProtectTextEntityDescription, ...]
_MODEL_DESCRIPTIONS: dict[ModelType, Sequence[ProtectEntityDescription]]

async def async_setup_entry(hass: HomeAssistant, entry: UFPConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ProtectDeviceText(ProtectDeviceEntity, TextEntity):
    entity_description: ProtectTextEntityDescription
    _state_attrs: Incomplete
    _attr_native_value: Incomplete
    @callback
    def _async_update_device_from_protect(self, device: ProtectDeviceType) -> None: ...
    async def async_set_value(self, value: str) -> None: ...
