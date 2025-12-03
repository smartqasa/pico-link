import logging
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from collections.abc import Mapping
from demetriek import CloudDevice as CloudDevice
from homeassistant.components.dhcp import DhcpServiceInfo as DhcpServiceInfo
from homeassistant.components.ssdp import ATTR_UPNP_FRIENDLY_NAME as ATTR_UPNP_FRIENDLY_NAME, ATTR_UPNP_SERIAL as ATTR_UPNP_SERIAL, SsdpServiceInfo as SsdpServiceInfo
from homeassistant.config_entries import ConfigFlowResult as ConfigFlowResult, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_DEVICE as CONF_DEVICE, CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC
from homeassistant.data_entry_flow import AbortFlow as AbortFlow
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.config_entry_oauth2_flow import AbstractOAuth2FlowHandler as AbstractOAuth2FlowHandler
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.selector import SelectOptionDict as SelectOptionDict, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode, TextSelector as TextSelector, TextSelectorConfig as TextSelectorConfig, TextSelectorType as TextSelectorType
from homeassistant.util.network import is_link_local as is_link_local
from typing import Any

class LaMetricFlowHandler(AbstractOAuth2FlowHandler, domain=DOMAIN):
    DOMAIN = DOMAIN
    VERSION: int
    devices: dict[str, CloudDevice]
    discovered_host: str
    discovered_serial: str
    discovered: bool
    @property
    def logger(self) -> logging.Logger: ...
    @property
    def extra_authorize_data(self) -> dict[str, Any]: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_ssdp(self, discovery_info: SsdpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_choice_enter_manual_or_fetch_cloud(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_manual_entry(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_cloud_fetch_devices(self, data: dict[str, Any]) -> ConfigFlowResult: ...
    async def async_step_cloud_select_device(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _async_step_create_entry(self, host: str, api_key: str) -> ConfigFlowResult: ...
    async def async_step_dhcp(self, discovery_info: DhcpServiceInfo) -> ConfigFlowResult: ...
    async_oauth_create_entry = async_step_cloud_fetch_devices
