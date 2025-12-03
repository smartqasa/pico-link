from .const import DOMAIN as DOMAIN
from .coordinator import LaMetricDataUpdateCoordinator as LaMetricDataUpdateCoordinator
from .entity import LaMetricEntity as LaMetricEntity
from .helpers import lametric_exception_handler as lametric_exception_handler
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from demetriek import Device as Device, LaMetricDevice as LaMetricDevice, Range as Range
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

@dataclass(frozen=True, kw_only=True)
class LaMetricNumberEntityDescription(NumberEntityDescription):
    value_fn: Callable[[Device], int | None]
    range_fn: Callable[[Device], Range | None]
    has_fn: Callable[[Device], bool] = ...
    set_value_fn: Callable[[LaMetricDevice, float], Awaitable[Any]]

NUMBERS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LaMetricNumberEntity(LaMetricEntity, NumberEntity):
    entity_description: LaMetricNumberEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LaMetricDataUpdateCoordinator, description: LaMetricNumberEntityDescription) -> None: ...
    @property
    def native_value(self) -> int | None: ...
    @property
    def native_min_value(self) -> int: ...
    @property
    def native_max_value(self) -> int: ...
    @lametric_exception_handler
    async def async_set_native_value(self, value: float) -> None: ...
