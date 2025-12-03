from .const import POWER_PLUGS as POWER_PLUGS
from .entity import DeconzDevice as DeconzDevice
from .hub import DeconzHub as DeconzHub
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP_KELVIN as ATTR_COLOR_TEMP_KELVIN, ATTR_EFFECT as ATTR_EFFECT, ATTR_FLASH as ATTR_FLASH, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_TRANSITION as ATTR_TRANSITION, ATTR_XY_COLOR as ATTR_XY_COLOR, ColorMode as ColorMode, DEFAULT_MAX_KELVIN as DEFAULT_MAX_KELVIN, DEFAULT_MIN_KELVIN as DEFAULT_MIN_KELVIN, DOMAIN as LIGHT_DOMAIN, EFFECT_COLORLOOP as EFFECT_COLORLOOP, FLASH_LONG as FLASH_LONG, FLASH_SHORT as FLASH_SHORT, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.color import color_hs_to_xy as color_hs_to_xy, color_temperature_kelvin_to_mired as color_temperature_kelvin_to_mired, color_temperature_mired_to_kelvin as color_temperature_mired_to_kelvin
from pydeconz.interfaces.groups import GroupHandler as GroupHandler
from pydeconz.interfaces.lights import LightHandler as LightHandler
from pydeconz.models.event import EventType as EventType
from pydeconz.models.group import Group
from pydeconz.models.light.light import Light, LightAlert, LightEffect
from typing import Any, TypedDict

DECONZ_GROUP: str
EFFECT_TO_DECONZ: Incomplete
FLASH_TO_DECONZ: Incomplete
DECONZ_TO_COLOR_MODE: Incomplete
XMAS_LIGHT_EFFECTS: Incomplete

class SetStateAttributes(TypedDict, total=False):
    alert: LightAlert
    brightness: int
    color_temperature: int
    effect: LightEffect
    hue: int
    on: bool
    saturation: int
    transition_time: int
    xy: tuple[float, float]

def update_color_state(group: Group, lights: list[Light], override: bool = False) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DeconzBaseLight[_LightDeviceT: Group | Light](DeconzDevice[_LightDeviceT], LightEntity):
    TYPE = LIGHT_DOMAIN
    _attr_color_mode: Incomplete
    _attr_min_color_temp_kelvin = DEFAULT_MIN_KELVIN
    _attr_max_color_temp_kelvin = DEFAULT_MAX_KELVIN
    api: GroupHandler | LightHandler
    _attr_supported_color_modes: set[ColorMode]
    _attr_effect_list: Incomplete
    def __init__(self, device: _LightDeviceT, hub: DeconzHub) -> None: ...
    @property
    def color_mode(self) -> str | None: ...
    @property
    def brightness(self) -> int | None: ...
    @property
    def color_temp_kelvin(self) -> int | None: ...
    @property
    def hs_color(self) -> tuple[float, float] | None: ...
    @property
    def xy_color(self) -> tuple[float, float] | None: ...
    @property
    def is_on(self) -> bool | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, bool]: ...

class DeconzLight(DeconzBaseLight[Light]):
    @property
    def min_color_temp_kelvin(self) -> int: ...
    @property
    def max_color_temp_kelvin(self) -> int: ...
    @callback
    def async_update_callback(self) -> None: ...

class DeconzGroup(DeconzBaseLight[Group]):
    _attr_has_entity_name: bool
    _unique_id: Incomplete
    _attr_name: Incomplete
    def __init__(self, device: Group, hub: DeconzHub) -> None: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def extra_state_attributes(self) -> dict[str, bool]: ...
