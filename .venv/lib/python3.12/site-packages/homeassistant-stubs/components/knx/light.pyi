from . import KNXModule as KNXModule
from .const import CONF_SYNC_STATE as CONF_SYNC_STATE, ColorTempModes as ColorTempModes, DOMAIN as DOMAIN, KNX_ADDRESS as KNX_ADDRESS, KNX_MODULE_KEY as KNX_MODULE_KEY
from .entity import KnxUiEntity as KnxUiEntity, KnxUiEntityPlatformController as KnxUiEntityPlatformController, KnxYamlEntity as KnxYamlEntity
from .schema import LightSchema as LightSchema
from .storage.const import CONF_COLOR_TEMP_MAX as CONF_COLOR_TEMP_MAX, CONF_COLOR_TEMP_MIN as CONF_COLOR_TEMP_MIN, CONF_DPT as CONF_DPT, CONF_ENTITY as CONF_ENTITY, CONF_GA_BLUE_BRIGHTNESS as CONF_GA_BLUE_BRIGHTNESS, CONF_GA_BLUE_SWITCH as CONF_GA_BLUE_SWITCH, CONF_GA_BRIGHTNESS as CONF_GA_BRIGHTNESS, CONF_GA_COLOR as CONF_GA_COLOR, CONF_GA_COLOR_TEMP as CONF_GA_COLOR_TEMP, CONF_GA_GREEN_BRIGHTNESS as CONF_GA_GREEN_BRIGHTNESS, CONF_GA_GREEN_SWITCH as CONF_GA_GREEN_SWITCH, CONF_GA_HUE as CONF_GA_HUE, CONF_GA_PASSIVE as CONF_GA_PASSIVE, CONF_GA_RED_BRIGHTNESS as CONF_GA_RED_BRIGHTNESS, CONF_GA_RED_SWITCH as CONF_GA_RED_SWITCH, CONF_GA_SATURATION as CONF_GA_SATURATION, CONF_GA_STATE as CONF_GA_STATE, CONF_GA_SWITCH as CONF_GA_SWITCH, CONF_GA_WHITE_BRIGHTNESS as CONF_GA_WHITE_BRIGHTNESS, CONF_GA_WHITE_SWITCH as CONF_GA_WHITE_SWITCH, CONF_GA_WRITE as CONF_GA_WRITE
from .storage.entity_store_schema import LightColorMode as LightColorMode
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP_KELVIN as ATTR_COLOR_TEMP_KELVIN, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_RGBW_COLOR as ATTR_RGBW_COLOR, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ATTR_XY_COLOR as ATTR_XY_COLOR, ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.const import CONF_ENTITY_CATEGORY as CONF_ENTITY_CATEGORY, CONF_NAME as CONF_NAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback, async_get_current_platform as async_get_current_platform
from homeassistant.helpers.typing import ConfigType as ConfigType
from propcache import cached_property
from typing import Any
from xknx import XKNX as XKNX
from xknx.devices.light import Light as XknxLight

async def async_setup_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def _create_yaml_light(xknx: XKNX, config: ConfigType) -> XknxLight: ...
def _create_ui_light(xknx: XKNX, knx_config: ConfigType, name: str) -> XknxLight: ...

class _KnxLight(LightEntity):
    _attr_max_color_temp_kelvin: int
    _attr_min_color_temp_kelvin: int
    _device: XknxLight
    @property
    def is_on(self) -> bool: ...
    @property
    def brightness(self) -> int | None: ...
    @property
    def rgb_color(self) -> tuple[int, int, int] | None: ...
    @property
    def rgbw_color(self) -> tuple[int, int, int, int] | None: ...
    @property
    def hs_color(self) -> tuple[float, float] | None: ...
    @property
    def xy_color(self) -> tuple[float, float] | None: ...
    @property
    def color_temp_kelvin(self) -> int | None: ...
    @cached_property
    def supported_color_modes(self) -> set[ColorMode]: ...
    _attr_color_mode: Incomplete
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class KnxYamlLight(_KnxLight, KnxYamlEntity):
    _device: XknxLight
    _attr_color_mode: Incomplete
    _attr_max_color_temp_kelvin: int
    _attr_min_color_temp_kelvin: int
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, knx_module: KNXModule, config: ConfigType) -> None: ...
    def _device_unique_id(self) -> str: ...

class KnxUiLight(_KnxLight, KnxUiEntity):
    _device: XknxLight
    _attr_color_mode: Incomplete
    _attr_max_color_temp_kelvin: int
    _attr_min_color_temp_kelvin: int
    def __init__(self, knx_module: KNXModule, unique_id: str, config: ConfigType) -> None: ...
