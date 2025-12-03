import datetime
from .const import DOMAIN as DOMAIN
from .coordinator import EnphaseConfigEntry as EnphaseConfigEntry, EnphaseUpdateCoordinator as EnphaseUpdateCoordinator
from .entity import EnvoyBaseEntity as EnvoyBaseEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import PERCENTAGE as PERCENTAGE, UnitOfApparentPower as UnitOfApparentPower, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfFrequency as UnitOfFrequency, UnitOfPower as UnitOfPower, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyenphase import EnvoyACBPower as EnvoyACBPower, EnvoyBatteryAggregate as EnvoyBatteryAggregate, EnvoyEncharge as EnvoyEncharge, EnvoyEnchargeAggregate as EnvoyEnchargeAggregate, EnvoyEnchargePower as EnvoyEnchargePower, EnvoyEnpower as EnvoyEnpower, EnvoyInverter as EnvoyInverter, EnvoySystemConsumption as EnvoySystemConsumption, EnvoySystemProduction as EnvoySystemProduction
from pyenphase.models.meters import CtMeterStatus, CtState as CtState, CtStatusFlags as CtStatusFlags, CtType, EnvoyMeterData as EnvoyMeterData

ICON: str
_LOGGER: Incomplete
INVERTERS_KEY: str
LAST_REPORTED_KEY: str
PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class EnvoyInverterSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[EnvoyInverter], datetime.datetime | float]

INVERTER_SENSORS: Incomplete

@dataclass(frozen=True, kw_only=True)
class EnvoyProductionSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[EnvoySystemProduction], int]
    on_phase: str | None

PRODUCTION_SENSORS: Incomplete
PRODUCTION_PHASE_SENSORS: Incomplete

@dataclass(frozen=True, kw_only=True)
class EnvoyConsumptionSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[EnvoySystemConsumption], int]
    on_phase: str | None

CONSUMPTION_SENSORS: Incomplete
CONSUMPTION_PHASE_SENSORS: Incomplete
NET_CONSUMPTION_SENSORS: Incomplete
NET_CONSUMPTION_PHASE_SENSORS: Incomplete

@dataclass(frozen=True, kw_only=True)
class EnvoyCTSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[EnvoyMeterData], int | float | str | CtType | CtMeterStatus | CtStatusFlags | CtState | None]
    on_phase: str | None

CT_NET_CONSUMPTION_SENSORS: Incomplete
CT_NET_CONSUMPTION_PHASE_SENSORS: Incomplete
CT_PRODUCTION_SENSORS: Incomplete
CT_PRODUCTION_PHASE_SENSORS: Incomplete
CT_STORAGE_SENSORS: Incomplete
CT_STORAGE_PHASE_SENSORS: Incomplete

@dataclass(frozen=True, kw_only=True)
class EnvoyEnchargeSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[EnvoyEncharge], datetime.datetime | int | float]

@dataclass(frozen=True)
class EnvoyEnchargePowerRequiredKeysMixin: ...

@dataclass(frozen=True, kw_only=True)
class EnvoyEnchargePowerSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[EnvoyEnchargePower], int | float]

ENCHARGE_INVENTORY_SENSORS: Incomplete
ENCHARGE_POWER_SENSORS: Incomplete

@dataclass(frozen=True, kw_only=True)
class EnvoyEnpowerSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[EnvoyEnpower], datetime.datetime | int | float]

ENPOWER_SENSORS: Incomplete

@dataclass(frozen=True)
class EnvoyEnchargeAggregateRequiredKeysMixin: ...

@dataclass(frozen=True, kw_only=True)
class EnvoyEnchargeAggregateSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[EnvoyEnchargeAggregate], int]

ENCHARGE_AGGREGATE_SENSORS: Incomplete

@dataclass(frozen=True, kw_only=True)
class EnvoyAcbBatterySensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[EnvoyACBPower], int | str]

ACB_BATTERY_POWER_SENSORS: Incomplete
ACB_BATTERY_ENERGY_SENSORS: Incomplete

@dataclass(frozen=True, kw_only=True)
class EnvoyAggregateBatterySensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[EnvoyBatteryAggregate], int]

AGGREGATE_BATTERY_SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: EnphaseConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EnvoySensorBaseEntity(EnvoyBaseEntity, SensorEntity): ...

class EnvoySystemSensorEntity(EnvoySensorBaseEntity):
    _attr_icon = ICON
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: EnphaseUpdateCoordinator, description: SensorEntityDescription) -> None: ...

class EnvoyProductionEntity(EnvoySystemSensorEntity):
    entity_description: EnvoyProductionSensorEntityDescription
    @property
    def native_value(self) -> int | None: ...

