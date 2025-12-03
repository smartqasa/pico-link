from .const import DOMAIN as DOMAIN
from .coordinator import SleepIQData as SleepIQData
from .entity import SleepIQEntity as SleepIQEntity
from _typeshed import Incomplete
from asyncsleepiq import SleepIQBed as SleepIQBed
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

@dataclass(frozen=True, kw_only=True)
class SleepIQButtonEntityDescription(ButtonEntityDescription):
    press_action: Callable[[SleepIQBed], Any]

ENTITY_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SleepNumberButton(SleepIQEntity, ButtonEntity):
    entity_description: SleepIQButtonEntityDescription
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, bed: SleepIQBed, entity_description: SleepIQButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
