from .const import DOMAIN as DOMAIN, TYPE_ALLERGY_FORECAST as TYPE_ALLERGY_FORECAST, TYPE_ALLERGY_INDEX as TYPE_ALLERGY_INDEX, TYPE_ALLERGY_OUTLOOK as TYPE_ALLERGY_OUTLOOK, TYPE_ALLERGY_TODAY as TYPE_ALLERGY_TODAY, TYPE_ALLERGY_TOMORROW as TYPE_ALLERGY_TOMORROW, TYPE_ASTHMA_FORECAST as TYPE_ASTHMA_FORECAST, TYPE_ASTHMA_INDEX as TYPE_ASTHMA_INDEX, TYPE_ASTHMA_TODAY as TYPE_ASTHMA_TODAY, TYPE_ASTHMA_TOMORROW as TYPE_ASTHMA_TOMORROW, TYPE_DISEASE_FORECAST as TYPE_DISEASE_FORECAST, TYPE_DISEASE_INDEX as TYPE_DISEASE_INDEX, TYPE_DISEASE_TODAY as TYPE_DISEASE_TODAY
from .entity import IQVIAEntity as IQVIAEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_STATE as ATTR_STATE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import NamedTuple

ATTR_ALLERGEN_AMOUNT: str
ATTR_ALLERGEN_GENUS: str
ATTR_ALLERGEN_NAME: str
ATTR_ALLERGEN_TYPE: str
ATTR_CITY: str
ATTR_OUTLOOK: str
ATTR_RATING: str
ATTR_SEASON: str
ATTR_TREND: str
ATTR_ZIP_CODE: str
API_CATEGORY_MAPPING: Incomplete

class Rating(NamedTuple):
    label: str
    minimum: float
    maximum: float

RATING_MAPPING: list[Rating]
TREND_FLAT: str
TREND_INCREASING: str
TREND_SUBSIDING: str
FORECAST_SENSOR_DESCRIPTIONS: Incomplete
INDEX_SENSOR_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
@callback
def calculate_trend(indices: list[float]) -> str: ...

class ForecastSensor(IQVIAEntity, SensorEntity):
    _attr_native_value: Incomplete
    @callback
    def update_from_latest_data(self) -> None: ...

class IndexSensor(IQVIAEntity, SensorEntity):
    _attr_native_value: Incomplete
    @callback
    def update_from_latest_data(self) -> None: ...
