import pyatmo
from .const import API_SCOPES_EXCLUDED_FROM_CLOUD as API_SCOPES_EXCLUDED_FROM_CLOUD
from _typeshed import Incomplete
from aiohttp import ClientSession as ClientSession
from collections.abc import Iterable
from homeassistant.components import cloud as cloud
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow

def get_api_scopes(auth_implementation: str) -> Iterable[str]: ...

class AsyncConfigEntryNetatmoAuth(pyatmo.AbstractAsyncAuth):
    _oauth_session: Incomplete
    def __init__(self, websession: ClientSession, oauth_session: config_entry_oauth2_flow.OAuth2Session) -> None: ...
    async def async_get_access_token(self) -> str: ...
