from .entity import ReolinkChannelCoordinatorEntity as ReolinkChannelCoordinatorEntity, ReolinkChannelEntityDescription as ReolinkChannelEntityDescription, ReolinkHostCoordinatorEntity as ReolinkHostCoordinatorEntity, ReolinkHostEntityDescription as ReolinkHostEntityDescription
from .util import ReolinkConfigEntry as ReolinkConfigEntry, ReolinkData as ReolinkData, raise_translated_error as raise_translated_error
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ColorMode as ColorMode, LightEntity as LightEntity, LightEntityDescription as LightEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from reolink_aio.api import Host as Host
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class ReolinkLightEntityDescription(LightEntityDescription, ReolinkChannelEntityDescription):
    get_brightness_fn: Callable[[Host, int], int | None] | None = ...
    is_on_fn: Callable[[Host, int], bool]
    set_brightness_fn: Callable[[Host, int, int], Any] | None = ...
    turn_on_off_fn: Callable[[Host, int, bool], Any]

@dataclass(frozen=True, kw_only=True)
class ReolinkHostLightEntityDescription(LightEntityDescription, ReolinkHostEntityDescription):
    is_on_fn: Callable[[Host], bool]
    turn_on_off_fn: Callable[[Host, bool], Any]

LIGHT_ENTITIES: Incomplete
HOST_LIGHT_ENTITIES: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ReolinkConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ReolinkLightEntity(ReolinkChannelCoordinatorEntity, LightEntity):
    entity_description: ReolinkLightEntityDescription
    _attr_supported_color_modes: Incomplete
    _attr_color_mode: Incomplete
    def __init__(self, reolink_data: ReolinkData, channel: int, entity_description: ReolinkLightEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def brightness(self) -> int | None: ...
    @raise_translated_error
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @raise_translated_error
    async def async_turn_on(self, **kwargs: Any) -> None: ...

class ReolinkHostLightEntity(ReolinkHostCoordinatorEntity, LightEntity):
    entity_description: ReolinkHostLightEntityDescription
    _attr_supported_color_modes: Incomplete
    _attr_color_mode: Incomplete
    def __init__(self, reolink_data: ReolinkData, entity_description: ReolinkHostLightEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @raise_translated_error
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @raise_translated_error
    async def async_turn_on(self, **kwargs: Any) -> None: ...
