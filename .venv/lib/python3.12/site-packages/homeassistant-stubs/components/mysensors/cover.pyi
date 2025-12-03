from . import setup_mysensors_platform as setup_mysensors_platform
from .const import DiscoveryInfo as DiscoveryInfo, MYSENSORS_DISCOVERY as MYSENSORS_DISCOVERY
from .entity import MySensorsChildEntity as MySensorsChildEntity
from .helpers import on_unload as on_unload
from enum import Enum
from homeassistant.components.cover import ATTR_POSITION as ATTR_POSITION, CoverEntity as CoverEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

class CoverState(Enum):
    OPEN = 0
    OPENING = 1
    CLOSING = 2
    CLOSED = 3

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MySensorsCover(MySensorsChildEntity, CoverEntity):
    def get_cover_state(self) -> CoverState: ...
    @property
    def is_closed(self) -> bool: ...
    @property
    def is_closing(self) -> bool: ...
    @property
    def is_opening(self) -> bool: ...
    @property
    def current_cover_position(self) -> int | None: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    async def async_set_cover_position(self, **kwargs: Any) -> None: ...
    async def async_stop_cover(self, **kwargs: Any) -> None: ...
