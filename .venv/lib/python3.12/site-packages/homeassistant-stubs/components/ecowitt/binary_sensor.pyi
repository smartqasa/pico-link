from . import EcowittConfigEntry as EcowittConfigEntry
from .entity import EcowittEntity as EcowittEntity
from _typeshed import Incomplete
from aioecowitt import EcoWittSensor as EcoWittSensor
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Final

ECOWITT_BINARYSENSORS_MAPPING: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: EcowittConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EcowittBinarySensorEntity(EcowittEntity, BinarySensorEntity):
    entity_description: Incomplete
    def __init__(self, sensor: EcoWittSensor, description: BinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
