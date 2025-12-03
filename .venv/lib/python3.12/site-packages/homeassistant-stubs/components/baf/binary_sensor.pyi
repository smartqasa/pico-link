from . import BAFConfigEntry as BAFConfigEntry
from .entity import BAFDescriptionEntity as BAFDescriptionEntity
from _typeshed import Incomplete
from aiobafi6 import Device as Device
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class BAFBinarySensorDescription(BinarySensorEntityDescription):
    value_fn: Callable[[Device], bool | None]

OCCUPANCY_SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: BAFConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BAFBinarySensor(BAFDescriptionEntity, BinarySensorEntity):
    entity_description: BAFBinarySensorDescription
    _attr_is_on: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...
