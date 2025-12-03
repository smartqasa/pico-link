import axis
from ..const import LOGGER as LOGGER
from ..errors import AuthenticationRequired as AuthenticationRequired, CannotConnect as CannotConnect
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_PROTOCOL as CONF_PROTOCOL, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from types import MappingProxyType
from typing import Any

async def get_axis_api(hass: HomeAssistant, config: MappingProxyType[str, Any]) -> axis.AxisDevice: ...
