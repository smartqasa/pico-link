import aiounifi
from ..const import CONF_SITE_ID as CONF_SITE_ID, LOGGER as LOGGER
from ..errors import AuthenticationRequired as AuthenticationRequired, CannotConnect as CannotConnect
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import aiohttp_client as aiohttp_client
from types import MappingProxyType
from typing import Any

async def get_unifi_api(hass: HomeAssistant, config: MappingProxyType[str, Any]) -> aiounifi.Controller: ...
