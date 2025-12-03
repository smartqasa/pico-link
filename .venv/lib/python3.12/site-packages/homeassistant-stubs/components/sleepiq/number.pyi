from .const import ACTUATOR as ACTUATOR, DOMAIN as DOMAIN, ENTITY_TYPES as ENTITY_TYPES, FIRMNESS as FIRMNESS, FOOT_WARMING_TIMER as FOOT_WARMING_TIMER, ICON_OCCUPIED as ICON_OCCUPIED
from .coordinator import SleepIQData as SleepIQData, SleepIQDataUpdateCoordinator as SleepIQDataUpdateCoordinator
from .entity import SleepIQBedEntity as SleepIQBedEntity, sleeper_for_side as sleeper_for_side
from _typeshed import Incomplete
from asyncsleepiq import SleepIQActuator as SleepIQActuator, SleepIQBed as SleepIQBed, SleepIQFootWarmer as SleepIQFootWarmer, SleepIQSleeper as SleepIQSleeper
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

@dataclass(frozen=True, kw_only=True)
class SleepIQNumberEntityDescription(NumberEntityDescription):
    value_fn: Callable[[Any], float]
    set_value_fn: Callable[[Any, int], Coroutine[None, None, None]]
    get_name_fn: Callable[[SleepIQBed, Any], str]
    get_unique_id_fn: Callable[[SleepIQBed, Any], str]

async def _async_set_firmness(sleeper: SleepIQSleeper, firmness: int) -> None: ...
async def _async_set_actuator_position(actuator: SleepIQActuator, position: int) -> None: ...
def _get_actuator_name(bed: SleepIQBed, actuator: SleepIQActuator) -> str: ...
def _get_actuator_unique_id(bed: SleepIQBed, actuator: SleepIQActuator) -> str: ...
def _get_sleeper_name(bed: SleepIQBed, sleeper: SleepIQSleeper) -> str: ...
def _get_sleeper_unique_id(bed: SleepIQBed, sleeper: SleepIQSleeper) -> str: ...
async def _async_set_foot_warmer_time(foot_warmer: SleepIQFootWarmer, time: int) -> None: ...
def _get_foot_warming_name(bed: SleepIQBed, foot_warmer: SleepIQFootWarmer) -> str: ...
def _get_foot_warming_unique_id(bed: SleepIQBed, foot_warmer: SleepIQFootWarmer) -> str: ...

NUMBER_DESCRIPTIONS: dict[str, SleepIQNumberEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SleepIQNumberEntity(SleepIQBedEntity[SleepIQDataUpdateCoordinator], NumberEntity):
    entity_description: SleepIQNumberEntityDescription
    _attr_icon: str
    device: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SleepIQDataUpdateCoordinator, bed: SleepIQBed, device: Any, description: SleepIQNumberEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...
    async def async_set_native_value(self, value: float) -> None: ...
