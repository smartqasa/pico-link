from . import AirlyConfigEntry as AirlyConfigEntry, AirlyDataUpdateCoordinator as AirlyDataUpdateCoordinator
from .const import ATTRIBUTION as ATTRIBUTION, ATTR_ADVICE as ATTR_ADVICE, ATTR_API_ADVICE as ATTR_API_ADVICE, ATTR_API_CAQI as ATTR_API_CAQI, ATTR_API_CAQI_DESCRIPTION as ATTR_API_CAQI_DESCRIPTION, ATTR_API_CAQI_LEVEL as ATTR_API_CAQI_LEVEL, ATTR_API_CO as ATTR_API_CO, ATTR_API_HUMIDITY as ATTR_API_HUMIDITY, ATTR_API_NO2 as ATTR_API_NO2, ATTR_API_O3 as ATTR_API_O3, ATTR_API_PM1 as ATTR_API_PM1, ATTR_API_PM10 as ATTR_API_PM10, ATTR_API_PM25 as ATTR_API_PM25, ATTR_API_PRESSURE as ATTR_API_PRESSURE, ATTR_API_SO2 as ATTR_API_SO2, ATTR_API_TEMPERATURE as ATTR_API_TEMPERATURE, ATTR_DESCRIPTION as ATTR_DESCRIPTION, ATTR_LEVEL as ATTR_LEVEL, ATTR_LIMIT as ATTR_LIMIT, ATTR_PERCENT as ATTR_PERCENT, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, SUFFIX_LIMIT as SUFFIX_LIMIT, SUFFIX_PERCENT as SUFFIX_PERCENT, URL as URL
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONF_NAME as CONF_NAME, PERCENTAGE as PERCENTAGE, UnitOfPressure as UnitOfPressure, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True)
class AirlySensorEntityDescription(SensorEntityDescription):
    attrs: Callable[[dict[str, Any]], dict[str, Any]] = ...

SENSOR_TYPES: tuple[AirlySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: AirlyConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AirlySensor(CoordinatorEntity[AirlyDataUpdateCoordinator], SensorEntity):
    _attr_attribution = ATTRIBUTION
    _attr_has_entity_name: bool
    entity_description: AirlySensorEntityDescription
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    _attr_native_value: Incomplete
    _attr_extra_state_attributes: Incomplete
    def __init__(self, coordinator: AirlyDataUpdateCoordinator, name: str, description: AirlySensorEntityDescription) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
