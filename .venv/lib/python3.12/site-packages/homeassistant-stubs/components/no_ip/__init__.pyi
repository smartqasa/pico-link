import aiohttp
from _typeshed import Incomplete
from homeassistant.const import CONF_DOMAIN as CONF_DOMAIN, CONF_PASSWORD as CONF_PASSWORD, CONF_TIMEOUT as CONF_TIMEOUT, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import SERVER_SOFTWARE as SERVER_SOFTWARE, async_get_clientsession as async_get_clientsession
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
DOMAIN: str
EMAIL: str
INTERVAL: Incomplete
DEFAULT_TIMEOUT: int
NO_IP_ERRORS: Incomplete
UPDATE_URL: str
HA_USER_AGENT: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def _update_no_ip(hass: HomeAssistant, session: aiohttp.ClientSession, domain: str, auth_str: bytes, timeout: int) -> bool: ...
