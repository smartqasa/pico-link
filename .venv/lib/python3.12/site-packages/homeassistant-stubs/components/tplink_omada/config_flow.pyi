from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import selector as selector
from homeassistant.helpers.aiohttp_client import async_create_clientsession as async_create_clientsession, async_get_clientsession as async_get_clientsession
from tplink_omada_client import OmadaClient, OmadaSite as OmadaSite
from types import MappingProxyType
from typing import Any, NamedTuple

_LOGGER: Incomplete
CONF_SITE: str
STEP_USER_DATA_SCHEMA: Incomplete

async def create_omada_client(hass: HomeAssistant, data: MappingProxyType[str, Any]) -> OmadaClient: ...

class HubInfo(NamedTuple):
    controller_id: str
    name: str
    sites: list[OmadaSite]

async def _validate_input(hass: HomeAssistant, data: dict[str, Any]) -> HubInfo: ...

class TpLinkOmadaConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _omada_opts: dict[str, Any]
    _sites: list[OmadaSite]
    _controller_name: str
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_site(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _test_login(self, data: dict[str, Any], errors: dict[str, str]) -> HubInfo | None: ...
