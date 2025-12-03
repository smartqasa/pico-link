from . import OverkizDataConfigEntry as OverkizDataConfigEntry
from .const import IGNORED_OVERKIZ_DEVICES as IGNORED_OVERKIZ_DEVICES
from .entity import OverkizDescriptiveEntity as OverkizDescriptiveEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyoverkiz.types import StateType as OverkizStateType

@dataclass(frozen=True, kw_only=True)
class OverkizBinarySensorDescription(BinarySensorEntityDescription):
    value_fn: Callable[[OverkizStateType], bool]

BINARY_SENSOR_DESCRIPTIONS: list[OverkizBinarySensorDescription]
SUPPORTED_STATES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: OverkizDataConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OverkizBinarySensor(OverkizDescriptiveEntity, BinarySensorEntity):
    entity_description: OverkizBinarySensorDescription
    @property
    def is_on(self) -> bool | None: ...
