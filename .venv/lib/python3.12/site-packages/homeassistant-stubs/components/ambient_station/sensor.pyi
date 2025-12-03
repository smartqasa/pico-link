from . import AmbientStation as AmbientStation, AmbientStationConfigEntry as AmbientStationConfigEntry
from .const import ATTR_LAST_DATA as ATTR_LAST_DATA, TYPE_SOLARRADIATION as TYPE_SOLARRADIATION, TYPE_SOLARRADIATION_LX as TYPE_SOLARRADIATION_LX
from .entity import AmbientWeatherEntity as AmbientWeatherEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import ATTR_NAME as ATTR_NAME, CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, DEGREE as DEGREE, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, UnitOfIrradiance as UnitOfIrradiance, UnitOfLength as UnitOfLength, UnitOfPrecipitationDepth as UnitOfPrecipitationDepth, UnitOfPressure as UnitOfPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature, UnitOfVolumetricFlux as UnitOfVolumetricFlux
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

TYPE_24HOURRAININ: str
TYPE_AQI_PM25: str
TYPE_AQI_PM25_24H: str
TYPE_AQI_PM25_IN: str
TYPE_AQI_PM25_IN_24H: str
TYPE_BAROMABSIN: str
TYPE_BAROMRELIN: str
TYPE_CO2: str
TYPE_DAILYRAININ: str
TYPE_DEWPOINT: str
TYPE_EVENTRAININ: str
TYPE_FEELSLIKE: str
TYPE_HOURLYRAININ: str
TYPE_HUMIDITY: str
TYPE_HUMIDITY1: str
TYPE_HUMIDITY10: str
TYPE_HUMIDITY2: str
TYPE_HUMIDITY3: str
TYPE_HUMIDITY4: str
TYPE_HUMIDITY5: str
TYPE_HUMIDITY6: str
TYPE_HUMIDITY7: str
TYPE_HUMIDITY8: str
TYPE_HUMIDITY9: str
TYPE_HUMIDITYIN: str
TYPE_LASTRAIN: str
TYPE_LIGHTNING_PER_DAY: str
TYPE_LIGHTNING_PER_HOUR: str
TYPE_LASTLIGHTNING_DISTANCE: str
TYPE_LASTLIGHTNING: str
TYPE_MAXDAILYGUST: str
TYPE_MONTHLYRAININ: str
TYPE_PM25: str
TYPE_PM25_24H: str
TYPE_PM25_IN: str
TYPE_PM25_IN_24H: str
TYPE_SOILHUM1: str
TYPE_SOILHUM10: str
TYPE_SOILHUM2: str
TYPE_SOILHUM3: str
TYPE_SOILHUM4: str
TYPE_SOILHUM5: str
TYPE_SOILHUM6: str
TYPE_SOILHUM7: str
TYPE_SOILHUM8: str
TYPE_SOILHUM9: str
TYPE_SOILTEMP1F: str
TYPE_SOILTEMP10F: str
TYPE_SOILTEMP2F: str
TYPE_SOILTEMP3F: str
TYPE_SOILTEMP4F: str
TYPE_SOILTEMP5F: str
TYPE_SOILTEMP6F: str
TYPE_SOILTEMP7F: str
TYPE_SOILTEMP8F: str
TYPE_SOILTEMP9F: str
TYPE_TEMP10F: str
TYPE_TEMP1F: str
TYPE_TEMP2F: str
TYPE_TEMP3F: str
TYPE_TEMP4F: str
TYPE_TEMP5F: str
TYPE_TEMP6F: str
TYPE_TEMP7F: str
TYPE_TEMP8F: str
TYPE_TEMP9F: str
TYPE_TEMPF: str
TYPE_TEMPINF: str
TYPE_TOTALRAININ: str
TYPE_UV: str
TYPE_WEEKLYRAININ: str
TYPE_WINDDIR: str
TYPE_WINDDIR_AVG10M: str
TYPE_WINDDIR_AVG2M: str
TYPE_WINDGUSTDIR: str
TYPE_WINDGUSTMPH: str
TYPE_WINDSPDMPH_AVG10M: str
TYPE_WINDSPDMPH_AVG2M: str
TYPE_WINDSPEEDMPH: str
TYPE_YEARLYRAININ: str
SENSOR_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: AmbientStationConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AmbientWeatherSensor(AmbientWeatherEntity, SensorEntity):
    entity_id: Incomplete
    def __init__(self, ambient: AmbientStation, mac_address: str, station_name: str, description: EntityDescription) -> None: ...
    _attr_native_value: Incomplete
    @callback
    def update_from_latest_data(self) -> None: ...
