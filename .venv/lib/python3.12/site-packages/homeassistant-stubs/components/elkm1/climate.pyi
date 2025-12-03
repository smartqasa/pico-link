from . import ElkM1ConfigEntry as ElkM1ConfigEntry
from .const import DOMAIN as DOMAIN
from .entity import ElkEntity as ElkEntity, create_elk_entities as create_elk_entities
from _typeshed import Incomplete
from elkm1_lib.const import ThermostatFan, ThermostatMode
from elkm1_lib.elements import Element as Element
from elkm1_lib.thermostats import Thermostat as Thermostat
from homeassistant.components.climate import ATTR_TARGET_TEMP_HIGH as ATTR_TARGET_TEMP_HIGH, ATTR_TARGET_TEMP_LOW as ATTR_TARGET_TEMP_LOW, ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, FAN_AUTO as FAN_AUTO, FAN_ON as FAN_ON, HVACMode as HVACMode
from homeassistant.const import PRECISION_WHOLE as PRECISION_WHOLE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from typing import Any

SUPPORT_HVAC: Incomplete
HASS_TO_ELK_HVAC_MODES: Incomplete
ELK_TO_HASS_HVAC_MODES: Incomplete
HASS_TO_ELK_FAN_MODES: Incomplete
ELK_TO_HASS_FAN_MODES: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ElkM1ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ElkThermostat(ElkEntity, ClimateEntity):
    _attr_precision = PRECISION_WHOLE
    _attr_supported_features: Incomplete
    _attr_min_temp: int
    _attr_max_temp: int
    _attr_hvac_modes = SUPPORT_HVAC
    _attr_hvac_mode: HVACMode | None
    _attr_target_temperature_step: int
    _attr_fan_modes: Incomplete
    _element: Thermostat
    @property
    def temperature_unit(self) -> str: ...
    @property
    def current_temperature(self) -> float | None: ...
    @property
    def target_temperature(self) -> float | None: ...
    @property
    def target_temperature_high(self) -> float | None: ...
    @property
    def target_temperature_low(self) -> float | None: ...
    @property
    def current_humidity(self) -> int | None: ...
    @property
    def is_aux_heat(self) -> bool: ...
    @property
    def fan_mode(self) -> str | None: ...
    def _elk_set(self, mode: ThermostatMode | None, fan: ThermostatFan | None) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_turn_aux_heat_on(self) -> None: ...
    async def async_turn_aux_heat_off(self) -> None: ...
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    def _element_changed(self, element: Element, changeset: Any) -> None: ...
