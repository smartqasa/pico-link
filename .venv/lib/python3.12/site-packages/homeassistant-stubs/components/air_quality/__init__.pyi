from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType, StateType as StateType
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Final, final

_LOGGER: Final[Incomplete]
DATA_COMPONENT: HassKey[EntityComponent[AirQualityEntity]]
ENTITY_ID_FORMAT: Final[Incomplete]
PLATFORM_SCHEMA: Incomplete
PLATFORM_SCHEMA_BASE: Incomplete
SCAN_INTERVAL: Final[Incomplete]
ATTR_AQI: Final[str]
ATTR_CO2: Final[str]
ATTR_CO: Final[str]
ATTR_N2O: Final[str]
ATTR_NO: Final[str]
ATTR_NO2: Final[str]
ATTR_OZONE: Final[str]
ATTR_PM_0_1: Final[str]
ATTR_PM_10: Final[str]
ATTR_PM_2_5: Final[str]
ATTR_SO2: Final[str]
PROP_TO_ATTR: Final[dict[str, str]]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class AirQualityEntity(Entity):
    @property
    def particulate_matter_2_5(self) -> StateType: ...
    @property
    def particulate_matter_10(self) -> StateType: ...
    @property
    def particulate_matter_0_1(self) -> StateType: ...
    @property
    def air_quality_index(self) -> StateType: ...
    @property
    def ozone(self) -> StateType: ...
    @property
    def carbon_monoxide(self) -> StateType: ...
    @property
    def carbon_dioxide(self) -> StateType: ...
    @property
    def sulphur_dioxide(self) -> StateType: ...
    @property
    def nitrogen_oxide(self) -> StateType: ...
    @property
    def nitrogen_monoxide(self) -> StateType: ...
    @property
    def nitrogen_dioxide(self) -> StateType: ...
    @final
    @property
    def state_attributes(self) -> dict[str, str | int | float]: ...
    @property
    def state(self) -> StateType: ...
    @property
    def unit_of_measurement(self) -> str: ...
