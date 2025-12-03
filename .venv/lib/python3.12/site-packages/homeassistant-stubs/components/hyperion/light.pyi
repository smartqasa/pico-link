from . import get_hyperion_device_id as get_hyperion_device_id, get_hyperion_unique_id as get_hyperion_unique_id, listen_for_instance_updates as listen_for_instance_updates
from .const import CONF_EFFECT_HIDE_LIST as CONF_EFFECT_HIDE_LIST, CONF_INSTANCE_CLIENTS as CONF_INSTANCE_CLIENTS, CONF_PRIORITY as CONF_PRIORITY, DEFAULT_ORIGIN as DEFAULT_ORIGIN, DEFAULT_PRIORITY as DEFAULT_PRIORITY, DOMAIN as DOMAIN, HYPERION_MANUFACTURER_NAME as HYPERION_MANUFACTURER_NAME, HYPERION_MODEL_NAME as HYPERION_MODEL_NAME, SIGNAL_ENTITY_REMOVE as SIGNAL_ENTITY_REMOVE, TYPE_HYPERION_LIGHT as TYPE_HYPERION_LIGHT
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping, Sequence
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_EFFECT as ATTR_EFFECT, ATTR_HS_COLOR as ATTR_HS_COLOR, ColorMode as ColorMode, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from hyperion import client as client
from types import MappingProxyType
from typing import Any

_LOGGER: Incomplete
CONF_DEFAULT_COLOR: str
CONF_HDMI_PRIORITY: str
CONF_EFFECT_LIST: str
KEY_EFFECT_SOLID: str
DEFAULT_COLOR: Incomplete
DEFAULT_BRIGHTNESS: int
DEFAULT_EFFECT = KEY_EFFECT_SOLID
DEFAULT_NAME: str
DEFAULT_PORT: Incomplete
DEFAULT_HDMI_PRIORITY: int
DEFAULT_EFFECT_LIST: list[str]
ICON_LIGHTBULB: str
ICON_EFFECT: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HyperionLight(LightEntity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_color_mode: Incomplete
    _attr_should_poll: bool
    _attr_supported_color_modes: Incomplete
    _attr_supported_features: Incomplete
    _attr_unique_id: Incomplete
    _device_id: Incomplete
    _instance_name: Incomplete
    _options: Incomplete
    _client: Incomplete
    _brightness: int
    _rgb_color: Sequence[int]
    _effect: str
    _static_effect_list: list[str]
    _effect_list: list[str]
    _client_callbacks: Mapping[str, Callable[[dict[str, Any]], None]]
    _attr_device_info: Incomplete
    def __init__(self, server_id: str, instance_num: int, instance_name: str, options: MappingProxyType[str, Any], hyperion_client: client.HyperionClient) -> None: ...
    def _compute_unique_id(self, server_id: str, instance_num: int) -> str: ...
    @property
    def brightness(self) -> int: ...
    @property
    def hs_color(self) -> tuple[float, float]: ...
    @property
    def icon(self) -> str: ...
    @property
    def effect(self) -> str: ...
    @property
    def effect_list(self) -> list[str]: ...
    @property
    def available(self) -> bool: ...
    def _get_option(self, key: str) -> Any: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def _set_internal_state(self, brightness: int | None = None, rgb_color: Sequence[int] | None = None, effect: str | None = None) -> None: ...
    @callback
    def _update_components(self, _: dict[str, Any] | None = None) -> None: ...
    @callback
    def _update_adjustment(self, _: dict[str, Any] | None = None) -> None: ...
    @callback
    def _update_priorities(self, _: dict[str, Any] | None = None) -> None: ...
    @callback
    def _update_effect_list(self, _: dict[str, Any] | None = None) -> None: ...
    @callback
    def _update_full_state(self) -> None: ...
    @callback
    def _update_client(self, _: dict[str, Any] | None = None) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    def _get_priority_entry_that_dictates_state(self) -> dict[str, Any] | None: ...
