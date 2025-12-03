from .const import CONF_COLORS as CONF_COLORS, CONF_CUSTOM_EFFECT_COLORS as CONF_CUSTOM_EFFECT_COLORS, CONF_CUSTOM_EFFECT_SPEED_PCT as CONF_CUSTOM_EFFECT_SPEED_PCT, CONF_CUSTOM_EFFECT_TRANSITION as CONF_CUSTOM_EFFECT_TRANSITION, CONF_SPEED_PCT as CONF_SPEED_PCT, CONF_TRANSITION as CONF_TRANSITION, DEFAULT_EFFECT_SPEED as DEFAULT_EFFECT_SPEED, DOMAIN as DOMAIN, MIN_CCT_BRIGHTNESS as MIN_CCT_BRIGHTNESS, MIN_RGB_BRIGHTNESS as MIN_RGB_BRIGHTNESS, MULTI_BRIGHTNESS_COLOR_MODES as MULTI_BRIGHTNESS_COLOR_MODES, TRANSITION_GRADUAL as TRANSITION_GRADUAL, TRANSITION_JUMP as TRANSITION_JUMP, TRANSITION_STROBE as TRANSITION_STROBE
from .coordinator import FluxLedUpdateCoordinator as FluxLedUpdateCoordinator
from .entity import FluxOnOffEntity as FluxOnOffEntity
from .util import _effect_brightness as _effect_brightness, _flux_color_mode_to_hass as _flux_color_mode_to_hass, _hass_color_modes as _hass_color_modes, _min_rgb_brightness as _min_rgb_brightness, _min_rgbw_brightness as _min_rgbw_brightness, _min_rgbwc_brightness as _min_rgbwc_brightness, _str_to_multi_color_effect as _str_to_multi_color_effect
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP_KELVIN as ATTR_COLOR_TEMP_KELVIN, ATTR_EFFECT as ATTR_EFFECT, ATTR_RGBWW_COLOR as ATTR_RGBWW_COLOR, ATTR_RGBW_COLOR as ATTR_RGBW_COLOR, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ATTR_WHITE as ATTR_WHITE, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature
from homeassistant.const import CONF_EFFECT as CONF_EFFECT
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import VolDictType as VolDictType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any, Final

_LOGGER: Incomplete
MODE_ATTRS: Incomplete
ATTR_FOREGROUND_COLOR: Final[str]
ATTR_BACKGROUND_COLOR: Final[str]
ATTR_SENSITIVITY: Final[str]
ATTR_LIGHT_SCREEN: Final[str]
COLOR_TEMP_WARM_VS_COLD_WHITE_CUT_OFF: Final[int]
EFFECT_CUSTOM: Final[str]
SERVICE_CUSTOM_EFFECT: Final[str]
SERVICE_SET_ZONES: Final[str]
SERVICE_SET_MUSIC_MODE: Final[str]
CUSTOM_EFFECT_DICT: VolDictType
SET_MUSIC_MODE_DICT: VolDictType
SET_ZONES_DICT: VolDictType

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FluxLight(FluxOnOffEntity, CoordinatorEntity[FluxLedUpdateCoordinator], LightEntity):
    _attr_name: Incomplete
    _attr_supported_features: Incomplete
    _attr_min_color_temp_kelvin: Incomplete
    _attr_max_color_temp_kelvin: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_effect_list: Incomplete
    _custom_effect_colors: Incomplete
    _custom_effect_speed_pct: Incomplete
    _custom_effect_transition: Incomplete
    def __init__(self, coordinator: FluxLedUpdateCoordinator, base_unique_id: str, custom_effect_colors: list[tuple[int, int, int]], custom_effect_speed_pct: int, custom_effect_transition: str) -> None: ...
    @property
    def brightness(self) -> int: ...
    @property
    def color_temp_kelvin(self) -> int: ...
    @property
    def rgb_color(self) -> tuple[int, int, int]: ...
    @property
    def rgbw_color(self) -> tuple[int, int, int, int]: ...
    @property
    def rgbww_color(self) -> tuple[int, int, int, int, int]: ...
    @property
    def color_mode(self) -> str: ...
    @property
    def effect(self) -> str | None: ...
    async def _async_turn_on(self, **kwargs: Any) -> None: ...
    async def _async_set_effect(self, effect: str, brightness: int) -> None: ...
    @callback
    def _async_brightness(self, **kwargs: Any) -> int: ...
    async def _async_set_mode(self, **kwargs: Any) -> None: ...
    async def async_set_custom_effect(self, colors: list[tuple[int, int, int]], speed_pct: int, transition: str) -> None: ...
    async def async_set_zones(self, colors: list[tuple[int, int, int]], speed_pct: int, effect: str) -> None: ...
    async def async_set_music_mode(self, sensitivity: int, brightness: int, effect: int, light_screen: bool, foreground_color: tuple[int, int, int] | None = None, background_color: tuple[int, int, int] | None = None) -> None: ...
