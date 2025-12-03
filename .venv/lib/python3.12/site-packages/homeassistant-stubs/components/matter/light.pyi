from .const import LOGGER as LOGGER
from .entity import MatterEntity as MatterEntity
from .helpers import get_matter as get_matter
from .models import MatterDiscoverySchema as MatterDiscoverySchema
from .util import convert_to_hass_hs as convert_to_hass_hs, convert_to_hass_xy as convert_to_hass_xy, convert_to_matter_hs as convert_to_matter_hs, convert_to_matter_xy as convert_to_matter_xy, renormalize as renormalize
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP_KELVIN as ATTR_COLOR_TEMP_KELVIN, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_TRANSITION as ATTR_TRANSITION, ATTR_XY_COLOR as ATTR_XY_COLOR, ColorMode as ColorMode, DEFAULT_MAX_KELVIN as DEFAULT_MAX_KELVIN, DEFAULT_MIN_KELVIN as DEFAULT_MIN_KELVIN, LightEntity as LightEntity, LightEntityDescription as LightEntityDescription, LightEntityFeature as LightEntityFeature, filter_supported_color_modes as filter_supported_color_modes
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

COLOR_MODE_MAP: Incomplete
TRANSITION_BLOCKLIST: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MatterLight(MatterEntity, LightEntity):
    entity_description: LightEntityDescription
    _supports_brightness: bool
    _supports_color: bool
    _supports_color_temperature: bool
    _transitions_disabled: bool
    _platform_translation_key: str
    _attr_min_color_temp_kelvin = DEFAULT_MIN_KELVIN
    _attr_max_color_temp_kelvin = DEFAULT_MAX_KELVIN
    async def _set_xy_color(self, xy_color: tuple[float, float], transition: float = 0.0) -> None: ...
    async def _set_hs_color(self, hs_color: tuple[float, float], transition: float = 0.0) -> None: ...
    async def _set_color_temp(self, color_temp_kelvin: int, transition: float = 0.0) -> None: ...
    async def _set_brightness(self, brightness: int, transition: float = 0.0) -> None: ...
    def _get_xy_color(self) -> tuple[float, float]: ...
    def _get_hs_color(self) -> tuple[float, float]: ...
    def _get_color_temperature(self) -> int: ...
    def _get_brightness(self) -> int: ...
    def _get_color_mode(self) -> ColorMode: ...
    async def send_device_command(self, command: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_supported_color_modes: Incomplete
    _attr_is_on: Incomplete
    _attr_brightness: Incomplete
    _attr_color_temp_kelvin: Incomplete
    _attr_color_mode: Incomplete
    _attr_hs_color: Incomplete
    _attr_xy_color: Incomplete
    @callback
    def _update_from_device(self) -> None: ...
    def _check_transition_blocklist(self) -> None: ...

DISCOVERY_SCHEMAS: Incomplete
