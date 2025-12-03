from .entity import ReolinkChannelCoordinatorEntity as ReolinkChannelCoordinatorEntity, ReolinkChannelEntityDescription as ReolinkChannelEntityDescription, ReolinkChimeCoordinatorEntity as ReolinkChimeCoordinatorEntity, ReolinkChimeEntityDescription as ReolinkChimeEntityDescription, ReolinkHostCoordinatorEntity as ReolinkHostCoordinatorEntity, ReolinkHostEntityDescription as ReolinkHostEntityDescription
from .util import ReolinkConfigEntry as ReolinkConfigEntry, ReolinkData as ReolinkData, raise_translated_error as raise_translated_error
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription, NumberMode as NumberMode
from homeassistant.const import EntityCategory as EntityCategory, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from reolink_aio.api import Chime as Chime, Host as Host
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class ReolinkNumberEntityDescription(NumberEntityDescription, ReolinkChannelEntityDescription):
    get_max_value: Callable[[Host, int], float] | None = ...
    get_min_value: Callable[[Host, int], float] | None = ...
    method: Callable[[Host, int, float], Any]
    mode: NumberMode = ...
    value: Callable[[Host, int], float | None]

@dataclass(frozen=True, kw_only=True)
class ReolinkHostNumberEntityDescription(NumberEntityDescription, ReolinkHostEntityDescription):
    method: Callable[[Host, float], Any]
    mode: NumberMode = ...
    value: Callable[[Host], float | None]

@dataclass(frozen=True, kw_only=True)
class ReolinkChimeNumberEntityDescription(NumberEntityDescription, ReolinkChimeEntityDescription):
    method: Callable[[Chime, float], Any]
    mode: NumberMode = ...
    value: Callable[[Chime], float | None]

NUMBER_ENTITIES: Incomplete
HOST_NUMBER_ENTITIES: Incomplete
CHIME_NUMBER_ENTITIES: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ReolinkConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ReolinkNumberEntity(ReolinkChannelCoordinatorEntity, NumberEntity):
    entity_description: ReolinkNumberEntityDescription
    _attr_native_min_value: Incomplete
    _attr_native_max_value: Incomplete
    _attr_mode: Incomplete
    def __init__(self, reolink_data: ReolinkData, channel: int, entity_description: ReolinkNumberEntityDescription) -> None: ...
    @property
    def native_value(self) -> float | None: ...
    @raise_translated_error
    async def async_set_native_value(self, value: float) -> None: ...

class ReolinkHostNumberEntity(ReolinkHostCoordinatorEntity, NumberEntity):
    entity_description: ReolinkHostNumberEntityDescription
    _attr_mode: Incomplete
    def __init__(self, reolink_data: ReolinkData, entity_description: ReolinkHostNumberEntityDescription) -> None: ...
    @property
    def native_value(self) -> float | None: ...
    @raise_translated_error
    async def async_set_native_value(self, value: float) -> None: ...

class ReolinkChimeNumberEntity(ReolinkChimeCoordinatorEntity, NumberEntity):
    entity_description: ReolinkChimeNumberEntityDescription
    _attr_mode: Incomplete
    def __init__(self, reolink_data: ReolinkData, chime: Chime, entity_description: ReolinkChimeNumberEntityDescription) -> None: ...
    @property
    def native_value(self) -> float | None: ...
    @raise_translated_error
    async def async_set_native_value(self, value: float) -> None: ...
