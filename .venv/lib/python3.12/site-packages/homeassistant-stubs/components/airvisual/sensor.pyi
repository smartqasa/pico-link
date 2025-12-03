from . import AirVisualConfigEntry as AirVisualConfigEntry
from .const import CONF_CITY as CONF_CITY
from .entity import AirVisualEntity as AirVisualEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, ATTR_STATE as ATTR_STATE, CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONCENTRATION_PARTS_PER_BILLION as CONCENTRATION_PARTS_PER_BILLION, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, CONF_COUNTRY as CONF_COUNTRY, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_SHOW_ON_MAP as CONF_SHOW_ON_MAP, CONF_STATE as CONF_STATE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

ATTR_CITY: str
ATTR_COUNTRY: str
ATTR_POLLUTANT_SYMBOL: str
ATTR_POLLUTANT_UNIT: str
ATTR_REGION: str
SENSOR_KIND_AQI: str
SENSOR_KIND_LEVEL: str
SENSOR_KIND_POLLUTANT: str
GEOGRAPHY_SENSOR_DESCRIPTIONS: Incomplete
GEOGRAPHY_SENSOR_LOCALES: Incomplete
STATE_POLLUTANT_LABEL_CO: str
STATE_POLLUTANT_LABEL_N2: str
STATE_POLLUTANT_LABEL_O3: str
STATE_POLLUTANT_LABEL_P1: str
STATE_POLLUTANT_LABEL_P2: str
STATE_POLLUTANT_LABEL_S2: str
STATE_POLLUTANT_LEVEL_GOOD: str
STATE_POLLUTANT_LEVEL_MODERATE: str
STATE_POLLUTANT_LEVEL_UNHEALTHY_SENSITIVE: str
STATE_POLLUTANT_LEVEL_UNHEALTHY: str
STATE_POLLUTANT_LEVEL_VERY_UNHEALTHY: str
STATE_POLLUTANT_LEVEL_HAZARDOUS: str
POLLUTANT_LEVELS: Incomplete
POLLUTANT_UNITS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: AirVisualConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AirVisualGeographySensor(AirVisualEntity, SensorEntity):
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _locale: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator, entry: ConfigEntry, description: SensorEntityDescription, locale: str) -> None: ...
    @property
    def available(self) -> bool: ...
    _attr_native_value: Incomplete
    @callback
    def update_from_latest_data(self) -> None: ...
