from .const import CONF_STATION as CONF_STATION, DOMAIN as DOMAIN
from .coordinator import InvalidAuth as InvalidAuth, async_validate_input as async_validate_input
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

COMPONENT_DOMAIN = DOMAIN
STEP_USER_DATA_SCHEMA: Incomplete

async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, str]: ...

class WallboxConfigFlow(ConfigFlow, domain=COMPONENT_DOMAIN):
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
