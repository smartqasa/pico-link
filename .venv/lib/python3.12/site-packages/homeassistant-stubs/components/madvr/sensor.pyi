from . import MadVRConfigEntry as MadVRConfigEntry
from .const import ASPECT_DEC as ASPECT_DEC, ASPECT_INT as ASPECT_INT, ASPECT_NAME as ASPECT_NAME, ASPECT_RES as ASPECT_RES, INCOMING_ASPECT_RATIO as INCOMING_ASPECT_RATIO, INCOMING_BIT_DEPTH as INCOMING_BIT_DEPTH, INCOMING_BLACK_LEVELS as INCOMING_BLACK_LEVELS, INCOMING_COLORIMETRY as INCOMING_COLORIMETRY, INCOMING_COLOR_SPACE as INCOMING_COLOR_SPACE, INCOMING_FRAME_RATE as INCOMING_FRAME_RATE, INCOMING_RES as INCOMING_RES, INCOMING_SIGNAL_TYPE as INCOMING_SIGNAL_TYPE, MASKING_DEC as MASKING_DEC, MASKING_INT as MASKING_INT, MASKING_RES as MASKING_RES, OUTGOING_BIT_DEPTH as OUTGOING_BIT_DEPTH, OUTGOING_BLACK_LEVELS as OUTGOING_BLACK_LEVELS, OUTGOING_COLORIMETRY as OUTGOING_COLORIMETRY, OUTGOING_COLOR_SPACE as OUTGOING_COLOR_SPACE, OUTGOING_FRAME_RATE as OUTGOING_FRAME_RATE, OUTGOING_RES as OUTGOING_RES, OUTGOING_SIGNAL_TYPE as OUTGOING_SIGNAL_TYPE, TEMP_CPU as TEMP_CPU, TEMP_GPU as TEMP_GPU, TEMP_HDMI as TEMP_HDMI, TEMP_MAINBOARD as TEMP_MAINBOARD
from .coordinator import MadVRCoordinator as MadVRCoordinator
from .entity import MadVREntity as MadVREntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

def is_valid_temperature(value: float | None) -> bool: ...
def get_temperature(coordinator: MadVRCoordinator, key: str) -> float | None: ...

@dataclass(frozen=True, kw_only=True)
class MadvrSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[MadVRCoordinator], StateType]

SENSORS: tuple[MadvrSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: MadVRConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MadvrSensor(MadVREntity, SensorEntity):
    entity_description: MadvrSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: MadVRCoordinator, description: MadvrSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> float | str | None: ...
