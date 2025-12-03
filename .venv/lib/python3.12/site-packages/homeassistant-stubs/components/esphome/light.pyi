from .entity import EsphomeEntity as EsphomeEntity, convert_api_error_ha_error as convert_api_error_ha_error, esphome_state_property as esphome_state_property, platform_async_setup_entry as platform_async_setup_entry
from _typeshed import Incomplete
from aioesphomeapi import EntityInfo as EntityInfo, LightColorCapability, LightInfo, LightState
from functools import lru_cache
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP_KELVIN as ATTR_COLOR_TEMP_KELVIN, ATTR_EFFECT as ATTR_EFFECT, ATTR_FLASH as ATTR_FLASH, ATTR_RGBWW_COLOR as ATTR_RGBWW_COLOR, ATTR_RGBW_COLOR as ATTR_RGBW_COLOR, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ATTR_TRANSITION as ATTR_TRANSITION, ATTR_WHITE as ATTR_WHITE, ColorMode as ColorMode, FLASH_LONG as FLASH_LONG, FLASH_SHORT as FLASH_SHORT, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature
from homeassistant.core import callback as callback
from typing import Any

FLASH_LENGTHS: Incomplete
_COLOR_MODE_MAPPING: Incomplete

def _mired_to_kelvin(mired_temperature: float) -> int: ...
@lru_cache
def _color_mode_to_ha(mode: int) -> str: ...
@lru_cache
def _filter_color_modes(supported: list[int], features: LightColorCapability) -> tuple[int, ...]: ...
@lru_cache
def _least_complex_color_mode(color_modes: tuple[int, ...]) -> int: ...

class EsphomeLight(EsphomeEntity[LightInfo, LightState], LightEntity):
    _native_supported_color_modes: tuple[int, ...]
    _supports_color_mode: bool
    @property
    @esphome_state_property
    def is_on(self) -> bool | None: ...
    @convert_api_error_ha_error
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @convert_api_error_ha_error
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    @esphome_state_property
    def brightness(self) -> int | None: ...
    @property
    @esphome_state_property
    def color_mode(self) -> str | None: ...
    @property
    @esphome_state_property
    def rgb_color(self) -> tuple[int, int, int] | None: ...
    @property
    @esphome_state_property
    def rgbw_color(self) -> tuple[int, int, int, int] | None: ...
    @property
    @esphome_state_property
    def rgbww_color(self) -> tuple[int, int, int, int, int] | None: ...
    @property
    @esphome_state_property
    def color_temp_kelvin(self) -> int: ...
    @property
    @esphome_state_property
    def effect(self) -> str | None: ...
    _attr_supported_features: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_effect_list: Incomplete
    _attr_min_color_temp_kelvin: Incomplete
    _attr_max_color_temp_kelvin: Incomplete
    @callback
    def _on_static_info_update(self, static_info: EntityInfo) -> None: ...

async_setup_entry: Incomplete
