from .const import CONF_PHONE as CONF_PHONE, CONF_REFRESH_TOKEN as CONF_REFRESH_TOKEN, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any

_LOGGER: Incomplete
_STEP_PHONE_NUMBER_SCHEMA: Incomplete
_STEP_OTP_CODE_SCHEMA: Incomplete
_PHONE_MATCHER: Incomplete

class Tami4ConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    phone: str
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_otp(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class InvalidPhoneNumber(HomeAssistantError): ...
