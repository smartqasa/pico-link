from .coordinator import LaMarzoccoConfigEntry as LaMarzoccoConfigEntry
from .entity import LaMarzoccScaleEntity as LaMarzoccScaleEntity, LaMarzoccoEntity as LaMarzoccoEntity, LaMarzoccoEntityDescription as LaMarzoccoEntityDescription
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pylamarzocco.models import LaMarzoccoMachineConfig as LaMarzoccoMachineConfig

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class LaMarzoccoBinarySensorEntityDescription(LaMarzoccoEntityDescription, BinarySensorEntityDescription):
    is_on_fn: Callable[[LaMarzoccoMachineConfig], bool | None]

ENTITIES: tuple[LaMarzoccoBinarySensorEntityDescription, ...]
SCALE_ENTITIES: tuple[LaMarzoccoBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: LaMarzoccoConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LaMarzoccoBinarySensorEntity(LaMarzoccoEntity, BinarySensorEntity):
    entity_description: LaMarzoccoBinarySensorEntityDescription
    @property
    def is_on(self) -> bool | None: ...

class LaMarzoccoScaleBinarySensorEntity(LaMarzoccoBinarySensorEntity, LaMarzoccScaleEntity):
    entity_description: LaMarzoccoBinarySensorEntityDescription
