from . import NanoleafConfigEntry as NanoleafConfigEntry
from .coordinator import NanoleafCoordinator as NanoleafCoordinator
from .entity import NanoleafEntity as NanoleafEntity
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP_KELVIN as ATTR_COLOR_TEMP_KELVIN, ATTR_EFFECT as ATTR_EFFECT, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_TRANSITION as ATTR_TRANSITION, ColorMode as ColorMode, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

RESERVED_EFFECTS: Incomplete
DEFAULT_NAME: str

async def async_setup_entry(hass: HomeAssistant, entry: NanoleafConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NanoleafLight(NanoleafEntity, LightEntity):
    _attr_supported_color_modes: Incomplete
    _attr_supported_features: Incomplete
    _attr_name: Incomplete
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    _attr_max_color_temp_kelvin: Incomplete
    _attr_min_color_temp_kelvin: Incomplete
    def __init__(self, coordinator: NanoleafCoordinator) -> None: ...
    @property
    def brightness(self) -> int: ...
    @property
    def color_temp_kelvin(self) -> int | None: ...
    @property
    def effect(self) -> str | None: ...
    @property
    def effect_list(self) -> list[str]: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def hs_color(self) -> tuple[int, int]: ...
    @property
    def color_mode(self) -> ColorMode | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
