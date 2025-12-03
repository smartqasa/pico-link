from . import VelbusConfigEntry as VelbusConfigEntry
from .entity import VelbusEntity as VelbusEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from velbusaio.channels import ButtonCounter as ButtonCounter, LightSensor as LightSensor, SensorNumber as SensorNumber, Temperature as Temperature

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: VelbusConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class VelbusSensor(VelbusEntity, SensorEntity):
    _channel: ButtonCounter | Temperature | LightSensor | SensorNumber
    _is_counter: bool
    _attr_device_class: Incomplete
    _attr_icon: str
    _attr_name: Incomplete
    _attr_state_class: Incomplete
    _attr_unique_id: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    def __init__(self, channel: ButtonCounter | Temperature | LightSensor | SensorNumber, counter: bool = False) -> None: ...
    @property
    def native_value(self) -> float | int | None: ...
