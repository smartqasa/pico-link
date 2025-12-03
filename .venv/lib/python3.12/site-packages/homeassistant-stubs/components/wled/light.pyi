from . import WLEDConfigEntry as WLEDConfigEntry
from .const import ATTR_CCT as ATTR_CCT, ATTR_COLOR_PRIMARY as ATTR_COLOR_PRIMARY, ATTR_ON as ATTR_ON, ATTR_SEGMENT_ID as ATTR_SEGMENT_ID, COLOR_TEMP_K_MAX as COLOR_TEMP_K_MAX, COLOR_TEMP_K_MIN as COLOR_TEMP_K_MIN, LIGHT_CAPABILITIES_COLOR_MODE_MAPPING as LIGHT_CAPABILITIES_COLOR_MODE_MAPPING
from .coordinator import WLEDDataUpdateCoordinator as WLEDDataUpdateCoordinator
from .entity import WLEDEntity as WLEDEntity
from .helpers import kelvin_to_255 as kelvin_to_255, kelvin_to_255_reverse as kelvin_to_255_reverse, wled_exception_handler as wled_exception_handler
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP_KELVIN as ATTR_COLOR_TEMP_KELVIN, ATTR_EFFECT as ATTR_EFFECT, ATTR_RGBW_COLOR as ATTR_RGBW_COLOR, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ATTR_TRANSITION as ATTR_TRANSITION, ColorMode as ColorMode, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: WLEDConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WLEDMainLight(WLEDEntity, LightEntity):
    _attr_color_mode: Incomplete
    _attr_translation_key: str
    _attr_supported_features: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: WLEDDataUpdateCoordinator) -> None: ...
    @property
    def brightness(self) -> int | None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def available(self) -> bool: ...
    @wled_exception_handler
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @wled_exception_handler
    async def async_turn_on(self, **kwargs: Any) -> None: ...

class WLEDSegmentLight(WLEDEntity, LightEntity):
    _attr_supported_features: Incomplete
    _attr_translation_key: str
    _attr_min_color_temp_kelvin = COLOR_TEMP_K_MIN
    _attr_max_color_temp_kelvin = COLOR_TEMP_K_MAX
    _segment: Incomplete
    _attr_name: Incomplete
    _attr_translation_placeholders: Incomplete
    _attr_unique_id: Incomplete
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    def __init__(self, coordinator: WLEDDataUpdateCoordinator, segment: int) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def rgb_color(self) -> tuple[int, int, int] | None: ...
    @property
    def rgbw_color(self) -> tuple[int, int, int, int] | None: ...
    @property
    def color_temp_kelvin(self) -> int | None: ...
    @property
    def effect(self) -> str | None: ...
    @property
    def brightness(self) -> int | None: ...
    @property
    def effect_list(self) -> list[str]: ...
    @property
    def is_on(self) -> bool: ...
    @wled_exception_handler
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @wled_exception_handler
    async def async_turn_on(self, **kwargs: Any) -> None: ...

@callback
def async_update_segments(coordinator: WLEDDataUpdateCoordinator, current_ids: set[int], async_add_entities: AddEntitiesCallback) -> None: ...
