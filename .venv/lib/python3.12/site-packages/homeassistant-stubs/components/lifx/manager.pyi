from .const import ATTR_THEME as ATTR_THEME, DATA_LIFX_MANAGER as DATA_LIFX_MANAGER, DOMAIN as DOMAIN, _ATTR_COLOR_TEMP as _ATTR_COLOR_TEMP
from .coordinator import LIFXUpdateCoordinator as LIFXUpdateCoordinator, Light as Light
from .util import convert_8_to_16 as convert_8_to_16, find_hsbk as find_hsbk
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_BRIGHTNESS_PCT as ATTR_BRIGHTNESS_PCT, ATTR_COLOR_NAME as ATTR_COLOR_NAME, ATTR_COLOR_TEMP_KELVIN as ATTR_COLOR_TEMP_KELVIN, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ATTR_TRANSITION as ATTR_TRANSITION, ATTR_XY_COLOR as ATTR_XY_COLOR, COLOR_GROUP as COLOR_GROUP, VALID_BRIGHTNESS as VALID_BRIGHTNESS, VALID_BRIGHTNESS_PCT as VALID_BRIGHTNESS_PCT
from homeassistant.const import ATTR_MODE as ATTR_MODE
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers.service import async_extract_referenced_entity_ids as async_extract_referenced_entity_ids
from typing import Any

SCAN_INTERVAL: Incomplete
SERVICE_EFFECT_COLORLOOP: str
SERVICE_EFFECT_FLAME: str
SERVICE_EFFECT_MORPH: str
SERVICE_EFFECT_MOVE: str
SERVICE_EFFECT_PULSE: str
SERVICE_EFFECT_SKY: str
SERVICE_EFFECT_STOP: str
ATTR_CHANGE: str
ATTR_CLOUD_SATURATION_MIN: str
ATTR_CLOUD_SATURATION_MAX: str
ATTR_CYCLES: str
ATTR_DIRECTION: str
ATTR_PALETTE: str
ATTR_PERIOD: str
ATTR_POWER_OFF: str
ATTR_POWER_ON: str
ATTR_SATURATION_MAX: str
ATTR_SATURATION_MIN: str
ATTR_SKY_TYPE: str
ATTR_SPEED: str
ATTR_SPREAD: str
EFFECT_FLAME: str
EFFECT_MORPH: str
EFFECT_MOVE: str
EFFECT_OFF: str
EFFECT_SKY: str
EFFECT_FLAME_DEFAULT_SPEED: int
EFFECT_MORPH_DEFAULT_SPEED: int
EFFECT_MORPH_DEFAULT_THEME: str
EFFECT_MOVE_DEFAULT_SPEED: int
EFFECT_MOVE_DEFAULT_DIRECTION: str
EFFECT_MOVE_DIRECTION_RIGHT: str
EFFECT_MOVE_DIRECTION_LEFT: str
EFFECT_MOVE_DIRECTIONS: Incomplete
EFFECT_SKY_DEFAULT_SPEED: int
EFFECT_SKY_DEFAULT_SKY_TYPE: str
EFFECT_SKY_DEFAULT_CLOUD_SATURATION_MIN: int
EFFECT_SKY_DEFAULT_CLOUD_SATURATION_MAX: int
EFFECT_SKY_SKY_TYPES: Incomplete
PULSE_MODE_BLINK: str
PULSE_MODE_BREATHE: str
PULSE_MODE_PING: str
PULSE_MODE_SOLID: str
PULSE_MODE_STROBE: str
PULSE_MODES: Incomplete
LIFX_EFFECT_SCHEMA: Incomplete
LIFX_EFFECT_PULSE_SCHEMA: Incomplete
LIFX_EFFECT_COLORLOOP_SCHEMA: Incomplete
LIFX_EFFECT_STOP_SCHEMA: Incomplete
LIFX_EFFECT_FLAME_SCHEMA: Incomplete
HSBK_SCHEMA: Incomplete
LIFX_EFFECT_MORPH_SCHEMA: Incomplete
LIFX_EFFECT_MOVE_SCHEMA: Incomplete
LIFX_EFFECT_SKY_SCHEMA: Incomplete
SERVICES: Incomplete

class LIFXManager:
    hass: Incomplete
    effects_conductor: Incomplete
    entry_id_to_entity_id: dict[str, str]
    def __init__(self, hass: HomeAssistant) -> None: ...
    @callback
    def async_unload(self) -> None: ...
    @callback
    def async_register_entity(self, entity_id: str, entry_id: str) -> Callable[[], None]: ...
    @callback
    def async_setup(self) -> None: ...
    async def start_effect(self, entity_ids: set[str], service: str, **kwargs: Any) -> None: ...
