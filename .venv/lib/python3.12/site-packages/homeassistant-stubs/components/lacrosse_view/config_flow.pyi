from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from lacrosse_view import Location as Location
from typing import Any

STEP_USER_DATA_SCHEMA: Incomplete
_LOGGER: Incomplete

async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> list[Location]: ...

class LaCrosseViewConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    data: dict[str, str]
    locations: list[Location]
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_location(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...

class InvalidAuth(HomeAssistantError): ...
class NoLocations(HomeAssistantError): ...
class NonExistentEntry(HomeAssistantError): ...
