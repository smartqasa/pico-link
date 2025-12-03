import evohomeasync2 as evo
from . import EvoBroker as EvoBroker
from .const import ATTR_DURATION_DAYS as ATTR_DURATION_DAYS, ATTR_DURATION_HOURS as ATTR_DURATION_HOURS, ATTR_DURATION_UNTIL as ATTR_DURATION_UNTIL, ATTR_SYSTEM_MODE as ATTR_SYSTEM_MODE, ATTR_ZONE_TEMP as ATTR_ZONE_TEMP, DOMAIN as DOMAIN, EVO_AUTO as EVO_AUTO, EVO_AUTOECO as EVO_AUTOECO, EVO_AWAY as EVO_AWAY, EVO_CUSTOM as EVO_CUSTOM, EVO_DAYOFF as EVO_DAYOFF, EVO_FOLLOW as EVO_FOLLOW, EVO_HEATOFF as EVO_HEATOFF, EVO_PERMOVER as EVO_PERMOVER, EVO_RESET as EVO_RESET, EVO_TEMPOVER as EVO_TEMPOVER, EvoService as EvoService
from .entity import EvoChild as EvoChild, EvoDevice as EvoDevice
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACMode as HVACMode, PRESET_AWAY as PRESET_AWAY, PRESET_ECO as PRESET_ECO, PRESET_HOME as PRESET_HOME, PRESET_NONE as PRESET_NONE
from homeassistant.const import PRECISION_TENTHS as PRECISION_TENTHS, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Incomplete
PRESET_RESET: str
PRESET_CUSTOM: str
TCS_PRESET_TO_HA: Incomplete
HA_PRESET_TO_TCS: Incomplete
EVO_PRESET_TO_HA: Incomplete
HA_PRESET_TO_EVO: Incomplete
STATE_ATTRS_TCS: Incomplete
STATE_ATTRS_ZONES: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class EvoClimateEntity(EvoDevice, ClimateEntity):
    _attr_hvac_modes: Incomplete
    _attr_temperature_unit: Incomplete

class EvoZone(EvoChild, EvoClimateEntity):
    _attr_preset_modes: Incomplete
    _evo_device: evo.Zone
    _evo_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_precision: Incomplete
    _attr_supported_features: Incomplete
    def __init__(self, evo_broker: EvoBroker, evo_device: evo.Zone) -> None: ...
    async def async_zone_svc_request(self, service: str, data: dict[str, Any]) -> None: ...
    @property
    def name(self) -> str | None: ...
    @property
    def hvac_mode(self) -> HVACMode | None: ...
    @property
    def target_temperature(self) -> float | None: ...
    @property
    def preset_mode(self) -> str | None: ...
    @property
    def min_temp(self) -> float: ...
    @property
    def max_temp(self) -> float: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    async def async_update(self) -> None: ...

class EvoController(EvoClimateEntity):
    _attr_icon: str
    _attr_precision = PRECISION_TENTHS
    _evo_device: evo.ControlSystem
    _evo_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    _evo_modes: Incomplete
    _attr_preset_modes: Incomplete
    _attr_supported_features: Incomplete
    def __init__(self, evo_broker: EvoBroker, evo_device: evo.ControlSystem) -> None: ...
    async def async_tcs_svc_request(self, service: str, data: dict[str, Any]) -> None: ...
    async def _set_tcs_mode(self, mode: str, until: datetime | None = None) -> None: ...
    @property
    def hvac_mode(self) -> HVACMode: ...
    @property
    def current_temperature(self) -> float | None: ...
    @property
    def preset_mode(self) -> str | None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    _device_state_attrs: Incomplete
    async def async_update(self) -> None: ...
