from . import IronOSConfigEntry as IronOSConfigEntry
from .const import DOMAIN as DOMAIN, MAX_TEMP as MAX_TEMP, MIN_TEMP as MIN_TEMP
from .coordinator import IronOSCoordinators as IronOSCoordinators
from .entity import IronOSBaseEntity as IronOSBaseEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from enum import StrEnum
from homeassistant.components.number import DEFAULT_MAX_VALUE as DEFAULT_MAX_VALUE, NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription, NumberMode as NumberMode
from homeassistant.const import EntityCategory as EntityCategory, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfPower as UnitOfPower, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pynecil import CharSetting, LiveDataResponse as LiveDataResponse, SettingsDataResponse as SettingsDataResponse

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class IronOSNumberEntityDescription(NumberEntityDescription):
    value_fn: Callable[[LiveDataResponse, SettingsDataResponse], float | int | None]
    max_value_fn: Callable[[LiveDataResponse], float | int] | None = ...
    characteristic: CharSetting
    raw_value_fn: Callable[[float], float | int] | None = ...

class PinecilNumber(StrEnum):
    SETPOINT_TEMP = 'setpoint_temperature'
    SLEEP_TEMP = 'sleep_temperature'
    SLEEP_TIMEOUT = 'sleep_timeout'
    QC_MAX_VOLTAGE = 'qc_max_voltage'
    PD_TIMEOUT = 'pd_timeout'
    BOOST_TEMP = 'boost_temp'
    SHUTDOWN_TIMEOUT = 'shutdown_timeout'
    DISPLAY_BRIGHTNESS = 'display_brightness'
    POWER_LIMIT = 'power_limit'
    CALIBRATION_OFFSET = 'calibration_offset'
    HALL_SENSITIVITY = 'hall_sensitivity'
    MIN_VOLTAGE_PER_CELL = 'min_voltage_per_cell'
    ACCEL_SENSITIVITY = 'accel_sensitivity'
    KEEP_AWAKE_PULSE_POWER = 'keep_awake_pulse_power'
    KEEP_AWAKE_PULSE_DELAY = 'keep_awake_pulse_delay'
    KEEP_AWAKE_PULSE_DURATION = 'keep_awake_pulse_duration'
    VOLTAGE_DIV = 'voltage_div'
    TEMP_INCREMENT_SHORT = 'temp_increment_short'
    TEMP_INCREMENT_LONG = 'temp_increment_long'

def multiply(value: float | None, multiplier: float) -> float | None: ...

PINECIL_NUMBER_DESCRIPTIONS: tuple[IronOSNumberEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: IronOSConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class IronOSNumberEntity(IronOSBaseEntity, NumberEntity):
    entity_description: IronOSNumberEntityDescription
    settings: Incomplete
    def __init__(self, coordinators: IronOSCoordinators, entity_description: IronOSNumberEntityDescription) -> None: ...
    async def async_set_native_value(self, value: float) -> None: ...
    @property
    def native_value(self) -> float | int | None: ...
    @property
    def native_max_value(self) -> float: ...
    async def async_added_to_hass(self) -> None: ...
