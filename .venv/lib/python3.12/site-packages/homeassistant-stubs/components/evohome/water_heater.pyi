import evohomeasync2 as evo
from . import EvoBroker as EvoBroker
from .const import DOMAIN as DOMAIN, EVO_FOLLOW as EVO_FOLLOW, EVO_PERMOVER as EVO_PERMOVER
from .entity import EvoChild as EvoChild
from _typeshed import Incomplete
from homeassistant.components.water_heater import WaterHeaterEntity as WaterHeaterEntity, WaterHeaterEntityFeature as WaterHeaterEntityFeature
from homeassistant.const import PRECISION_TENTHS as PRECISION_TENTHS, PRECISION_WHOLE as PRECISION_WHOLE, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Incomplete
STATE_AUTO: str
HA_STATE_TO_EVO: Incomplete
EVO_STATE_TO_HA: Incomplete
STATE_ATTRS_DHW: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class EvoDHW(EvoChild, WaterHeaterEntity):
    _attr_name: str
    _attr_icon: str
    _attr_operation_list: Incomplete
    _attr_temperature_unit: Incomplete
    _evo_device: evo.HotWater
    _evo_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_precision: Incomplete
    _attr_supported_features: Incomplete
    def __init__(self, evo_broker: EvoBroker, evo_device: evo.HotWater) -> None: ...
    @property
    def current_operation(self) -> str | None: ...
    @property
    def is_away_mode_on(self) -> bool | None: ...
    async def async_set_operation_mode(self, operation_mode: str) -> None: ...
    async def async_turn_away_mode_on(self) -> None: ...
    async def async_turn_away_mode_off(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_update(self) -> None: ...
