from .const import CONF_DEFAULT_TRANSITION as CONF_DEFAULT_TRANSITION, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_TRANSITION as ATTR_TRANSITION, ColorMode as ColorMode, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pylitejet import LiteJet as LiteJet
from typing import Any

ATTR_NUMBER: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LiteJetLight(LightEntity):
    _attr_color_mode: Incomplete
    _attr_should_poll: bool
    _attr_supported_color_modes: Incomplete
    _attr_supported_features: Incomplete
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _config_entry: Incomplete
    _lj: Incomplete
    _index: Incomplete
    _attr_brightness: int
    _attr_is_on: bool
    _attr_unique_id: Incomplete
    _attr_extra_state_attributes: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, config_entry: ConfigEntry, system: LiteJet, index: int, name: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    def _on_load_changed(self, level: int | None) -> None: ...
    def _on_connected_changed(self, connected: bool, reason: str) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_available: Incomplete
    async def async_update(self) -> None: ...
