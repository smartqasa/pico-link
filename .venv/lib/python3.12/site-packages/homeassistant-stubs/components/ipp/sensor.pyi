from . import IPPConfigEntry as IPPConfigEntry
from .const import ATTR_COMMAND_SET as ATTR_COMMAND_SET, ATTR_INFO as ATTR_INFO, ATTR_MARKER_HIGH_LEVEL as ATTR_MARKER_HIGH_LEVEL, ATTR_MARKER_LOW_LEVEL as ATTR_MARKER_LOW_LEVEL, ATTR_MARKER_TYPE as ATTR_MARKER_TYPE, ATTR_SERIAL as ATTR_SERIAL, ATTR_STATE_MESSAGE as ATTR_STATE_MESSAGE, ATTR_STATE_REASON as ATTR_STATE_REASON, ATTR_URI_SUPPORTED as ATTR_URI_SUPPORTED
from .entity import IPPEntity as IPPEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import ATTR_LOCATION as ATTR_LOCATION, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from pyipp import Marker as Marker, Printer as Printer
from typing import Any

@dataclass(frozen=True, kw_only=True)
class IPPSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Printer], StateType | datetime]
    attributes_fn: Callable[[Printer], dict[Any, StateType]] = ...

def _get_marker_attributes_fn(marker_index: int, attributes_fn: Callable[[Marker], dict[Any, StateType]]) -> Callable[[Printer], dict[Any, StateType]]: ...
def _get_marker_value_fn(marker_index: int, value_fn: Callable[[Marker], StateType | datetime]) -> Callable[[Printer], StateType | datetime]: ...

PRINTER_SENSORS: tuple[IPPSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: IPPConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class IPPSensor(IPPEntity, SensorEntity):
    entity_description: IPPSensorEntityDescription
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def native_value(self) -> StateType | datetime: ...
