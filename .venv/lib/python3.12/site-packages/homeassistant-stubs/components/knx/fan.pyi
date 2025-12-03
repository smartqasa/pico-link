from . import KNXModule as KNXModule
from .const import KNX_ADDRESS as KNX_ADDRESS, KNX_MODULE_KEY as KNX_MODULE_KEY
from .entity import KnxYamlEntity as KnxYamlEntity
from .schema import FanSchema as FanSchema
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components.fan import FanEntity as FanEntity, FanEntityFeature as FanEntityFeature
from homeassistant.const import CONF_ENTITY_CATEGORY as CONF_ENTITY_CATEGORY, CONF_NAME as CONF_NAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.percentage import percentage_to_ranged_value as percentage_to_ranged_value, ranged_value_to_percentage as ranged_value_to_percentage
from homeassistant.util.scaling import int_states_in_range as int_states_in_range
from typing import Any, Final
from xknx.devices import Fan as XknxFan

DEFAULT_PERCENTAGE: Final[int]

async def async_setup_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class KNXFan(KnxYamlEntity, FanEntity):
    _device: XknxFan
    _step_range: tuple[int, int] | None
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, knx_module: KNXModule, config: ConfigType) -> None: ...
    async def async_set_percentage(self, percentage: int) -> None: ...
    @property
    def supported_features(self) -> FanEntityFeature: ...
    @property
    def percentage(self) -> int | None: ...
    @property
    def speed_count(self) -> int: ...
    async def async_turn_on(self, percentage: int | None = None, preset_mode: str | None = None, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_oscillate(self, oscillating: bool) -> None: ...
    @property
    def oscillating(self) -> bool | None: ...
