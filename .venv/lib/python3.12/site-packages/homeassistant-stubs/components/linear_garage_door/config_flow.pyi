from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Collection, Mapping, Sequence
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import CONF_EMAIL as CONF_EMAIL, CONF_PASSWORD as CONF_PASSWORD
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete

async def validate_input(hass: HomeAssistant, data: dict[str, str]) -> dict[str, Sequence[Collection[str]]]: ...

class LinearGarageDoorConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    data: dict[str, Sequence[Collection[str]]]
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_site(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...

class InvalidAuth(HomeAssistantError): ...
class InvalidDeviceID(HomeAssistantError): ...
