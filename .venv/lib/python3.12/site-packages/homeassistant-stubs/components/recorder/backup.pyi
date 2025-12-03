from .util import async_migration_in_progress as async_migration_in_progress, get_instance as get_instance
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError

_LOGGER: Incomplete

async def async_pre_backup(hass: HomeAssistant) -> None: ...
async def async_post_backup(hass: HomeAssistant) -> None: ...
