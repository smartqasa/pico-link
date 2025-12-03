from . import get_device_info as get_device_info
from .const import ATTRIBUTION as ATTRIBUTION, CONDITION_MAP as CONDITION_MAP, DOMAIN as DOMAIN, METOFFICE_COORDINATES as METOFFICE_COORDINATES, METOFFICE_DAILY_COORDINATOR as METOFFICE_DAILY_COORDINATOR, METOFFICE_HOURLY_COORDINATOR as METOFFICE_HOURLY_COORDINATOR, METOFFICE_NAME as METOFFICE_NAME, MODE_DAILY as MODE_DAILY, VISIBILITY_CLASSES as VISIBILITY_CLASSES, VISIBILITY_DISTANCE_CLASSES as VISIBILITY_DISTANCE_CLASSES
from .data import MetOfficeData as MetOfficeData
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE, UV_INDEX as UV_INDEX, UnitOfLength as UnitOfLength, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

ATTR_LAST_UPDATE: str
ATTR_SENSOR_ID: str
ATTR_SITE_ID: str
ATTR_SITE_NAME: str
SENSOR_TYPES: tuple[SensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MetOfficeCurrentSensor(CoordinatorEntity[DataUpdateCoordinator[MetOfficeData]], SensorEntity):
    _attr_attribution = ATTRIBUTION
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_device_info: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_entity_registry_enabled_default: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator[MetOfficeData], hass_data: dict[str, Any], use_3hourly: bool, description: SensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def icon(self) -> str | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
