from . import BAFConfigEntry as BAFConfigEntry
from .const import HALF_DAY_SECS as HALF_DAY_SECS, ONE_DAY_SECS as ONE_DAY_SECS, ONE_MIN_SECS as ONE_MIN_SECS, SPEED_RANGE as SPEED_RANGE
from .entity import BAFDescriptionEntity as BAFDescriptionEntity
from _typeshed import Incomplete
from aiobafi6 import Device as Device
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription, NumberMode as NumberMode
from homeassistant.const import EntityCategory as EntityCategory, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class BAFNumberDescription(NumberEntityDescription):
    value_fn: Callable[[Device], int | None]

AUTO_COMFORT_NUMBER_DESCRIPTIONS: Incomplete
FAN_NUMBER_DESCRIPTIONS: Incomplete
LIGHT_NUMBER_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: BAFConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BAFNumber(BAFDescriptionEntity, NumberEntity):
    entity_description: BAFNumberDescription
    _attr_native_value: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...
    async def async_set_native_value(self, value: float) -> None: ...
