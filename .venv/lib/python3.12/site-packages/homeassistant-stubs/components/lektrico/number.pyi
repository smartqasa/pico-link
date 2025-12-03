from . import LektricoConfigEntry as LektricoConfigEntry, LektricoDeviceDataUpdateCoordinator as LektricoDeviceDataUpdateCoordinator
from .entity import LektricoEntity as LektricoEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import ATTR_SERIAL_NUMBER as ATTR_SERIAL_NUMBER, CONF_TYPE as CONF_TYPE, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfElectricCurrent as UnitOfElectricCurrent
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from lektricowifi import Device as Device
from typing import Any

@dataclass(frozen=True, kw_only=True)
class LektricoNumberEntityDescription(NumberEntityDescription):
    value_fn: Callable[[dict[str, Any]], int]
    set_value_fn: Callable[[Device, int], Coroutine[Any, Any, dict[Any, Any]]]

NUMBERS: tuple[LektricoNumberEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: LektricoConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LektricoNumber(LektricoEntity, NumberEntity):
    entity_description: LektricoNumberEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, description: LektricoNumberEntityDescription, coordinator: LektricoDeviceDataUpdateCoordinator, device_name: str) -> None: ...
    @property
    def native_value(self) -> int | None: ...
    async def async_set_native_value(self, value: float) -> None: ...
