from . import YaleConfigEntry as YaleConfigEntry
from .entity import YaleEntity as YaleEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.const import UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

async def async_setup_entry(hass: HomeAssistant, entry: YaleConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class YaleTemperatureSensor(YaleEntity, SensorEntity):
    _attr_device_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    @property
    def native_value(self) -> StateType: ...
