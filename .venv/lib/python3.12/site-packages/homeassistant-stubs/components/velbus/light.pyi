from . import VelbusConfigEntry as VelbusConfigEntry
from .entity import VelbusEntity as VelbusEntity, api_call as api_call
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_FLASH as ATTR_FLASH, ATTR_TRANSITION as ATTR_TRANSITION, ColorMode as ColorMode, FLASH_LONG as FLASH_LONG, FLASH_SHORT as FLASH_SHORT, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any
from velbusaio.channels import Button as VelbusButton, Channel as VelbusChannel, Dimmer as VelbusDimmer

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: VelbusConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class VelbusLight(VelbusEntity, LightEntity):
    _channel: VelbusDimmer
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_supported_features: Incomplete
    @property
    def is_on(self) -> bool: ...
    @property
    def brightness(self) -> int: ...
    @api_call
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @api_call
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class VelbusButtonLight(VelbusEntity, LightEntity):
    _channel: VelbusButton
    _attr_entity_registry_enabled_default: bool
    _attr_entity_category: Incomplete
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_supported_features: Incomplete
    _attr_name: Incomplete
    def __init__(self, channel: VelbusChannel) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @api_call
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @api_call
    async def async_turn_off(self, **kwargs: Any) -> None: ...
