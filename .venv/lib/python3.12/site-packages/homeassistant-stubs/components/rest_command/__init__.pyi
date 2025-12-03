from _typeshed import Incomplete
from homeassistant.const import CONF_HEADERS as CONF_HEADERS, CONF_METHOD as CONF_METHOD, CONF_PASSWORD as CONF_PASSWORD, CONF_PAYLOAD as CONF_PAYLOAD, CONF_TIMEOUT as CONF_TIMEOUT, CONF_URL as CONF_URL, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL, SERVICE_RELOAD as SERVICE_RELOAD
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.reload import async_integration_yaml_config as async_integration_yaml_config
from homeassistant.helpers.typing import ConfigType as ConfigType

DOMAIN: str
_LOGGER: Incomplete
DEFAULT_TIMEOUT: int
DEFAULT_METHOD: str
DEFAULT_VERIFY_SSL: bool
SUPPORT_REST_METHODS: Incomplete
CONF_CONTENT_TYPE: str
COMMAND_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
