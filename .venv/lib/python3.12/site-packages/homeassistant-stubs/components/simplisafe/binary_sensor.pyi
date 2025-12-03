from . import SimpliSafe as SimpliSafe
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from .entity import SimpliSafeEntity as SimpliSafeEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from simplipy.device import DeviceV3 as DeviceV3
from simplipy.device.sensor.v3 import SensorV3 as SensorV3
from simplipy.system.v3 import SystemV3 as SystemV3

SUPPORTED_BATTERY_SENSOR_TYPES: Incomplete
TRIGGERED_SENSOR_TYPES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TriggeredBinarySensor(SimpliSafeEntity, BinarySensorEntity):
    _attr_device_class: Incomplete
    _device: SensorV3
    def __init__(self, simplisafe: SimpliSafe, system: SystemV3, sensor: SensorV3, device_class: BinarySensorDeviceClass) -> None: ...
    _attr_is_on: Incomplete
    @callback
    def async_update_from_rest_api(self) -> None: ...

class BatteryBinarySensor(SimpliSafeEntity, BinarySensorEntity):
    _attr_device_class: Incomplete
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    _device: DeviceV3
    def __init__(self, simplisafe: SimpliSafe, system: SystemV3, device: DeviceV3) -> None: ...
    _attr_is_on: Incomplete
    @callback
    def async_update_from_rest_api(self) -> None: ...
