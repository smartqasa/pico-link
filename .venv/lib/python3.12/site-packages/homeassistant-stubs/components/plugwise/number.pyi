from . import PlugwiseConfigEntry as PlugwiseConfigEntry
from .const import NumberType as NumberType
from .coordinator import PlugwiseDataUpdateCoordinator as PlugwiseDataUpdateCoordinator
from .entity import PlugwiseEntity as PlugwiseEntity
from .util import plugwise_command as plugwise_command
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription, NumberMode as NumberMode
from homeassistant.const import EntityCategory as EntityCategory, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class PlugwiseNumberEntityDescription(NumberEntityDescription):
    key: NumberType

NUMBER_TYPES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: PlugwiseConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PlugwiseNumberEntity(PlugwiseEntity, NumberEntity):
    entity_description: PlugwiseNumberEntityDescription
    _attr_mode: Incomplete
    _attr_native_max_value: Incomplete
    _attr_native_min_value: Incomplete
    _attr_unique_id: Incomplete
    device_id: Incomplete
    _attr_native_step: Incomplete
    def __init__(self, coordinator: PlugwiseDataUpdateCoordinator, device_id: str, description: PlugwiseNumberEntityDescription) -> None: ...
    @property
    def native_value(self) -> float: ...
    @plugwise_command
    async def async_set_native_value(self, value: float) -> None: ...
