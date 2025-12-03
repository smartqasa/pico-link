from . import AppleTvConfigEntry as AppleTvConfigEntry
from .entity import AppleTVEntity as AppleTVEntity
from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant.components.remote import ATTR_DELAY_SECS as ATTR_DELAY_SECS, ATTR_HOLD_SECS as ATTR_HOLD_SECS, ATTR_NUM_REPEATS as ATTR_NUM_REPEATS, DEFAULT_DELAY_SECS as DEFAULT_DELAY_SECS, DEFAULT_HOLD_SECS as DEFAULT_HOLD_SECS, RemoteEntity as RemoteEntity
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Incomplete
PARALLEL_UPDATES: int
COMMAND_TO_ATTRIBUTE: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: AppleTvConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AppleTVRemote(AppleTVEntity, RemoteEntity):
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_send_command(self, command: Iterable[str], **kwargs: Any) -> None: ...
