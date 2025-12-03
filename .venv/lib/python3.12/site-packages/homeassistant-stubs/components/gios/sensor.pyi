from . import GiosConfigEntry as GiosConfigEntry
from .const import ATTRIBUTION as ATTRIBUTION, ATTR_AQI as ATTR_AQI, ATTR_C6H6 as ATTR_C6H6, ATTR_CO as ATTR_CO, ATTR_NO2 as ATTR_NO2, ATTR_O3 as ATTR_O3, ATTR_PM10 as ATTR_PM10, ATTR_PM25 as ATTR_PM25, ATTR_SO2 as ATTR_SO2, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, URL as URL
from .coordinator import GiosDataUpdateCoordinator as GiosDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from gios.model import GiosSensors as GiosSensors
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class GiosSensorEntityDescription(SensorEntityDescription):
    value: Callable[[GiosSensors], StateType]
    subkey: str | None = ...

SENSOR_TYPES: tuple[GiosSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: GiosConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class GiosSensor(CoordinatorEntity[GiosDataUpdateCoordinator], SensorEntity):
    _attr_attribution = ATTRIBUTION
    _attr_has_entity_name: bool
    entity_description: GiosSensorEntityDescription
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, name: str, coordinator: GiosDataUpdateCoordinator, description: GiosSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def available(self) -> bool: ...
