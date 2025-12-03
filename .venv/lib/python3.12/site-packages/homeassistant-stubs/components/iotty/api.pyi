from _typeshed import Incomplete
from aiohttp import ClientSession as ClientSession
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from iottycloud.cloudapi import CloudApi
from typing import Any

OAUTH2_CLIENT_ID: str
IOTTYAPI_BASE: str

class IottyProxy(CloudApi):
    _oauth_session: Incomplete
    _hass: Incomplete
    def __init__(self, hass: HomeAssistant, websession: ClientSession, oauth_session: config_entry_oauth2_flow.OAuth2Session) -> None: ...
    async def async_get_access_token(self) -> Any: ...
