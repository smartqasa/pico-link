from .coordinator import PeblarConfigEntry as PeblarConfigEntry, PeblarData as PeblarData, PeblarDataUpdateCoordinator as PeblarDataUpdateCoordinator
from .entity import PeblarEntity as PeblarEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class PeblarBinarySensorEntityDescription(BinarySensorEntityDescription):
    is_on_fn: Callable[[PeblarData], bool]

DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: PeblarConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PeblarBinarySensorEntity(PeblarEntity[PeblarDataUpdateCoordinator], BinarySensorEntity):
    entity_description: PeblarBinarySensorEntityDescription
    @property
    def is_on(self) -> bool: ...
