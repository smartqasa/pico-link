from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, TemplateError as TemplateError
from homeassistant.helpers import template as template
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.json import JsonObjectType as JsonObjectType

DOMAIN: str
COMMAND_TIMEOUT: int
_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
