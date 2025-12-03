from .const import BLEScannerMode as BLEScannerMode, CONF_BLE_SCANNER_MODE as CONF_BLE_SCANNER_MODE, CONF_GEN as CONF_GEN, CONF_SLEEP_PERIOD as CONF_SLEEP_PERIOD, DOMAIN as DOMAIN, LOGGER as LOGGER, MODEL_WALL_DISPLAY as MODEL_WALL_DISPLAY
from .coordinator import async_reconnect_soon as async_reconnect_soon
from .utils import get_block_device_sleep_period as get_block_device_sleep_period, get_coap_context as get_coap_context, get_device_entry_gen as get_device_entry_gen, get_http_port as get_http_port, get_info_auth as get_info_auth, get_info_gen as get_info_gen, get_model_name as get_model_name, get_rpc_device_wakeup_period as get_rpc_device_wakeup_period, get_ws_context as get_ws_context, mac_address_from_name as mac_address_from_name
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components.zeroconf import ZeroconfServiceInfo as ZeroconfServiceInfo
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.selector import SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig
from typing import Any, Final

CONFIG_SCHEMA: Final[Incomplete]
BLE_SCANNER_OPTIONS: Incomplete
INTERNAL_WIFI_AP_IP: str

async def validate_input(hass: HomeAssistant, host: str, port: int, info: dict[str, Any], data: dict[str, Any]) -> dict[str, Any]: ...

class ShellyConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    MINOR_VERSION: int
    host: str
    port: int
    info: dict[str, Any]
    device_info: dict[str, Any]
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_credentials(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _async_discovered_mac(self, mac: str, host: str) -> None: ...
    async def async_step_zeroconf(self, discovery_info: ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_confirm_discovery(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _async_get_info(self, host: str, port: int) -> dict[str, Any]: ...
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlowHandler: ...
    @classmethod
    @callback
    def async_supports_options_flow(cls, config_entry: ConfigEntry) -> bool: ...

class OptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
