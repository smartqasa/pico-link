import asyncio
from .const import CONF_COMMAND_TIMEOUT as CONF_COMMAND_TIMEOUT, LOGGER as LOGGER, TRIGGER_ENTITY_OPTIONS as TRIGGER_ENTITY_OPTIONS
from .utils import async_call_shell_with_timeout as async_call_shell_with_timeout, async_check_output_or_log as async_check_output_or_log
from _typeshed import Incomplete
from datetime import datetime, timedelta
from homeassistant.components.cover import CoverEntity as CoverEntity
from homeassistant.const import CONF_COMMAND_CLOSE as CONF_COMMAND_CLOSE, CONF_COMMAND_OPEN as CONF_COMMAND_OPEN, CONF_COMMAND_STATE as CONF_COMMAND_STATE, CONF_COMMAND_STOP as CONF_COMMAND_STOP, CONF_NAME as CONF_NAME, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.trigger_template_entity import ManualTriggerEntity as ManualTriggerEntity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util import slugify as slugify
from typing import Any

SCAN_INTERVAL: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class CommandCover(ManualTriggerEntity, CoverEntity):
    _attr_should_poll: bool
    _state: int | None
    _command_open: Incomplete
    _command_close: Incomplete
    _command_stop: Incomplete
    _command_state: Incomplete
    _value_template: Incomplete
    _timeout: Incomplete
    _scan_interval: Incomplete
    _process_updates: asyncio.Lock | None
    def __init__(self, config: ConfigType, command_open: str, command_close: str, command_stop: str, command_state: str | None, value_template: Template | None, timeout: int, scan_interval: timedelta) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def _async_move_cover(self, command: str) -> bool: ...
    @property
    def is_closed(self) -> bool | None: ...
    @property
    def current_cover_position(self) -> int | None: ...
    async def _async_query_state(self) -> str | None: ...
    async def _update_entity_state(self, now: datetime | None = None) -> None: ...
    async def _async_update(self) -> None: ...
    async def async_update(self) -> None: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    async def async_stop_cover(self, **kwargs: Any) -> None: ...
