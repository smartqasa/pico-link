import openai
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers import selector as selector
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from homeassistant.helpers.typing import ConfigType as ConfigType

SERVICE_GENERATE_IMAGE: str
PLATFORMS: Incomplete
CONFIG_SCHEMA: Incomplete
type OpenAIConfigEntry = ConfigEntry[openai.AsyncClient]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: OpenAIConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
