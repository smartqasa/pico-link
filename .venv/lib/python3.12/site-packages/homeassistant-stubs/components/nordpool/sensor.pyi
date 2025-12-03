from . import NordPoolConfigEntry as NordPoolConfigEntry
from .const import LOGGER as LOGGER
from .coordinator import NordPoolDataUpdateCoordinator as NordPoolDataUpdateCoordinator
from .entity import NordpoolBaseEntity as NordpoolBaseEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import EntityCategory as EntityCategory, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util import slugify as slugify

PARALLEL_UPDATES: int

def validate_prices(func: Callable[[NordpoolPriceSensor], dict[str, tuple[float | None, float, float | None]]], entity: NordpoolPriceSensor, area: str, index: int) -> float | None: ...
def get_prices(entity: NordpoolPriceSensor) -> dict[str, tuple[float | None, float, float | None]]: ...
def get_min_max_price(entity: NordpoolPriceSensor, func: Callable[[float, float], float]) -> tuple[float, datetime, datetime]: ...
def get_blockprices(entity: NordpoolBlockPriceSensor) -> dict[str, dict[str, tuple[datetime, datetime, float, float, float]]]: ...

@dataclass(frozen=True, kw_only=True)
class NordpoolDefaultSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[NordpoolSensor], str | float | datetime | None]

@dataclass(frozen=True, kw_only=True)
class NordpoolPricesSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[NordpoolPriceSensor], float | None]
    extra_fn: Callable[[NordpoolPriceSensor], dict[str, str] | None]

@dataclass(frozen=True, kw_only=True)
class NordpoolBlockPricesSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[tuple[datetime, datetime, float, float, float]], float | datetime | None]

DEFAULT_SENSOR_TYPES: tuple[NordpoolDefaultSensorEntityDescription, ...]
PRICES_SENSOR_TYPES: tuple[NordpoolPricesSensorEntityDescription, ...]
BLOCK_PRICES_SENSOR_TYPES: tuple[NordpoolBlockPricesSensorEntityDescription, ...]
DAILY_AVERAGE_PRICES_SENSOR_TYPES: tuple[SensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: NordPoolConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NordpoolSensor(NordpoolBaseEntity, SensorEntity):
    entity_description: NordpoolDefaultSensorEntityDescription
    @property
    def native_value(self) -> str | float | datetime | None: ...

class NordpoolPriceSensor(NordpoolBaseEntity, SensorEntity):
    entity_description: NordpoolPricesSensorEntityDescription
    _attr_native_unit_of_measurement: Incomplete
    def __init__(self, coordinator: NordPoolDataUpdateCoordinator, entity_description: NordpoolPricesSensorEntityDescription, area: str, currency: str) -> None: ...
    @property
    def native_value(self) -> float | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, str] | None: ...

class NordpoolBlockPriceSensor(NordpoolBaseEntity, SensorEntity):
    entity_description: NordpoolBlockPricesSensorEntityDescription
    _attr_native_unit_of_measurement: Incomplete
    _attr_unique_id: Incomplete
    block_name: Incomplete
    _attr_translation_placeholders: Incomplete
    def __init__(self, coordinator: NordPoolDataUpdateCoordinator, entity_description: NordpoolBlockPricesSensorEntityDescription, area: str, currency: str, block_name: str) -> None: ...
    @property
    def native_value(self) -> float | datetime | None: ...

class NordpoolDailyAveragePriceSensor(NordpoolBaseEntity, SensorEntity):
    entity_description: SensorEntityDescription
    _attr_native_unit_of_measurement: Incomplete
    def __init__(self, coordinator: NordPoolDataUpdateCoordinator, entity_description: SensorEntityDescription, area: str, currency: str) -> None: ...
    @property
    def native_value(self) -> float | None: ...
