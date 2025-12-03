from .coordinator import AsekoConfigEntry as AsekoConfigEntry
from .entity import AsekoEntity as AsekoEntity
from aioaseko import Unit as Unit
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class AsekoBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[Unit], bool | None]

BINARY_SENSORS: tuple[AsekoBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: AsekoConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AsekoBinarySensorEntity(AsekoEntity, BinarySensorEntity):
    entity_description: AsekoBinarySensorEntityDescription
    @property
    def is_on(self) -> bool | None: ...
