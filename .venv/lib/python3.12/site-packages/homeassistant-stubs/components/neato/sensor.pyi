from .const import NEATO_LOGIN as NEATO_LOGIN, NEATO_ROBOTS as NEATO_ROBOTS, SCAN_INTERVAL_MINUTES as SCAN_INTERVAL_MINUTES
from .entity import NeatoEntity as NeatoEntity
from .hub import NeatoHub as NeatoHub
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pybotvac.robot import Robot as Robot
from typing import Any

_LOGGER: Incomplete
SCAN_INTERVAL: Incomplete
BATTERY: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NeatoSensor(NeatoEntity, SensorEntity):
    _attr_device_class: Incomplete
    _attr_entity_category: Incomplete
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_available: bool
    _robot_serial: str
    _attr_unique_id: Incomplete
    _state: dict[str, Any] | None
    def __init__(self, neato: NeatoHub, robot: Robot) -> None: ...
    def update(self) -> None: ...
    @property
    def native_value(self) -> str | None: ...
