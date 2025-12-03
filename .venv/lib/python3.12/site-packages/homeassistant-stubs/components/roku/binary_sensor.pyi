from . import RokuConfigEntry as RokuConfigEntry
from .entity import RokuEntity as RokuEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from rokuecp.models import Device as RokuDevice

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class RokuBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[RokuDevice], bool | None]

BINARY_SENSORS: tuple[RokuBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: RokuConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RokuBinarySensorEntity(RokuEntity, BinarySensorEntity):
    entity_description: RokuBinarySensorEntityDescription
    @property
    def is_on(self) -> bool | None: ...
