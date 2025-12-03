from .const import COMPONENT_LOADED_COOLDOWN as COMPONENT_LOADED_COOLDOWN, DOMAIN as DOMAIN, REQUEST_TIMEOUT as REQUEST_TIMEOUT
from .coordinator import AlertUpdateCoordinator as AlertUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import EVENT_COMPONENT_LOADED as EVENT_COMPONENT_LOADED
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue, async_delete_issue as async_delete_issue
from homeassistant.helpers.start import async_at_started as async_at_started
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.setup import EventComponentLoaded as EventComponentLoaded

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
