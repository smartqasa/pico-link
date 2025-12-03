from . import IronOSConfigEntry as IronOSConfigEntry
from .const import OHM as OHM
from .coordinator import IronOSLiveDataCoordinator as IronOSLiveDataCoordinator
from .entity import IronOSBaseEntity as IronOSBaseEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from enum import StrEnum
from homeassistant.components.sensor import EntityCategory as EntityCategory, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import PERCENTAGE as PERCENTAGE, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfPower as UnitOfPower, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from pynecil import LiveDataResponse as LiveDataResponse

PARALLEL_UPDATES: int

class PinecilSensor(StrEnum):
    LIVE_TEMP = 'live_temperature'
    SETPOINT_TEMP = 'setpoint_temperature'
    DC_VOLTAGE = 'voltage'
    HANDLETEMP = 'handle_temperature'
    PWMLEVEL = 'power_pwm_level'
    POWER_SRC = 'power_source'
    TIP_RESISTANCE = 'tip_resistance'
    UPTIME = 'uptime'
    MOVEMENT_TIME = 'movement_time'
    MAX_TIP_TEMP_ABILITY = 'max_tip_temp_ability'
    TIP_VOLTAGE = 'tip_voltage'
    HALL_SENSOR = 'hall_sensor'
    OPERATING_MODE = 'operating_mode'
    ESTIMATED_POWER = 'estimated_power'

@dataclass(frozen=True, kw_only=True)
class IronOSSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[LiveDataResponse, bool], StateType]

PINECIL_SENSOR_DESCRIPTIONS: tuple[IronOSSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: IronOSConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class IronOSSensorEntity(IronOSBaseEntity, SensorEntity):
    entity_description: IronOSSensorEntityDescription
    coordinator: IronOSLiveDataCoordinator
    @property
    def native_value(self) -> StateType: ...
