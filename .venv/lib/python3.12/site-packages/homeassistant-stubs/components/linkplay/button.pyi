from . import LinkPlayConfigEntry as LinkPlayConfigEntry
from .entity import LinkPlayBaseEntity as LinkPlayBaseEntity, exception_wrap as exception_wrap
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from linkplay.bridge import LinkPlayBridge as LinkPlayBridge
from typing import Any

_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class LinkPlayButtonEntityDescription(ButtonEntityDescription):
    remote_function: Callable[[LinkPlayBridge], Coroutine[Any, Any, None]]

BUTTON_TYPES: tuple[LinkPlayButtonEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: LinkPlayConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LinkPlayButton(LinkPlayBaseEntity, ButtonEntity):
    entity_description: LinkPlayButtonEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, bridge: LinkPlayBridge, description: LinkPlayButtonEntityDescription) -> None: ...
    @exception_wrap
    async def async_press(self) -> None: ...
