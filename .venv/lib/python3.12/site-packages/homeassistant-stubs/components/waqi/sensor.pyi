from .const import DOMAIN as DOMAIN
from .coordinator import WAQIDataUpdateCoordinator as WAQIDataUpdateCoordinator
from _typeshed import Incomplete
from aiowaqi import WAQIAirQuality as WAQIAirQuality
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE, UnitOfPressure as UnitOfPressure, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

_LOGGER: Incomplete
ATTR_DOMINENTPOL: str
ATTR_HUMIDITY: str
ATTR_NITROGEN_DIOXIDE: str
ATTR_OZONE: str
ATTR_PM10: str
ATTR_PM2_5: str
ATTR_PRESSURE: str
ATTR_SULFUR_DIOXIDE: str

@dataclass(frozen=True, kw_only=True)
class WAQISensorEntityDescription(SensorEntityDescription):
    available_fn: Callable[[WAQIAirQuality], bool] = ...
    value_fn: Callable[[WAQIAirQuality], StateType]

SENSORS: list[WAQISensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WaqiSensor(CoordinatorEntity[WAQIDataUpdateCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    entity_description: WAQISensorEntityDescription
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_attribution: Incomplete
    def __init__(self, coordinator: WAQIDataUpdateCoordinator, entity_description: WAQISensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
