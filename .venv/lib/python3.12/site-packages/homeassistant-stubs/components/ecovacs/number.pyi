from . import EcovacsConfigEntry as EcovacsConfigEntry
from .entity import EcovacsCapabilityEntityDescription as EcovacsCapabilityEntityDescription, EcovacsDescriptionEntity as EcovacsDescriptionEntity, EcovacsEntity as EcovacsEntity, EventT as EventT
from .util import get_supported_entitites as get_supported_entitites
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from deebot_client.capabilities import CapabilitySet
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription, NumberMode as NumberMode
from homeassistant.const import DEGREE as DEGREE, EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Generic

@dataclass(kw_only=True, frozen=True)
class EcovacsNumberEntityDescription(NumberEntityDescription, EcovacsCapabilityEntityDescription, Generic[EventT]):
    native_max_value_fn: Callable[[EventT], float | int | None] = ...
    value_fn: Callable[[EventT], float | None]

ENTITY_DESCRIPTIONS: tuple[EcovacsNumberEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: EcovacsConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EcovacsNumberEntity(EcovacsDescriptionEntity[CapabilitySet[EventT, [int]]], NumberEntity):
    entity_description: EcovacsNumberEntityDescription
    _attr_native_value: Incomplete
    _attr_native_max_value: Incomplete
    async def async_added_to_hass(self) -> None: ...
    async def async_set_native_value(self, value: float) -> None: ...
