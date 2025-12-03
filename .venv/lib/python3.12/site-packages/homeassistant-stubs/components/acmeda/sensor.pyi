from . import AcmedaConfigEntry as AcmedaConfigEntry
from .const import ACMEDA_HUB_UPDATE as ACMEDA_HUB_UPDATE
from .entity import AcmedaEntity as AcmedaEntity
from .helpers import async_add_acmeda_entities as async_add_acmeda_entities
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.const import PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, config_entry: AcmedaConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AcmedaBattery(AcmedaEntity, SensorEntity):
    _attr_device_class: Incomplete
    _attr_native_unit_of_measurement = PERCENTAGE
    @property
    def native_value(self) -> float | int | None: ...
