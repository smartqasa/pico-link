from . import SimpliSafe as SimpliSafe
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from .entity import SimpliSafeEntity as SimpliSafeEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from simplipy.device.sensor.v3 import SensorV3 as SensorV3
from simplipy.system.v3 import SystemV3 as SystemV3

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SimplisafeFreezeSensor(SimpliSafeEntity, SensorEntity):
    _attr_device_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_state_class: Incomplete
    _device: SensorV3
    def __init__(self, simplisafe: SimpliSafe, system: SystemV3, sensor: SensorV3) -> None: ...
    _attr_native_value: Incomplete
    @callback
    def async_update_from_rest_api(self) -> None: ...
