from .device import ConfiguredDoorBird as ConfiguredDoorBird, async_reset_device_favorites as async_reset_device_favorites
from .entity import DoorBirdEntity as DoorBirdEntity
from .models import DoorBirdConfigEntry as DoorBirdConfigEntry, DoorBirdData as DoorBirdData
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

IR_RELAY: str

@dataclass(frozen=True, kw_only=True)
class DoorbirdButtonEntityDescription(ButtonEntityDescription):
    press_action: Callable[[ConfiguredDoorBird, str], Coroutine[Any, Any, bool | None]]

RELAY_ENTITY_DESCRIPTION: Incomplete
BUTTON_DESCRIPTIONS: tuple[DoorbirdButtonEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: DoorBirdConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DoorBirdButton(DoorBirdEntity, ButtonEntity):
    entity_description: DoorbirdButtonEntityDescription
    _relay: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, door_bird_data: DoorBirdData, entity_description: DoorbirdButtonEntityDescription, relay: str | None = None) -> None: ...
    async def async_press(self) -> None: ...