class EnvoyConsumptionEntity(EnvoySystemSensorEntity):
    entity_description: EnvoyConsumptionSensorEntityDescription
    @property
    def native_value(self) -> int | None: ...

class EnvoyNetConsumptionEntity(EnvoySystemSensorEntity):
    entity_description: EnvoyConsumptionSensorEntityDescription
    @property
    def native_value(self) -> int | None: ...

class EnvoyProductionPhaseEntity(EnvoySystemSensorEntity):
    entity_description: EnvoyProductionSensorEntityDescription
    @property
    def native_value(self) -> int | None: ...

class EnvoyConsumptionPhaseEntity(EnvoySystemSensorEntity):
    entity_description: EnvoyConsumptionSensorEntityDescription
    @property
    def native_value(self) -> int | None: ...

class EnvoyNetConsumptionPhaseEntity(EnvoySystemSensorEntity):
    entity_description: EnvoyConsumptionSensorEntityDescription
    @property
    def native_value(self) -> int | None: ...

class EnvoyConsumptionCTEntity(EnvoySystemSensorEntity):
    entity_description: EnvoyCTSensorEntityDescription
    @property
    def native_value(self) -> int | float | str | CtType | CtMeterStatus | CtStatusFlags | None: ...

class EnvoyConsumptionCTPhaseEntity(EnvoySystemSensorEntity):
    entity_description: EnvoyCTSensorEntityDescription
    @property
    def native_value(self) -> int | float | str | CtType | CtMeterStatus | CtStatusFlags | None: ...

class EnvoyProductionCTEntity(EnvoySystemSensorEntity):
    entity_description: EnvoyCTSensorEntityDescription
    @property
    def native_value(self) -> int | float | str | CtType | CtMeterStatus | CtStatusFlags | None: ...

class EnvoyProductionCTPhaseEntity(EnvoySystemSensorEntity):
    entity_description: EnvoyCTSensorEntityDescription
    @property
    def native_value(self) -> int | float | str | CtType | CtMeterStatus | CtStatusFlags | None: ...

class EnvoyStorageCTEntity(EnvoySystemSensorEntity):
    entity_description: EnvoyCTSensorEntityDescription
    @property
    def native_value(self) -> int | float | str | CtType | CtMeterStatus | CtStatusFlags | None: ...

class EnvoyStorageCTPhaseEntity(EnvoySystemSensorEntity):
    entity_description: EnvoyCTSensorEntityDescription
    @property
    def native_value(self) -> int | float | str | CtType | CtMeterStatus | CtStatusFlags | None: ...

class EnvoyInverterEntity(EnvoySensorBaseEntity):
    _attr_icon = ICON
    entity_description: EnvoyInverterSensorEntityDescription
    _serial_number: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: EnphaseUpdateCoordinator, description: EnvoyInverterSensorEntityDescription, serial_number: str) -> None: ...
    @property
    def native_value(self) -> datetime.datetime | float | None: ...

class EnvoyEnchargeEntity(EnvoySensorBaseEntity):
    _serial_number: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: EnphaseUpdateCoordinator, description: EnvoyEnchargeSensorEntityDescription | EnvoyEnchargePowerSensorEntityDescription, serial_number: str) -> None: ...

class EnvoyEnchargeInventoryEntity(EnvoyEnchargeEntity):
    entity_description: EnvoyEnchargeSensorEntityDescription
    @property
    def native_value(self) -> int | float | datetime.datetime | None: ...

class EnvoyEnchargePowerEntity(EnvoyEnchargeEntity):
    entity_description: EnvoyEnchargePowerSensorEntityDescription
    @property
    def native_value(self) -> int | float | None: ...

class EnvoyEnchargeAggregateEntity(EnvoySystemSensorEntity):
    entity_description: EnvoyEnchargeAggregateSensorEntityDescription
    @property
    def native_value(self) -> int: ...

class EnvoyEnpowerEntity(EnvoySensorBaseEntity):
    entity_description: EnvoyEnpowerSensorEntityDescription
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: EnphaseUpdateCoordinator, description: EnvoyEnpowerSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> datetime.datetime | int | float | None: ...

class EnvoyAcbBatteryPowerEntity(EnvoySensorBaseEntity):
    entity_description: EnvoyAcbBatterySensorEntityDescription
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: EnphaseUpdateCoordinator, description: EnvoyAcbBatterySensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> int | str | None: ...

class EnvoyAcbBatteryEnergyEntity(EnvoySystemSensorEntity):
    entity_description: EnvoyAcbBatterySensorEntityDescription
    @property
    def native_value(self) -> int | str: ...

class AggregateBatteryEntity(EnvoySystemSensorEntity):
    entity_description: EnvoyAggregateBatterySensorEntityDescription
    @property
    def native_value(self) -> int: ...
