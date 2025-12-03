from .coordinator import AcaiaConfigEntry as AcaiaConfigEntry
from .entity import AcaiaEntity as AcaiaEntity
from aioacaia.acaiascale import AcaiaScale as AcaiaScale
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

PARALLEL_UPDATES: int

@dataclass(kw_only=True, frozen=True)
class AcaiaBinarySensorEntityDescription(BinarySensorEntityDescription):
    is_on_fn: Callable[[AcaiaScale], bool]

BINARY_SENSORS: tuple[AcaiaBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: AcaiaConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AcaiaBinarySensor(AcaiaEntity, BinarySensorEntity):
    entity_description: AcaiaBinarySensorEntityDescription
    @property
    def is_on(self) -> bool: ...
