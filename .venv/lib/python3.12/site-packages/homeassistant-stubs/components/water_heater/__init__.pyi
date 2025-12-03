from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from enum import IntFlag
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_TENTHS as PRECISION_TENTHS, PRECISION_WHOLE as PRECISION_WHOLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.deprecation import deprecated_class as deprecated_class
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType, VolDictType as VolDictType
from homeassistant.util.hass_dict import HassKey as HassKey
from homeassistant.util.unit_conversion import TemperatureConverter as TemperatureConverter
from propcache import cached_property
from typing import Any, final

DATA_COMPONENT: HassKey[EntityComponent[WaterHeaterEntity]]
ENTITY_ID_FORMAT: Incomplete
PLATFORM_SCHEMA: Incomplete
PLATFORM_SCHEMA_BASE: Incomplete
SCAN_INTERVAL: Incomplete
DEFAULT_MIN_TEMP: int
DEFAULT_MAX_TEMP: int
SERVICE_SET_AWAY_MODE: str
SERVICE_SET_TEMPERATURE: str
SERVICE_SET_OPERATION_MODE: str
STATE_ECO: str
STATE_ELECTRIC: str
STATE_PERFORMANCE: str
STATE_HIGH_DEMAND: str
STATE_HEAT_PUMP: str
STATE_GAS: str

class WaterHeaterEntityFeature(IntFlag):
    TARGET_TEMPERATURE = 1
    OPERATION_MODE = 2
    AWAY_MODE = 4
    ON_OFF = 8

ATTR_MAX_TEMP: str
ATTR_MIN_TEMP: str
ATTR_AWAY_MODE: str
ATTR_OPERATION_MODE: str
ATTR_OPERATION_LIST: str
ATTR_TARGET_TEMP_HIGH: str
ATTR_TARGET_TEMP_LOW: str
ATTR_CURRENT_TEMPERATURE: str
CONVERTIBLE_ATTRIBUTE: Incomplete
_LOGGER: Incomplete
SET_AWAY_MODE_SCHEMA: VolDictType
SET_TEMPERATURE_SCHEMA: VolDictType
SET_OPERATION_MODE_SCHEMA: VolDictType

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class WaterHeaterEntityDescription(EntityDescription, frozen_or_thawed=True): ...
class WaterHeaterEntityEntityDescription(WaterHeaterEntityDescription, frozen_or_thawed=True): ...

CACHED_PROPERTIES_WITH_ATTR_: Incomplete

class WaterHeaterEntity(Entity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    _entity_component_unrecorded_attributes: Incomplete
    entity_description: WaterHeaterEntityDescription
    _attr_current_operation: str | None
    _attr_current_temperature: float | None
    _attr_is_away_mode_on: bool | None
    _attr_max_temp: float
    _attr_min_temp: float
    _attr_operation_list: list[str] | None
    _attr_precision: float
    _attr_state: None
    _attr_supported_features: WaterHeaterEntityFeature
    _attr_target_temperature_high: float | None
    _attr_target_temperature_low: float | None
    _attr_target_temperature: float | None
    _attr_temperature_unit: str
    @final
    @property
    def state(self) -> str | None: ...
    @property
    def precision(self) -> float: ...
    @property
    def capability_attributes(self) -> dict[str, Any]: ...
    @final
    @property
    def state_attributes(self) -> dict[str, Any]: ...
    @cached_property
    def temperature_unit(self) -> str: ...
    @cached_property
    def current_operation(self) -> str | None: ...
    @cached_property
    def operation_list(self) -> list[str] | None: ...
    @cached_property
    def current_temperature(self) -> float | None: ...
    @cached_property
    def target_temperature(self) -> float | None: ...
    @cached_property
    def target_temperature_high(self) -> float | None: ...
    @cached_property
    def target_temperature_low(self) -> float | None: ...
    @cached_property
    def is_away_mode_on(self) -> bool | None: ...
    def set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def set_operation_mode(self, operation_mode: str) -> None: ...
    async def async_set_operation_mode(self, operation_mode: str) -> None: ...
    @final
    async def async_handle_set_operation_mode(self, operation_mode: str) -> None: ...
    def turn_away_mode_on(self) -> None: ...
    async def async_turn_away_mode_on(self) -> None: ...
    def turn_away_mode_off(self) -> None: ...
    async def async_turn_away_mode_off(self) -> None: ...
    @property
    def min_temp(self) -> float: ...
    @property
    def max_temp(self) -> float: ...
    @property
    def supported_features(self) -> WaterHeaterEntityFeature: ...

async def async_service_away_mode(entity: WaterHeaterEntity, service: ServiceCall) -> None: ...
async def async_service_temperature_set(entity: WaterHeaterEntity, service: ServiceCall) -> None: ...
