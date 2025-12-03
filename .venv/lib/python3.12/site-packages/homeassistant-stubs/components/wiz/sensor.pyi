from . import WizConfigEntry as WizConfigEntry
from .entity import WizEntity as WizEntity
from .models import WizData as WizData
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

SENSORS: tuple[SensorEntityDescription, ...]
POWER_SENSORS: tuple[SensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: WizConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WizSensor(WizEntity, SensorEntity):
    entity_description: SensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, wiz_data: WizData, name: str, description: SensorEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...

class WizPowerSensor(WizSensor):
    _attr_native_value: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...
