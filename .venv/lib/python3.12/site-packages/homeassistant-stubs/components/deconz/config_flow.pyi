from .const import CONF_ALLOW_CLIP_SENSOR as CONF_ALLOW_CLIP_SENSOR, CONF_ALLOW_DECONZ_GROUPS as CONF_ALLOW_DECONZ_GROUPS, CONF_ALLOW_NEW_DEVICES as CONF_ALLOW_NEW_DEVICES, DEFAULT_ALLOW_CLIP_SENSOR as DEFAULT_ALLOW_CLIP_SENSOR, DEFAULT_ALLOW_DECONZ_GROUPS as DEFAULT_ALLOW_DECONZ_GROUPS, DEFAULT_ALLOW_NEW_DEVICES as DEFAULT_ALLOW_NEW_DEVICES, DEFAULT_PORT as DEFAULT_PORT, DOMAIN as DOMAIN, HASSIO_CONFIGURATION_URL as HASSIO_CONFIGURATION_URL, LOGGER as LOGGER
from .hub import DeconzHub as DeconzHub
from collections.abc import Mapping
from homeassistant.components import ssdp as ssdp
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow, SOURCE_HASSIO as SOURCE_HASSIO
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.service_info.hassio import HassioServiceInfo as HassioServiceInfo
from pydeconz.utils import DiscoveredBridge as DiscoveredBridge
from typing import Any

DECONZ_MANUFACTURERURL: str
CONF_SERIAL: str
CONF_MANUAL_INPUT: str

@callback
def get_master_hub(hass: HomeAssistant) -> DeconzHub: ...

class DeconzFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _hassio_discovery: dict[str, Any]
    bridges: list[DiscoveredBridge]
    host: str
    port: int
    api_key: str
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> DeconzOptionsFlowHandler: ...
    bridge_id: str
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_manual_input(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_link(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _create_entry(self) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_ssdp(self, discovery_info: ssdp.SsdpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_hassio(self, discovery_info: HassioServiceInfo) -> ConfigFlowResult: ...
    async def async_step_hassio_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class DeconzOptionsFlowHandler(OptionsFlow):
    gateway: DeconzHub
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_deconz_devices(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
