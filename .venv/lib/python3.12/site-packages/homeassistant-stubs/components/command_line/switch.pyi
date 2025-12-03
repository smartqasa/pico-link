import asyncio
from .const import CONF_COMMAND_TIMEOUT as CONF_COMMAND_TIMEOUT, LOGGER as LOGGER, TRIGGER_ENTITY_OPTIONS as TRIGGER_ENTITY_OPTIONS
from .utils import async_call_shell_with_timeout as async_call_shell_with_timeout, async_check_output_or_log as async_check_output_or_log
from _typeshed import Incomplete
from datetime import datetime, timedelta
from homeassistant.components.switch import ENTITY_ID_FORMAT as ENTITY_ID_FORMAT, SwitchEntity as SwitchEntity
from homeassistant.const import CONF_COMMAND_OFF as CONF_COMMAND_OFF, CONF_COMMAND_ON as CONF_COMMAND_ON, CONF_COMMAND_STATE as CONF_COMMAND_STATE, CONF_NAME as CONF_NAME, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE
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

class CommandSwitch(ManualTriggerEntity, SwitchEntity):
    _attr_should_poll: bool
    entity_id: Incomplete
    _attr_is_on: bool
    _command_on: Incomplete
    _command_off: Incomplete
    _command_state: Incomplete
    _value_template: Incomplete
    _timeout: Incomplete
    _scan_interval: Incomplete
    _process_updates: asyncio.Lock | None
    def __init__(self, config: ConfigType, object_id: str, command_on: str, command_off: str, command_state: str | None, value_template: Template | None, timeout: int, scan_interval: timedelta) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def _switch(self, command: str) -> bool: ...
    async def _async_query_state_value(self, command: str) -> str | None: ...
    async def _async_query_state_code(self, command: str) -> bool: ...
    @property
    def assumed_state(self) -> bool: ...
    async def _async_query_state(self) -> str | int | None: ...
    async def _update_entity_state(self, now: datetime | None = None) -> None: ...
    async def _async_update(self) -> None: ...
    async def async_update(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
