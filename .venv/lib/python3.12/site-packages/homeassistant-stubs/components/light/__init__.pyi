import dataclasses
from .const import COLOR_MODES_BRIGHTNESS as COLOR_MODES_BRIGHTNESS, COLOR_MODES_COLOR as COLOR_MODES_COLOR, ColorMode as ColorMode, DATA_COMPONENT as DATA_COMPONENT, DATA_PROFILES as DATA_PROFILES, DEFAULT_MAX_KELVIN as DEFAULT_MAX_KELVIN, DEFAULT_MIN_KELVIN as DEFAULT_MIN_KELVIN, DOMAIN as DOMAIN, LightEntityFeature as LightEntityFeature, SCAN_INTERVAL as SCAN_INTERVAL, VALID_COLOR_MODES as VALID_COLOR_MODES
from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.deprecation import DeprecatedConstant as DeprecatedConstant, DeprecatedConstantEnum as DeprecatedConstantEnum, all_with_deprecated_constants as all_with_deprecated_constants, check_if_deprecated_constant as check_if_deprecated_constant, dir_with_deprecated_constants as dir_with_deprecated_constants
from homeassistant.helpers.entity import ToggleEntity as ToggleEntity, ToggleEntityDescription as ToggleEntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.frame import ReportBehavior as ReportBehavior, report_usage as report_usage
from homeassistant.helpers.typing import ConfigType as ConfigType, VolDictType as VolDictType
from homeassistant.loader import bind_hass as bind_hass
from propcache import cached_property
from typing import Any, Final, Self, final

ENTITY_ID_FORMAT: Incomplete
PLATFORM_SCHEMA: Incomplete
PLATFORM_SCHEMA_BASE: Incomplete
_DEPRECATED_SUPPORT_BRIGHTNESS: Final[Incomplete]
_DEPRECATED_SUPPORT_COLOR_TEMP: Final[Incomplete]
_DEPRECATED_SUPPORT_EFFECT: Final[Incomplete]
_DEPRECATED_SUPPORT_FLASH: Final[Incomplete]
_DEPRECATED_SUPPORT_COLOR: Final[Incomplete]
_DEPRECATED_SUPPORT_TRANSITION: Final[Incomplete]
ATTR_COLOR_MODE: str
ATTR_SUPPORTED_COLOR_MODES: str
_DEPRECATED_COLOR_MODE_UNKNOWN: Final[Incomplete]
_DEPRECATED_COLOR_MODE_ONOFF: Final[Incomplete]
_DEPRECATED_COLOR_MODE_BRIGHTNESS: Final[Incomplete]
_DEPRECATED_COLOR_MODE_COLOR_TEMP: Final[Incomplete]
_DEPRECATED_COLOR_MODE_HS: Final[Incomplete]
_DEPRECATED_COLOR_MODE_XY: Final[Incomplete]
_DEPRECATED_COLOR_MODE_RGB: Final[Incomplete]
_DEPRECATED_COLOR_MODE_RGBW: Final[Incomplete]
_DEPRECATED_COLOR_MODE_RGBWW: Final[Incomplete]
_DEPRECATED_COLOR_MODE_WHITE: Final[Incomplete]

def filter_supported_color_modes(color_modes: Iterable[ColorMode]) -> set[ColorMode]: ...
def valid_supported_color_modes(color_modes: Iterable[ColorMode | str]) -> set[ColorMode | str]: ...
def brightness_supported(color_modes: Iterable[ColorMode | str] | None) -> bool: ...
def color_supported(color_modes: Iterable[ColorMode | str] | None) -> bool: ...
def color_temp_supported(color_modes: Iterable[ColorMode | str] | None) -> bool: ...
def get_supported_color_modes(hass: HomeAssistant, entity_id: str) -> set[str] | None: ...

ATTR_TRANSITION: str
ATTR_RGB_COLOR: str
ATTR_RGBW_COLOR: str
ATTR_RGBWW_COLOR: str
ATTR_XY_COLOR: str
ATTR_HS_COLOR: str
ATTR_COLOR_TEMP_KELVIN: str
ATTR_MIN_COLOR_TEMP_KELVIN: str
ATTR_MAX_COLOR_TEMP_KELVIN: str
ATTR_COLOR_NAME: str
ATTR_WHITE: str
_DEPRECATED_ATTR_COLOR_TEMP: Final[Incomplete]
_DEPRECATED_ATTR_KELVIN: Final[Incomplete]
_DEPRECATED_ATTR_MIN_MIREDS: Final[Incomplete]
_DEPRECATED_ATTR_MAX_MIREDS: Final[Incomplete]
ATTR_BRIGHTNESS: str
ATTR_BRIGHTNESS_PCT: str
ATTR_BRIGHTNESS_STEP: str
ATTR_BRIGHTNESS_STEP_PCT: str
ATTR_PROFILE: str
ATTR_FLASH: str
FLASH_SHORT: str
FLASH_LONG: str
ATTR_EFFECT_LIST: str
ATTR_EFFECT: str
EFFECT_COLORLOOP: str
EFFECT_OFF: str
EFFECT_RANDOM: str
EFFECT_WHITE: str
COLOR_GROUP: str
LIGHT_PROFILES_FILE: str
VALID_TRANSITION: Incomplete
VALID_BRIGHTNESS: Incomplete
VALID_BRIGHTNESS_PCT: Incomplete
VALID_BRIGHTNESS_STEP: Incomplete
VALID_BRIGHTNESS_STEP_PCT: Incomplete
VALID_FLASH: Incomplete
LIGHT_TURN_ON_SCHEMA: VolDictType
LIGHT_TURN_OFF_SCHEMA: VolDictType
_LOGGER: Incomplete

