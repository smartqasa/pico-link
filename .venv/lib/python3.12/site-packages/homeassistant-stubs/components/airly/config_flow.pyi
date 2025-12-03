from .const import CONF_USE_NEAREST as CONF_USE_NEAREST, DOMAIN as DOMAIN, NO_AIRLY_SENSORS as NO_AIRLY_SENSORS
from aiohttp import ClientSession as ClientSession
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_NAME as CONF_NAME
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

class AirlyFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

async def test_location(client: ClientSession, api_key: str, latitude: float, longitude: float, use_nearest: bool = False) -> bool: ...
