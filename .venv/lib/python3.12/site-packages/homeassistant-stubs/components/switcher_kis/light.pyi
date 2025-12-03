from .const import SIGNAL_DEVICE_ADD as SIGNAL_DEVICE_ADD
from .coordinator import SwitcherDataUpdateCoordinator as SwitcherDataUpdateCoordinator
from .entity import SwitcherEntity as SwitcherEntity
from _typeshed import Incomplete
from homeassistant.components.light import ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

API_SET_LIGHT: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SwitcherBaseLightEntity(SwitcherEntity, LightEntity):
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    control_result: bool | None
    _light_id: int
    @callback
    def _handle_coordinator_update(self) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class SwitcherSingleLightEntity(SwitcherBaseLightEntity):
    _attr_name: Incomplete
    _light_id: Incomplete
    control_result: bool | None
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SwitcherDataUpdateCoordinator, light_id: int) -> None: ...

class SwitcherMultiLightEntity(SwitcherBaseLightEntity):
    _attr_translation_key: str
    _light_id: Incomplete
    control_result: bool | None
    _attr_translation_placeholders: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SwitcherDataUpdateCoordinator, light_id: int) -> None: ...
