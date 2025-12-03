from .const import DOMAIN as DOMAIN
from .models import DomainData as DomainData
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from sfrbox_api.bridge import SFRBox as SFRBox
from sfrbox_api.models import SystemInfo as SystemInfo
from typing import Any, Concatenate

def with_error_wrapping[**_P, _R](func: Callable[Concatenate[SFRBoxButton, _P], Awaitable[_R]]) -> Callable[Concatenate[SFRBoxButton, _P], Coroutine[Any, Any, _R]]: ...

@dataclass(frozen=True, kw_only=True)
class SFRBoxButtonEntityDescription(ButtonEntityDescription):
    async_press: Callable[[SFRBox], Coroutine[None, None, None]]

BUTTON_TYPES: tuple[SFRBoxButtonEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SFRBoxButton(ButtonEntity):
    entity_description: SFRBoxButtonEntityDescription
    _attr_has_entity_name: bool
    _box: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, box: SFRBox, description: SFRBoxButtonEntityDescription, system_info: SystemInfo) -> None: ...
    @with_error_wrapping
    async def async_press(self) -> None: ...
