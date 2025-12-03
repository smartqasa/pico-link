from .const import ATTR_FRIENDLY_NAME as ATTR_FRIENDLY_NAME, ATTR_ITEM_NUMBER as ATTR_ITEM_NUMBER, ATTR_SERIAL_NUMBER as ATTR_SERIAL_NUMBER, ATTR_TYPE_NUMBER as ATTR_TYPE_NUMBER, COMPATIBLE_MODELS as COMPATIBLE_MODELS, CONF_SERIAL_NUMBER as CONF_SERIAL_NUMBER, DEFAULT_MODEL as DEFAULT_MODEL, DOMAIN as DOMAIN
from .util import get_serial_number_from_jid as get_serial_number_from_jid
from _typeshed import Incomplete
from homeassistant.components.zeroconf import ZeroconfServiceInfo as ZeroconfServiceInfo
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MODEL as CONF_MODEL
from homeassistant.helpers.selector import SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig
from homeassistant.util.ssl import get_default_context as get_default_context
from mozart_api.mozart_client import MozartClient
from typing import Any, TypedDict

class EntryData(TypedDict, total=False):
    host: str
    jid: str
    model: str
    name: str

_exception_map: Incomplete

class BangOlufsenConfigFlowHandler(ConfigFlow, domain=DOMAIN):
    _beolink_jid: str
    _client: MozartClient
    _host: str
    _model: str
    _name: str
    _serial_number: str
    def __init__(self) -> None: ...
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_zeroconf(self, discovery_info: ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def _create_entry(self) -> ConfigFlowResult: ...
    async def async_step_zeroconf_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
