from .const import ATTR_DARK as ATTR_DARK, ATTR_ON as ATTR_ON
from .entity import DeconzDevice as DeconzDevice
from .hub import DeconzHub as DeconzHub
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription, DOMAIN as BINARY_SENSOR_DOMAIN
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pydeconz.interfaces.sensors import SensorResources
from pydeconz.models.event import EventType as EventType
from pydeconz.models.sensor import SensorBase as PydeconzSensorBase
from pydeconz.models.sensor.alarm import Alarm
from pydeconz.models.sensor.carbon_monoxide import CarbonMonoxide
from pydeconz.models.sensor.fire import Fire
from pydeconz.models.sensor.generic_flag import GenericFlag
from pydeconz.models.sensor.open_close import OpenClose
from pydeconz.models.sensor.presence import Presence
from pydeconz.models.sensor.vibration import Vibration
from pydeconz.models.sensor.water import Water

ATTR_ORIENTATION: str
ATTR_TILTANGLE: str
ATTR_VIBRATIONSTRENGTH: str
PROVIDES_EXTRA_ATTRIBUTES: Incomplete

@dataclass(frozen=True, kw_only=True)
class DeconzBinarySensorDescription[_T: (Alarm, CarbonMonoxide, Fire, GenericFlag, OpenClose, Presence, Vibration, Water, PydeconzSensorBase)](BinarySensorEntityDescription):
    instance_check: type[_T] | None = ...
    name_suffix: str = ...
    old_unique_id_suffix: str = ...
    update_key: str
    value_fn: Callable[[_T], bool | None]

ENTITY_DESCRIPTIONS: tuple[DeconzBinarySensorDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DeconzBinarySensor(DeconzDevice[SensorResources], BinarySensorEntity):
    TYPE = BINARY_SENSOR_DOMAIN
    entity_description: DeconzBinarySensorDescription
    unique_id_suffix: Incomplete
    _update_key: Incomplete
    _name_suffix: Incomplete
    def __init__(self, device: SensorResources, hub: DeconzHub, description: DeconzBinarySensorDescription) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, bool | float | int | list | None]: ...
