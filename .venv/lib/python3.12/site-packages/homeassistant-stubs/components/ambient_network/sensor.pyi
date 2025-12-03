from . import AmbientNetworkConfigEntry as AmbientNetworkConfigEntry
from .coordinator import AmbientNetworkDataUpdateCoordinator as AmbientNetworkDataUpdateCoordinator
from .entity import AmbientNetworkEntity as AmbientNetworkEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, CONF_MAC as CONF_MAC, DEGREE as DEGREE, PERCENTAGE as PERCENTAGE, UnitOfIrradiance as UnitOfIrradiance, UnitOfLength as UnitOfLength, UnitOfPrecipitationDepth as UnitOfPrecipitationDepth, UnitOfPressure as UnitOfPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature, UnitOfVolumetricFlux as UnitOfVolumetricFlux
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

TYPE_AQI_PM25: str
TYPE_AQI_PM25_24H: str
TYPE_BAROMABSIN: str
TYPE_BAROMRELIN: str
TYPE_CO2: str
TYPE_DAILYRAININ: str
TYPE_DEWPOINT: str
TYPE_EVENTRAININ: str
TYPE_FEELSLIKE: str
TYPE_HOURLYRAININ: str
TYPE_HUMIDITY: str
TYPE_LASTRAIN: str
TYPE_LIGHTNING_DISTANCE: str
TYPE_LIGHTNING_PER_DAY: str
TYPE_LIGHTNING_PER_HOUR: str
TYPE_MAXDAILYGUST: str
TYPE_MONTHLYRAININ: str
TYPE_PM25: str
TYPE_PM25_24H: str
TYPE_SOLARRADIATION: str
TYPE_TEMPF: str
TYPE_UV: str
TYPE_WEEKLYRAININ: str
TYPE_WINDDIR: str
TYPE_WINDGUSTMPH: str
TYPE_WINDSPEEDMPH: str
TYPE_YEARLYRAININ: str
SENSOR_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: AmbientNetworkConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AmbientNetworkSensor(AmbientNetworkEntity, SensorEntity):
    def __init__(self, coordinator: AmbientNetworkDataUpdateCoordinator, description: SensorEntityDescription, mac_address: str) -> None: ...
    _attr_available: Incomplete
    _attr_native_value: Incomplete
    _attr_extra_state_attributes: Incomplete
    def _update_attrs(self) -> None: ...
