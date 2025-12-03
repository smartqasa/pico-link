from .const import CONF_TURN_OFF_COMMAND as CONF_TURN_OFF_COMMAND, CONF_TURN_ON_COMMAND as CONF_TURN_ON_COMMAND, DOMAIN as DOMAIN
from .entity import AndroidTVEntity as AndroidTVEntity, adb_decorator as adb_decorator
from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant.components.remote import ATTR_NUM_REPEATS as ATTR_NUM_REPEATS, RemoteEntity as RemoteEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AndroidTVRemote(AndroidTVEntity, RemoteEntity):
    _attr_name: Incomplete
    _attr_should_poll: bool
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_send_command(self, command: Iterable[str], **kwargs: Any) -> None: ...
