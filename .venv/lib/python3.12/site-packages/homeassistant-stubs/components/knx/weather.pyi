from . import KNXModule as KNXModule
from .const import KNX_MODULE_KEY as KNX_MODULE_KEY
from .entity import KnxYamlEntity as KnxYamlEntity
from .schema import WeatherSchema as WeatherSchema
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components.weather import WeatherEntity as WeatherEntity
from homeassistant.const import CONF_ENTITY_CATEGORY as CONF_ENTITY_CATEGORY, CONF_NAME as CONF_NAME, Platform as Platform, UnitOfPressure as UnitOfPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType
from xknx import XKNX as XKNX
from xknx.devices import Weather as XknxWeather

async def async_setup_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def _create_weather(xknx: XKNX, config: ConfigType) -> XknxWeather: ...

class KNXWeather(KnxYamlEntity, WeatherEntity):
    _device: XknxWeather
    _attr_native_pressure_unit: Incomplete
    _attr_native_temperature_unit: Incomplete
    _attr_native_wind_speed_unit: Incomplete
    _attr_unique_id: Incomplete
    _attr_entity_category: Incomplete
    def __init__(self, knx_module: KNXModule, config: ConfigType) -> None: ...
    @property
    def native_temperature(self) -> float | None: ...
    @property
    def native_pressure(self) -> float | None: ...
    @property
    def condition(self) -> str: ...
    @property
    def humidity(self) -> float | None: ...
    @property
    def wind_bearing(self) -> int | None: ...
    @property
    def native_wind_speed(self) -> float | None: ...
