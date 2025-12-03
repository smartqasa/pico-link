from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from pyprusalink.types import VersionInfo as VersionInfo
from typing import Any

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete

def ensure_printer_is_supported(version: VersionInfo) -> None: ...
async def validate_input(hass: HomeAssistant, data: dict[str, str]) -> dict[str, str]: ...

class PrusaLinkConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    MINOR_VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class CannotConnect(HomeAssistantError): ...
class NotSupported(HomeAssistantError): ...
