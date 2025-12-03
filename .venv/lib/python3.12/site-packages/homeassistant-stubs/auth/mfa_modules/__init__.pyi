import types
import voluptuous as vol
from _typeshed import Incomplete
from homeassistant import data_entry_flow as data_entry_flow, requirements as requirements
from homeassistant.const import CONF_ID as CONF_ID, CONF_NAME as CONF_NAME, CONF_TYPE as CONF_TYPE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.importlib import async_import_module as async_import_module
from homeassistant.util.decorator import Registry as Registry
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Any, Generic
from typing_extensions import TypeVar

MULTI_FACTOR_AUTH_MODULES: Registry[str, type[MultiFactorAuthModule]]
MULTI_FACTOR_AUTH_MODULE_SCHEMA: Incomplete
DATA_REQS: HassKey[set[str]]
_LOGGER: Incomplete
_MultiFactorAuthModuleT = TypeVar('_MultiFactorAuthModuleT', bound='MultiFactorAuthModule', default='MultiFactorAuthModule')

class MultiFactorAuthModule:
    DEFAULT_TITLE: str
    MAX_RETRY_TIME: int
    hass: Incomplete
    config: Incomplete
    def __init__(self, hass: HomeAssistant, config: dict[str, Any]) -> None: ...
    @property
    def id(self) -> str: ...
    @property
    def type(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def input_schema(self) -> vol.Schema: ...
    async def async_setup_flow(self, user_id: str) -> SetupFlow[Any]: ...
    async def async_setup_user(self, user_id: str, setup_data: Any) -> Any: ...
    async def async_depose_user(self, user_id: str) -> None: ...
    async def async_is_user_setup(self, user_id: str) -> bool: ...
    async def async_validate(self, user_id: str, user_input: dict[str, Any]) -> bool: ...

class SetupFlow(data_entry_flow.FlowHandler, Generic[_MultiFactorAuthModuleT]):
    _auth_module: Incomplete
    _setup_schema: Incomplete
    _user_id: Incomplete
    def __init__(self, auth_module: _MultiFactorAuthModuleT, setup_schema: vol.Schema, user_id: str) -> None: ...
    async def async_step_init(self, user_input: dict[str, str] | None = None) -> FlowResult: ...

async def auth_mfa_module_from_config(hass: HomeAssistant, config: dict[str, Any]) -> MultiFactorAuthModule: ...
async def _load_mfa_module(hass: HomeAssistant, module_name: str) -> types.ModuleType: ...
