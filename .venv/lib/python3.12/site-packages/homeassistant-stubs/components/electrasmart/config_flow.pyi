from .const import CONF_IMEI as CONF_IMEI, CONF_OTP as CONF_OTP, CONF_PHONE_NUMBER as CONF_PHONE_NUMBER, DOMAIN as DOMAIN
from _typeshed import Incomplete
from electrasmart.api import ElectraAPI
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_TOKEN as CONF_TOKEN
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

_LOGGER: Incomplete

class ElectraSmartConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _phone_number: str | None
    _description_placeholders: Incomplete
    _otp: str | None
    _imei: str | None
    _token: str | None
    _api: ElectraAPI | None
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    def _show_setup_form(self, user_input: dict[str, str] | None = None, errors: dict[str, str] | None = None, step_id: str = 'user') -> ConfigFlowResult: ...
    async def _validate_phone_number(self, user_input: dict[str, str]) -> ConfigFlowResult: ...
    async def _validate_one_time_password(self, user_input: dict[str, str]) -> ConfigFlowResult: ...
    async def async_step_one_time_password(self, user_input: dict[str, Any] | None = None, errors: dict[str, str] | None = None) -> ConfigFlowResult: ...
    async def _show_otp_form(self, errors: dict[str, str] | None = None) -> ConfigFlowResult: ...
