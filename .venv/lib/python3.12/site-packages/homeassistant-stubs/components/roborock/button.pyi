from . import RoborockConfigEntry as RoborockConfigEntry
from .coordinator import RoborockDataUpdateCoordinator as RoborockDataUpdateCoordinator
from .entity import RoborockEntityV1 as RoborockEntityV1
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from roborock.roborock_typing import RoborockCommand

@dataclass(frozen=True, kw_only=True)
class RoborockButtonDescription(ButtonEntityDescription):
    command: RoborockCommand
    param: list | dict | None

CONSUMABLE_BUTTON_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: RoborockConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RoborockButtonEntity(RoborockEntityV1, ButtonEntity):
    entity_description: RoborockButtonDescription
    def __init__(self, coordinator: RoborockDataUpdateCoordinator, entity_description: RoborockButtonDescription) -> None: ...
    async def async_press(self) -> None: ...
