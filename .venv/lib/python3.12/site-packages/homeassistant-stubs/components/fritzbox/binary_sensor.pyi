from .coordinator import FritzboxConfigEntry as FritzboxConfigEntry
from .entity import FritzBoxDeviceEntity as FritzBoxDeviceEntity
from .model import FritzEntityDescriptionMixinBase as FritzEntityDescriptionMixinBase
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyfritzhome.fritzhomedevice import FritzhomeDevice as FritzhomeDevice
from typing import Final

@dataclass(frozen=True)
class FritzEntityDescriptionMixinBinarySensor(FritzEntityDescriptionMixinBase):
    is_on: Callable[[FritzhomeDevice], bool | None]

@dataclass(frozen=True)
class FritzBinarySensorEntityDescription(BinarySensorEntityDescription, FritzEntityDescriptionMixinBinarySensor): ...

BINARY_SENSOR_TYPES: Final[tuple[FritzBinarySensorEntityDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: FritzboxConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FritzboxBinarySensor(FritzBoxDeviceEntity, BinarySensorEntity):
    entity_description: FritzBinarySensorEntityDescription
    @property
    def is_on(self) -> bool | None: ...
