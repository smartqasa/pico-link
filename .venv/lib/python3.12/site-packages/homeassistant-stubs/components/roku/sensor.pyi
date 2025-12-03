from . import RokuConfigEntry as RokuConfigEntry
from .entity import RokuEntity as RokuEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from rokuecp.models import Device as RokuDevice

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class RokuSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[RokuDevice], str | None]

SENSORS: tuple[RokuSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: RokuConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RokuSensorEntity(RokuEntity, SensorEntity):
    entity_description: RokuSensorEntityDescription
    @property
    def native_value(self) -> str | None: ...
