import aiohttp
from _typeshed import Incomplete
from google_photos_library_api import api
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow

class AsyncConfigEntryAuth(api.AbstractAuth):
    _session: Incomplete
    def __init__(self, websession: aiohttp.ClientSession, oauth_session: config_entry_oauth2_flow.OAuth2Session) -> None: ...
    async def async_get_access_token(self) -> str: ...

class AsyncConfigFlowAuth(api.AbstractAuth):
    _token: Incomplete
    def __init__(self, websession: aiohttp.ClientSession, token: str) -> None: ...
    async def async_get_access_token(self) -> str: ...
