from . import MadVRConfigEntry as MadVRConfigEntry
from .coordinator import MadVRCoordinator as MadVRCoordinator
from .entity import MadVREntity as MadVREntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_HDR_FLAG: str
_OUTGOING_HDR_FLAG: str
_POWER_STATE: str
_SIGNAL_STATE: str

@dataclass(frozen=True, kw_only=True)
class MadvrBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[MadVRCoordinator], bool]

BINARY_SENSORS: tuple[MadvrBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: MadVRConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MadvrBinarySensor(MadVREntity, BinarySensorEntity):
    entity_description: MadvrBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: MadVRCoordinator, description: MadvrBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
