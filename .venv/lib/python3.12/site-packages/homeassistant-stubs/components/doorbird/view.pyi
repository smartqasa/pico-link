from .const import API_URL as API_URL, DOMAIN as DOMAIN
from .util import get_door_station_by_token as get_door_station_by_token
from _typeshed import Incomplete
from aiohttp import web
from homeassistant.components.http import HomeAssistantView as HomeAssistantView, KEY_HASS as KEY_HASS
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send

class DoorBirdRequestView(HomeAssistantView):
    requires_auth: bool
    url = API_URL
    name: Incomplete
    extra_urls: Incomplete
    async def get(self, request: web.Request, event: str) -> web.Response: ...
