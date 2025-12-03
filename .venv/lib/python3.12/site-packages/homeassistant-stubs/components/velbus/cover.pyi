from . import VelbusConfigEntry as VelbusConfigEntry
from .entity import VelbusEntity as VelbusEntity, api_call as api_call
from _typeshed import Incomplete
from homeassistant.components.cover import ATTR_POSITION as ATTR_POSITION, CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any
from velbusaio.channels import Blind as VelbusBlind

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: VelbusConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class VelbusCover(VelbusEntity, CoverEntity):
    _channel: VelbusBlind
    _assumed_closed: bool
    _attr_supported_features: Incomplete
    _attr_assumed_state: bool
    def __init__(self, channel: VelbusBlind) -> None: ...
    @property
    def is_closed(self) -> bool | None: ...
    @property
    def is_opening(self) -> bool: ...
    @property
    def is_closing(self) -> bool: ...
    @property
    def current_cover_position(self) -> int | None: ...
    @api_call
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    @api_call
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    @api_call
    async def async_stop_cover(self, **kwargs: Any) -> None: ...
    @api_call
    async def async_set_cover_position(self, **kwargs: Any) -> None: ...
