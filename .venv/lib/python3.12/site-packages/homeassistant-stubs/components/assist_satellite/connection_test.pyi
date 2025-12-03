from .const import CONNECTION_TEST_DATA as CONNECTION_TEST_DATA
from _typeshed import Incomplete
from aiohttp import web
from homeassistant.components.http import HomeAssistantView as HomeAssistantView, KEY_HASS as KEY_HASS

_LOGGER: Incomplete
CONNECTION_TEST_CONTENT_TYPE: str
CONNECTION_TEST_FILENAME: str
CONNECTION_TEST_URL_BASE: str

class ConnectionTestView(HomeAssistantView):
    requires_auth: bool
    url: Incomplete
    name: str
    async def get(self, request: web.Request, connection_id: str) -> web.Response: ...
