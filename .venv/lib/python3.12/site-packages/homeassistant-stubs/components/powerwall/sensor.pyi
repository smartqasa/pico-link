from .const import POWERWALL_COORDINATOR as POWERWALL_COORDINATOR
from .entity import BatteryEntity as BatteryEntity, PowerWallEntity as PowerWallEntity
from .models import BatteryResponse as BatteryResponse, PowerwallConfigEntry as PowerwallConfigEntry, PowerwallRuntimeData as PowerwallRuntimeData
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfFrequency as UnitOfFrequency, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from tesla_powerwall import MeterResponse, MeterType as MeterType

_METER_DIRECTION_EXPORT: str
_METER_DIRECTION_IMPORT: str
type _ValueType = float | int | str | None

@dataclass(frozen=True, kw_only=True)
class PowerwallSensorEntityDescription[_ValueParamT, _ValueT: _ValueType](SensorEntityDescription):
    value_fn: Callable[[_ValueParamT], _ValueT]

def _get_meter_power(meter: MeterResponse) -> float: ...
def _get_meter_frequency(meter: MeterResponse) -> float: ...
def _get_meter_average_voltage(meter: MeterResponse) -> float: ...

POWERWALL_INSTANT_SENSORS: Incomplete

def _get_instant_voltage(battery: BatteryResponse) -> float | None: ...
def _get_instant_frequency(battery: BatteryResponse) -> float | None: ...
def _get_instant_current(battery: BatteryResponse) -> float | None: ...

BATTERY_INSTANT_SENSORS: list[PowerwallSensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: PowerwallConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PowerWallChargeSensor(PowerWallEntity, SensorEntity):
    _attr_translation_key: str
    _attr_state_class: Incomplete
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_device_class: Incomplete
    @property
    def unique_id(self) -> str: ...
    @property
    def native_value(self) -> int: ...

class PowerWallEnergySensor(PowerWallEntity, SensorEntity):
    entity_description: PowerwallSensorEntityDescription[MeterResponse, float]
    _meter: Incomplete
    _attr_translation_key: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, powerwall_data: PowerwallRuntimeData, meter: MeterType, description: PowerwallSensorEntityDescription[MeterResponse, float]) -> None: ...
    @property
    def native_value(self) -> float | None: ...

class PowerWallBackupReserveSensor(PowerWallEntity, SensorEntity):
    _attr_translation_key: str
    _attr_state_class: Incomplete
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_device_class: Incomplete
    @property
    def unique_id(self) -> str: ...
    @property
    def native_value(self) -> int | None: ...

class PowerWallEnergyDirectionSensor(PowerWallEntity, SensorEntity):
    _attr_state_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_device_class: Incomplete
    _meter: Incomplete
    _attr_translation_key: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, powerwall_data: PowerwallRuntimeData, meter: MeterType, meter_direction: str) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def meter(self) -> MeterResponse | None: ...

class PowerWallExportSensor(PowerWallEnergyDirectionSensor):
    def __init__(self, powerwall_data: PowerwallRuntimeData, meter: MeterType) -> None: ...
    @property
    def native_value(self) -> float | None: ...

class PowerWallImportSensor(PowerWallEnergyDirectionSensor):
    def __init__(self, powerwall_data: PowerwallRuntimeData, meter: MeterType) -> None: ...
    @property
    def native_value(self) -> float | None: ...

class PowerWallBatterySensor[_ValueT: _ValueType](BatteryEntity, SensorEntity):
    entity_description: PowerwallSensorEntityDescription[BatteryResponse, _ValueT]
    _attr_translation_key: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, powerwall_data: PowerwallRuntimeData, battery: BatteryResponse, description: PowerwallSensorEntityDescription[BatteryResponse, _ValueT]) -> None: ...
    @property
    def native_value(self) -> float | int | str | None: ...
