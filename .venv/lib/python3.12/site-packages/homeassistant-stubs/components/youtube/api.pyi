from _typeshed import Incomplete
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from youtubeaio.youtube import YouTube

class AsyncConfigEntryAuth:
    youtube: YouTube | None
    oauth_session: Incomplete
    hass: Incomplete
    def __init__(self, hass: HomeAssistant, oauth2_session: config_entry_oauth2_flow.OAuth2Session) -> None: ...
    @property
    def access_token(self) -> str: ...
    async def check_and_refresh_token(self) -> str: ...
    async def get_resource(self) -> YouTube: ...
