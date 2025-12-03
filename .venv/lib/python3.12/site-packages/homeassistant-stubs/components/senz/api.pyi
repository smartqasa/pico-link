from _typeshed import Incomplete
from aiosenz import AbstractSENZAuth
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from httpx import AsyncClient as AsyncClient

class SENZConfigEntryAuth(AbstractSENZAuth):
    _oauth_session: Incomplete
    def __init__(self, httpx_async_client: AsyncClient, oauth_session: config_entry_oauth2_flow.OAuth2Session) -> None: ...
    async def get_access_token(self) -> str: ...
