from . import BlueCurrentConfigEntry as BlueCurrentConfigEntry, Connector as Connector
from .const import DOMAIN as DOMAIN
from .entity import BlueCurrentEntity as BlueCurrentEntity, ChargepointEntity as ChargepointEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CURRENCY_EURO as CURRENCY_EURO, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

SENSORS: Incomplete
TIMESTAMP_SENSORS: Incomplete
GRID_SENSORS: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: BlueCurrentConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ChargePointSensor(ChargepointEntity, SensorEntity):
    key: Incomplete
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, connector: Connector, sensor: SensorEntityDescription, evse_id: str) -> None: ...
    has_value: bool
    _attr_native_value: Incomplete
    @callback
    def update_from_latest_data(self) -> None: ...

class ChargePointTimestampSensor(ChargePointSensor):
    _attr_device_class: Incomplete
    has_value: bool
    _attr_native_value: Incomplete
    @callback
    def update_from_latest_data(self) -> None: ...

class GridSensor(BlueCurrentEntity, SensorEntity):
    key: Incomplete
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, connector: Connector, sensor: SensorEntityDescription) -> None: ...
    has_value: bool
    _attr_native_value: Incomplete
    @callback
    def update_from_latest_data(self) -> None: ...
