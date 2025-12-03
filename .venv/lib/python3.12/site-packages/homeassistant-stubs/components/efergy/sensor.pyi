from . import EfergyConfigEntry as EfergyConfigEntry
from .const import CONF_CURRENT_VALUES as CONF_CURRENT_VALUES, LOGGER as LOGGER
from .entity import EfergyEntity as EfergyEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from pyefergy import Efergy as Efergy

SENSOR_TYPES: tuple[SensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: EfergyConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EfergySensor(EfergyEntity, SensorEntity):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_translation_placeholders: Incomplete
    _attr_unique_id: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    sid: Incomplete
    period: Incomplete
    def __init__(self, api: Efergy, description: SensorEntityDescription, server_unique_id: str, period: str | None = None, currency: str | None = None, sid: int | None = None) -> None: ...
    _attr_native_value: Incomplete
    _attr_available: bool
    async def async_update(self) -> None: ...
