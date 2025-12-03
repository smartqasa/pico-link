from .const import DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN
from .discovery import ZwaveDiscoveryInfo as ZwaveDiscoveryInfo
from .entity import ZWaveBaseEntity as ZWaveBaseEntity
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP_KELVIN as ATTR_COLOR_TEMP_KELVIN, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_RGBW_COLOR as ATTR_RGBW_COLOR, ATTR_TRANSITION as ATTR_TRANSITION, ColorMode as ColorMode, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any
from zwave_js_server.const.command_class.color_switch import ColorComponent
from zwave_js_server.model.driver import Driver as Driver
from zwave_js_server.model.value import Value

PARALLEL_UPDATES: int
MULTI_COLOR_MAP: Incomplete
MIN_MIREDS: int
MAX_MIREDS: int

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def byte_to_zwave_brightness(value: int) -> int: ...

class ZwaveLight(ZWaveBaseEntity, LightEntity):
    _attr_min_color_temp_kelvin: int
    _attr_max_color_temp_kelvin: int
    _supports_color: bool
    _supports_rgbw: bool
    _supports_color_temp: bool
    _supports_dimming: bool
    _color_mode: str | None
    _hs_color: tuple[float, float] | None
    _rgbw_color: tuple[int, int, int, int] | None
    _color_temp: int | None
    _warm_white: Incomplete
    _cold_white: Incomplete
    _supported_color_modes: set[ColorMode]
    _target_brightness: Value | None
    _attr_name: Incomplete
    _current_color: Incomplete
    _target_color: Incomplete
    supports_brightness_transition: Incomplete
    supports_color_transition: Incomplete
    _set_optimistic_state: bool
    def __init__(self, config_entry: ConfigEntry, driver: Driver, info: ZwaveDiscoveryInfo) -> None: ...
    @callback
    def on_value_update(self) -> None: ...
    @property
    def brightness(self) -> int | None: ...
    @property
    def color_mode(self) -> str | None: ...
    @property
    def is_on(self) -> bool | None: ...
    @property
    def hs_color(self) -> tuple[float, float] | None: ...
    @property
    def rgbw_color(self) -> tuple[int, int, int, int] | None: ...
    @property
    def color_temp_kelvin(self) -> int | None: ...
    @property
    def supported_color_modes(self) -> set[ColorMode] | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def _get_new_colors(self, hs_color: tuple[float, float] | None, color_temp_k: int | None, rgbw: tuple[int, int, int, int] | None, brightness_scale: float | None = None) -> dict[ColorComponent, int] | None: ...
    async def _async_set_colors(self, colors: dict[ColorComponent, int], transition: float | None = None) -> None: ...
    async def _async_set_brightness(self, brightness: int | None, transition: float | None = None) -> None: ...
    @callback
    def _get_color_values(self) -> tuple[Value | None, ...]: ...
    @callback
    def _calculate_color_support(self) -> None: ...
    @callback
    def _calculate_color_values(self) -> None: ...

class ZwaveColorOnOffLight(ZwaveLight):
    _last_on_color: dict[ColorComponent, int] | None
    _last_brightness: int | None
    def __init__(self, config_entry: ConfigEntry, driver: Driver, info: ZwaveDiscoveryInfo) -> None: ...
    @property
    def brightness(self) -> int | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
