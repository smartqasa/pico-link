from .const import CONF_GATEWAY_ID as CONF_GATEWAY_ID, COORDINATOR as COORDINATOR, COORDINATOR_LIST as COORDINATOR_LIST, DOMAIN as DOMAIN, KEY_API as KEY_API
from .coordinator import TradfriDeviceDataUpdateCoordinator as TradfriDeviceDataUpdateCoordinator
from .entity import TradfriBaseEntity as TradfriBaseEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP_KELVIN as ATTR_COLOR_TEMP_KELVIN, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_TRANSITION as ATTR_TRANSITION, ColorMode as ColorMode, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature, filter_supported_color_modes as filter_supported_color_modes
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pytradfri.command import Command as Command
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TradfriLight(TradfriBaseEntity, LightEntity):
    _attr_name: Incomplete
    _attr_supported_features: Incomplete
    _fixed_color_mode: ColorMode | None
    _device_control: Incomplete
    _device_data: Incomplete
    _attr_unique_id: Incomplete
    _hs_color: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_max_color_temp_kelvin: Incomplete
    _attr_min_color_temp_kelvin: Incomplete
    def __init__(self, device_coordinator: TradfriDeviceDataUpdateCoordinator, api: Callable[[Command | list[Command]], Any], gateway_id: str) -> None: ...
    def _refresh(self) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def color_mode(self) -> ColorMode | None: ...
    @property
    def brightness(self) -> int | None: ...
    @property
    def color_temp_kelvin(self) -> int | None: ...
    @property
    def hs_color(self) -> tuple[float, float] | None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
