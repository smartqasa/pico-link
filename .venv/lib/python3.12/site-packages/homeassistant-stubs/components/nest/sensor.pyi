from .device_info import NestDeviceInfo as NestDeviceInfo
from .types import NestConfigEntry as NestConfigEntry
from _typeshed import Incomplete
from google_nest_sdm.device import Device as Device
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.const import PERCENTAGE as PERCENTAGE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_LOGGER: Incomplete
DEVICE_TYPE_MAP: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: NestConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SensorBase(SensorEntity):
    _attr_should_poll: bool
    _attr_state_class: Incomplete
    _attr_has_entity_name: bool
    _device: Incomplete
    _device_info: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, device: Device) -> None: ...
    @property
    def available(self) -> bool: ...
    async def async_added_to_hass(self) -> None: ...

class TemperatureSensor(SensorBase):
    _attr_device_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    @property
    def native_value(self) -> float: ...

class HumiditySensor(SensorBase):
    _attr_device_class: Incomplete
    _attr_native_unit_of_measurement = PERCENTAGE
    @property
    def native_value(self) -> int: ...
