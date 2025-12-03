from .util import get_host as get_host
from _typeshed import Incomplete
from aiohttp import web
from homeassistant.components.http import HomeAssistantView as HomeAssistantView
from homeassistant.components.media_source import Unresolvable as Unresolvable
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.util.ssl import SSLCipherList as SSLCipherList

_LOGGER: Incomplete

@callback
def async_generate_playback_proxy_url(config_entry_id: str, channel: int, filename: str, stream_res: str, vod_type: str) -> str: ...

class PlaybackProxyView(HomeAssistantView):
    requires_auth: bool
    url: str
    name: str
    hass: Incomplete
    session: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def get(self, request: web.Request, config_entry_id: str, channel: str, stream_res: str, vod_type: str, filename: str, retry: int = 2) -> web.StreamResponse: ...
