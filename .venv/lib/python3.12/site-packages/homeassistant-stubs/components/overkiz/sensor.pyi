from . import OverkizDataConfigEntry as OverkizDataConfigEntry
from .const import DOMAIN as DOMAIN, IGNORED_OVERKIZ_DEVICES as IGNORED_OVERKIZ_DEVICES, OVERKIZ_STATE_TO_TRANSLATION as OVERKIZ_STATE_TO_TRANSLATION, OVERKIZ_UNIT_TO_HA as OVERKIZ_UNIT_TO_HA
from .coordinator import OverkizDataUpdateCoordinator as OverkizDataUpdateCoordinator
from .entity import OverkizDescriptiveEntity as OverkizDescriptiveEntity, OverkizEntity as OverkizEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, EntityCategory as EntityCategory, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS as SIGNAL_STRENGTH_DECIBELS, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime, UnitOfVolume as UnitOfVolume, UnitOfVolumeFlowRate as UnitOfVolumeFlowRate
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from pyoverkiz.types import StateType as OverkizStateType

@dataclass(frozen=True)
class OverkizSensorDescription(SensorEntityDescription):
    native_value: Callable[[OverkizStateType], StateType] | None = ...

SENSOR_DESCRIPTIONS: list[OverkizSensorDescription]
SUPPORTED_STATES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: OverkizDataConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OverkizStateSensor(OverkizDescriptiveEntity, SensorEntity):
    entity_description: OverkizSensorDescription
    @property
    def native_value(self) -> StateType: ...
    @property
    def native_unit_of_measurement(self) -> str | None: ...

class OverkizHomeKitSetupCodeSensor(OverkizEntity, SensorEntity):
    _attr_icon: str
    _attr_entity_category: Incomplete
    _attr_name: str
    def __init__(self, device_url: str, coordinator: OverkizDataUpdateCoordinator) -> None: ...
    @property
    def native_value(self) -> str | None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
