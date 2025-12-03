from .const import API_CO2 as API_CO2, API_DUST as API_DUST, API_HUMID as API_HUMID, API_LUX as API_LUX, API_PM10 as API_PM10, API_PM25 as API_PM25, API_SCORE as API_SCORE, API_SPL_A as API_SPL_A, API_TEMP as API_TEMP, API_VOC as API_VOC, ATTRIBUTION as ATTRIBUTION, DOMAIN as DOMAIN
from .coordinator import AwairConfigEntry as AwairConfigEntry, AwairDataUpdateCoordinator as AwairDataUpdateCoordinator
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_CONNECTIONS as ATTR_CONNECTIONS, ATTR_SW_VERSION as ATTR_SW_VERSION, CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONCENTRATION_PARTS_PER_BILLION as CONCENTRATION_PARTS_PER_BILLION, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, UnitOfSoundPressure as UnitOfSoundPressure, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from python_awair.air_data import AirData as AirData
from python_awair.devices import AwairBaseDevice as AwairBaseDevice
from typing import Any

DUST_ALIASES: Incomplete

@dataclass(frozen=True, kw_only=True)
class AwairSensorEntityDescription(SensorEntityDescription):
    unique_id_tag: str

SENSOR_TYPE_SCORE: Incomplete
SENSOR_TYPES: tuple[AwairSensorEntityDescription, ...]
SENSOR_TYPES_DUST: tuple[AwairSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: AwairConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AwairSensor(CoordinatorEntity[AwairDataUpdateCoordinator], SensorEntity):
    entity_description: AwairSensorEntityDescription
    _attr_has_entity_name: bool
    _attr_attribution = ATTRIBUTION
    _device: Incomplete
    def __init__(self, device: AwairBaseDevice, coordinator: AwairDataUpdateCoordinator, description: AwairSensorEntityDescription) -> None: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def available(self) -> bool: ...
    @property
    def native_value(self) -> float | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def _air_data(self) -> AirData | None: ...
