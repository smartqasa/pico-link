from .const import BLOCK_EXPECTED_SLEEP_PERIOD as BLOCK_EXPECTED_SLEEP_PERIOD, BLOCK_WRONG_SLEEP_PERIOD as BLOCK_WRONG_SLEEP_PERIOD, CONF_COAP_PORT as CONF_COAP_PORT, CONF_SLEEP_PERIOD as CONF_SLEEP_PERIOD, DOMAIN as DOMAIN, FIRMWARE_UNSUPPORTED_ISSUE_ID as FIRMWARE_UNSUPPORTED_ISSUE_ID, LOGGER as LOGGER, MODELS_WITH_WRONG_SLEEP_PERIOD as MODELS_WITH_WRONG_SLEEP_PERIOD, PUSH_UPDATE_ISSUE_ID as PUSH_UPDATE_ISSUE_ID
from .coordinator import ShellyBlockCoordinator as ShellyBlockCoordinator, ShellyConfigEntry as ShellyConfigEntry, ShellyEntryData as ShellyEntryData, ShellyRestCoordinator as ShellyRestCoordinator, ShellyRpcCoordinator as ShellyRpcCoordinator, ShellyRpcPollingCoordinator as ShellyRpcPollingCoordinator
from .utils import async_create_issue_unsupported_firmware as async_create_issue_unsupported_firmware, get_coap_context as get_coap_context, get_device_entry_gen as get_device_entry_gen, get_http_port as get_http_port, get_ws_context as get_ws_context
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Final

PLATFORMS: Final[Incomplete]
BLOCK_SLEEPING_PLATFORMS: Final[Incomplete]
RPC_SLEEPING_PLATFORMS: Final[Incomplete]
COAP_SCHEMA: Final[Incomplete]
CONFIG_SCHEMA: Final[Incomplete]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ShellyConfigEntry) -> bool: ...
async def _async_setup_block_entry(hass: HomeAssistant, entry: ShellyConfigEntry) -> bool: ...
async def _async_setup_rpc_entry(hass: HomeAssistant, entry: ShellyConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ShellyConfigEntry) -> bool: ...
