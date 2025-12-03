from . import AirNowConfigEntry as AirNowConfigEntry, AirNowDataUpdateCoordinator as AirNowDataUpdateCoordinator
from .const import ATTR_API_AQI as ATTR_API_AQI, ATTR_API_AQI_DESCRIPTION as ATTR_API_AQI_DESCRIPTION, ATTR_API_AQI_LEVEL as ATTR_API_AQI_LEVEL, ATTR_API_O3 as ATTR_API_O3, ATTR_API_PM10 as ATTR_API_PM10, ATTR_API_PM25 as ATTR_API_PM25, ATTR_API_REPORT_DATE as ATTR_API_REPORT_DATE, ATTR_API_REPORT_HOUR as ATTR_API_REPORT_HOUR, ATTR_API_REPORT_TZ as ATTR_API_REPORT_TZ, ATTR_API_STATION as ATTR_API_STATION, ATTR_API_STATION_LATITUDE as ATTR_API_STATION_LATITUDE, ATTR_API_STATION_LONGITUDE as ATTR_API_STATION_LONGITUDE, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN, US_TZ_OFFSETS as US_TZ_OFFSETS
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import ATTR_TIME as ATTR_TIME, CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

ATTRIBUTION: str
PARALLEL_UPDATES: int
ATTR_DESCR: str
ATTR_LEVEL: str
ATTR_STATION: str

@dataclass(frozen=True, kw_only=True)
class AirNowEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Any], StateType]
    extra_state_attributes_fn: Callable[[Any], dict[str, str]] | None

def station_extra_attrs(data: dict[str, Any]) -> dict[str, Any]: ...
def aqi_extra_attrs(data: dict[str, Any]) -> dict[str, Any]: ...

SENSOR_TYPES: tuple[AirNowEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: AirNowConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AirNowSensor(CoordinatorEntity[AirNowDataUpdateCoordinator], SensorEntity):
    _attr_attribution = ATTRIBUTION
    _attr_has_entity_name: bool
    entity_description: AirNowEntityDescription
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: AirNowDataUpdateCoordinator, description: AirNowEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def extra_state_attributes(self) -> dict[str, str] | None: ...
