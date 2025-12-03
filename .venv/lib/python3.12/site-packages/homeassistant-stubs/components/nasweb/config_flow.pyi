from .const import DOMAIN as DOMAIN
from .coordinator import NASwebCoordinator as NASwebCoordinator
from .nasweb_data import NASwebData as NASwebData
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.config_entries import ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.data_entry_flow import AbortFlow as AbortFlow
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.network import NoURLAvailableError as NoURLAvailableError
from typing import Any

NASWEB_SCHEMA_IMG_URL: str
_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete

async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, Any]: ...

class NASwebConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class CannotConnect(HomeAssistantError): ...
class InvalidAuth(HomeAssistantError): ...
class MissingNASwebData(HomeAssistantError): ...
class MissingNASwebStatus(HomeAssistantError): ...
