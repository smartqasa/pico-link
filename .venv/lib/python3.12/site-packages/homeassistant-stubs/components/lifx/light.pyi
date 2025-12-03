import aiolifx_effects as aiolifx_effects_module
from .const import ATTR_DURATION as ATTR_DURATION, ATTR_INFRARED as ATTR_INFRARED, ATTR_POWER as ATTR_POWER, ATTR_ZONES as ATTR_ZONES, DATA_LIFX_MANAGER as DATA_LIFX_MANAGER, DOMAIN as DOMAIN, INFRARED_BRIGHTNESS as INFRARED_BRIGHTNESS, LIFX_CEILING_PRODUCT_IDS as LIFX_CEILING_PRODUCT_IDS, _LOGGER as _LOGGER
from .coordinator import FirmwareEffect as FirmwareEffect, LIFXUpdateCoordinator as LIFXUpdateCoordinator
from .entity import LIFXEntity as LIFXEntity
from .manager import LIFXManager as LIFXManager, SERVICE_EFFECT_COLORLOOP as SERVICE_EFFECT_COLORLOOP, SERVICE_EFFECT_FLAME as SERVICE_EFFECT_FLAME, SERVICE_EFFECT_MORPH as SERVICE_EFFECT_MORPH, SERVICE_EFFECT_MOVE as SERVICE_EFFECT_MOVE, SERVICE_EFFECT_PULSE as SERVICE_EFFECT_PULSE, SERVICE_EFFECT_SKY as SERVICE_EFFECT_SKY, SERVICE_EFFECT_STOP as SERVICE_EFFECT_STOP
from .util import convert_16_to_8 as convert_16_to_8, convert_8_to_16 as convert_8_to_16, find_hsbk as find_hsbk, lifx_features as lifx_features, merge_hsbk as merge_hsbk
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_EFFECT as ATTR_EFFECT, ATTR_TRANSITION as ATTR_TRANSITION, ColorMode as ColorMode, LIGHT_TURN_ON_SCHEMA as LIGHT_TURN_ON_SCHEMA, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, Platform as Platform
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.helpers.typing import VolDictType as VolDictType
from typing import Any

LIFX_STATE_SETTLE_DELAY: float
SERVICE_LIFX_SET_STATE: str
LIFX_SET_STATE_SCHEMA: VolDictType
SERVICE_LIFX_SET_HEV_CYCLE_STATE: str
LIFX_SET_HEV_CYCLE_STATE_SCHEMA: VolDictType
HSBK_HUE: int
HSBK_SATURATION: int
HSBK_BRIGHTNESS: int
HSBK_KELVIN: int

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LIFXLight(LIFXEntity, LightEntity):
    _attr_supported_features: Incomplete
    _attr_name: Incomplete
    mac_addr: Incomplete
    manager: Incomplete
    effects_conductor: aiolifx_effects_module.Conductor
    postponed_update: CALLBACK_TYPE | None
    entry: Incomplete
    _attr_unique_id: Incomplete
    _attr_min_color_temp_kelvin: Incomplete
    _attr_max_color_temp_kelvin: Incomplete
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_effect: Incomplete
    def __init__(self, coordinator: LIFXUpdateCoordinator, manager: LIFXManager, entry: ConfigEntry) -> None: ...
    @property
    def brightness(self) -> int: ...
    @property
    def color_temp_kelvin(self) -> int | None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def effect(self) -> str | None: ...
    async def update_during_transition(self, when: int) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def set_state(self, **kwargs: Any) -> None: ...
    async def set_hev_cycle_state(self, power: bool, duration: int | None = None) -> None: ...
    async def set_power(self, pwr: bool, duration: int = 0) -> None: ...
    async def set_color(self, hsbk: list[float | int | None], kwargs: dict[str, Any], duration: int = 0) -> None: ...
    async def get_color(self) -> None: ...
    async def default_effect(self, **kwargs: Any) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _cancel_postponed_update(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...

class LIFXWhite(LIFXLight):
    _attr_effect_list: Incomplete

class LIFXColor(LIFXLight):
    _attr_effect_list: Incomplete
    @property
    def supported_color_modes(self) -> set[ColorMode]: ...
    @property
    def color_mode(self) -> ColorMode: ...
    @property
    def hs_color(self) -> tuple[float, float] | None: ...

class LIFXMultiZone(LIFXColor):
    _attr_effect_list: Incomplete
    async def set_color(self, hsbk: list[float | int | None], kwargs: dict[str, Any], duration: int = 0) -> None: ...
    async def update_color_zones(self) -> None: ...

class LIFXExtendedMultiZone(LIFXMultiZone):
    async def set_color(self, hsbk: list[float | int | None], kwargs: dict[str, Any], duration: int = 0) -> None: ...

class LIFXMatrix(LIFXColor):
    _attr_effect_list: Incomplete

class LIFXCeiling(LIFXMatrix):
    _attr_effect_list: Incomplete
