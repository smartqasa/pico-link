from aionotion.client import Client as Client
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.instance_id import async_get as async_get

async def async_get_client_with_credentials(hass: HomeAssistant, email: str, password: str) -> Client: ...
async def async_get_client_with_refresh_token(hass: HomeAssistant, user_uuid: str, refresh_token: str) -> Client: ...
