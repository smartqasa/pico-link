from . import FullyKioskConfigEntry as FullyKioskConfigEntry
from .coordinator import FullyKioskDataUpdateCoordinator as FullyKioskDataUpdateCoordinator
from .entity import FullyKioskEntity as FullyKioskEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from fullykiosk import FullyKiosk as FullyKiosk
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

@dataclass(frozen=True, kw_only=True)
class FullyButtonEntityDescription(ButtonEntityDescription):
    press_action: Callable[[FullyKiosk], Any]

BUTTONS: tuple[FullyButtonEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: FullyKioskConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FullyButtonEntity(FullyKioskEntity, ButtonEntity):
    entity_description: FullyButtonEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FullyKioskDataUpdateCoordinator, description: FullyButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