@bind_hass
def is_on(hass: HomeAssistant, entity_id: str) -> bool: ...
def preprocess_turn_on_alternatives(hass: HomeAssistant, params: dict[str, Any]) -> None: ...
def filter_turn_off_params(light: LightEntity, params: dict[str, Any]) -> dict[str, Any]: ...
def filter_turn_on_params(light: LightEntity, params: dict[str, Any]) -> dict[str, Any]: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
def _coerce_none(value: str) -> None: ...

@dataclasses.dataclass
class Profile:
    name: str
    color_x: float | None = dataclasses.field(repr=False)
    color_y: float | None = dataclasses.field(repr=False)
    brightness: int | None
    transition: int | None = ...
    hs_color: tuple[float, float] | None = dataclasses.field(init=False)
    SCHEMA = ...
    def __post_init__(self) -> None: ...
    @classmethod
    def from_csv_row(cls, csv_row: list[str]) -> Self: ...

class Profiles:
    hass: Incomplete
    data: dict[str, Profile]
    def __init__(self, hass: HomeAssistant) -> None: ...
    def _load_profile_data(self) -> dict[str, Profile]: ...
    async def async_initialize(self) -> None: ...
    @callback
    def apply_default(self, entity_id: str, state_on: bool | None, params: dict[str, Any]) -> None: ...
    @callback
    def apply_profile(self, name: str, params: dict[str, Any]) -> None: ...

class LightEntityDescription(ToggleEntityDescription, frozen_or_thawed=True): ...

CACHED_PROPERTIES_WITH_ATTR_: Incomplete

class LightEntity(ToggleEntity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    _entity_component_unrecorded_attributes: Incomplete
    entity_description: LightEntityDescription
    _attr_brightness: int | None
    _attr_color_mode: ColorMode | str | None
    _attr_color_temp_kelvin: int | None
    _attr_effect_list: list[str] | None
    _attr_effect: str | None
    _attr_hs_color: tuple[float, float] | None
    _attr_max_color_temp_kelvin: int | None
    _attr_min_color_temp_kelvin: int | None
    _attr_rgb_color: tuple[int, int, int] | None
    _attr_rgbw_color: tuple[int, int, int, int] | None
    _attr_rgbww_color: tuple[int, int, int, int, int] | None
    _attr_supported_color_modes: set[ColorMode] | set[str] | None
    _attr_supported_features: LightEntityFeature
    _attr_xy_color: tuple[float, float] | None
    _attr_color_temp: Final[int | None]
    _attr_max_mireds: Final[int]
    _attr_min_mireds: Final[int]
    __color_mode_reported: bool
    @cached_property
    def brightness(self) -> int | None: ...
    @cached_property
    def color_mode(self) -> ColorMode | str | None: ...
    @property
    def _light_internal_color_mode(self) -> str: ...
    @cached_property
    def hs_color(self) -> tuple[float, float] | None: ...
    @cached_property
    def xy_color(self) -> tuple[float, float] | None: ...
    @cached_property
    def rgb_color(self) -> tuple[int, int, int] | None: ...
    @cached_property
    def rgbw_color(self) -> tuple[int, int, int, int] | None: ...
    @property
    def _light_internal_rgbw_color(self) -> tuple[int, int, int, int] | None: ...
    @cached_property
    def rgbww_color(self) -> tuple[int, int, int, int, int] | None: ...
    @final
    @cached_property
    def color_temp(self) -> int | None: ...
    @property
    def color_temp_kelvin(self) -> int | None: ...
    @final
    @cached_property
    def min_mireds(self) -> int: ...
    @final
    @cached_property
    def max_mireds(self) -> int: ...
    @property
    def min_color_temp_kelvin(self) -> int: ...
    @property
    def max_color_temp_kelvin(self) -> int: ...
    @cached_property
    def effect_list(self) -> list[str] | None: ...
    @cached_property
    def effect(self) -> str | None: ...
    @property
    def capability_attributes(self) -> dict[str, Any]: ...
    def _light_internal_convert_color(self, color_mode: ColorMode | str) -> dict[str, tuple[float, ...]]: ...
    def __validate_color_mode(self, color_mode: ColorMode | str | None, supported_color_modes: set[ColorMode] | set[str], effect: str | None) -> None: ...
    def __validate_supported_color_modes(self, supported_color_modes: set[ColorMode] | set[str]) -> None: ...
    @final
    @property
    def state_attributes(self) -> dict[str, Any] | None: ...
    @property
    def _light_internal_supported_color_modes(self) -> set[ColorMode] | set[str]: ...
    @cached_property
    def supported_color_modes(self) -> set[ColorMode] | set[str] | None: ...
    @cached_property
    def supported_features(self) -> LightEntityFeature: ...
    _deprecated_supported_features_reported: bool
    @property
    def supported_features_compat(self) -> LightEntityFeature: ...
    def __should_report_light_issue(self) -> bool: ...

__getattr__: Incomplete
__dir__: Incomplete
__all__: Incomplete
