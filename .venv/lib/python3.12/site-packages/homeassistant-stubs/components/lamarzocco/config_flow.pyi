from .const import CONF_USE_BLUETOOTH as CONF_USE_BLUETOOTH, DOMAIN as DOMAIN
from .coordinator import LaMarzoccoConfigEntry as LaMarzoccoConfigEntry
from _typeshed import Incomplete
from aiohttp import ClientSession as ClientSession
from collections.abc import Mapping
from homeassistant.components.bluetooth import BluetoothServiceInfo as BluetoothServiceInfo, async_discovered_service_info as async_discovered_service_info
from homeassistant.components.dhcp import DhcpServiceInfo as DhcpServiceInfo
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow, SOURCE_REAUTH as SOURCE_REAUTH, SOURCE_RECONFIGURE as SOURCE_RECONFIGURE
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_MODEL as CONF_MODEL, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_TOKEN as CONF_TOKEN, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from homeassistant.helpers.aiohttp_client import async_create_clientsession as async_create_clientsession
from homeassistant.helpers.selector import SelectOptionDict as SelectOptionDict, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode
from pylamarzocco.models import LaMarzoccoDeviceInfo as LaMarzoccoDeviceInfo
from typing import Any

CONF_MACHINE: str
_LOGGER: Incomplete

class LmConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _client: ClientSession
    _config: dict[str, Any]
    _fleet: dict[str, LaMarzoccoDeviceInfo]
    _discovered: dict[str, str]
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_machine_selection(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_bluetooth_selection(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_bluetooth(self, discovery_info: BluetoothServiceInfo) -> ConfigFlowResult: ...
    async def async_step_dhcp(self, discovery_info: DhcpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: LaMarzoccoConfigEntry) -> LmOptionsFlowHandler: ...

class LmOptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
