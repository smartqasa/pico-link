from .coordinator import TailwindConfigEntry as TailwindConfigEntry
from .entity import TailwindDoorEntity as TailwindDoorEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from gotailwind import TailwindDoor as TailwindDoor
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(kw_only=True, frozen=True)
class TailwindDoorBinarySensorEntityDescription(BinarySensorEntityDescription):
    is_on_fn: Callable[[TailwindDoor], bool]

DESCRIPTIONS: tuple[TailwindDoorBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: TailwindConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TailwindDoorBinarySensorEntity(TailwindDoorEntity, BinarySensorEntity):
    entity_description: TailwindDoorBinarySensorEntityDescription
    @property
    def is_on(self) -> bool | None: ...
