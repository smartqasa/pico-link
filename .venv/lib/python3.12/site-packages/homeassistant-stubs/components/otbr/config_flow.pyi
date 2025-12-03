import python_otbr_api
from . import OTBRConfigEntry as OTBRConfigEntry
from .const import DEFAULT_CHANNEL as DEFAULT_CHANNEL, DOMAIN as DOMAIN
from .util import compose_default_network_name as compose_default_network_name, generate_random_pan_id as generate_random_pan_id, get_allowed_channel as get_allowed_channel
from _typeshed import Incomplete
from homeassistant.components.hassio import AddonError as AddonError, AddonManager as AddonManager
from homeassistant.components.thread import async_get_preferred_dataset as async_get_preferred_dataset
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_HASSIO as SOURCE_HASSIO
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.service_info.hassio import HassioServiceInfo as HassioServiceInfo

_LOGGER: Incomplete

class AlreadyConfigured(HomeAssistantError): ...

@callback
def get_addon_manager(hass: HomeAssistant, slug: str) -> AddonManager: ...
def _is_yellow(hass: HomeAssistant) -> bool: ...
async def _title(hass: HomeAssistant, discovery_info: HassioServiceInfo) -> str: ...

class OTBRConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def _set_dataset(self, api: python_otbr_api.OTBR, otbr_url: str) -> None: ...
    async def _is_border_agent_id_configured(self, border_agent_id: bytes) -> bool: ...
    async def _connect_and_configure_router(self, otbr_url: str) -> bytes: ...
    async def async_step_user(self, user_input: dict[str, str] | None = None) -> ConfigFlowResult: ...
    async def async_step_hassio(self, discovery_info: HassioServiceInfo) -> ConfigFlowResult: ...
