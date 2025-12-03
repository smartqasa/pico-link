from . import FullyKioskConfigEntry as FullyKioskConfigEntry
from .coordinator import FullyKioskDataUpdateCoordinator as FullyKioskDataUpdateCoordinator
from .entity import FullyKioskEntity as FullyKioskEntity
from _typeshed import Incomplete
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

ENTITY_TYPES: tuple[NumberEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: FullyKioskConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FullyNumberEntity(FullyKioskEntity, NumberEntity):
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FullyKioskDataUpdateCoordinator, description: NumberEntityDescription) -> None: ...
    @property
    def native_value(self) -> int | None: ...
    async def async_set_native_value(self, value: float) -> None: ...
