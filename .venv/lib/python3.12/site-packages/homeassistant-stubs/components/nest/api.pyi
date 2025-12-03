from .const import API_URL as API_URL, CONF_PROJECT_ID as CONF_PROJECT_ID, CONF_SUBSCRIBER_ID as CONF_SUBSCRIBER_ID, CONF_SUBSCRIPTION_NAME as CONF_SUBSCRIPTION_NAME, OAUTH2_TOKEN as OAUTH2_TOKEN, SDM_SCOPES as SDM_SCOPES
from _typeshed import Incomplete
from aiohttp import ClientSession as ClientSession
from google.oauth2.credentials import Credentials
from google_nest_sdm.admin_client import AdminClient
from google_nest_sdm.auth import AbstractAuth
from google_nest_sdm.google_nest_subscriber import GoogleNestSubscriber
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import aiohttp_client as aiohttp_client, config_entry_oauth2_flow as config_entry_oauth2_flow

_LOGGER: Incomplete

class AsyncConfigEntryAuth(AbstractAuth):
    _oauth_session: Incomplete
    _client_id: Incomplete
    _client_secret: Incomplete
    def __init__(self, websession: ClientSession, oauth_session: config_entry_oauth2_flow.OAuth2Session, client_id: str, client_secret: str) -> None: ...
    async def async_get_access_token(self) -> str: ...
    async def async_get_creds(self) -> Credentials: ...

class AccessTokenAuthImpl(AbstractAuth):
    _access_token: Incomplete
    def __init__(self, websession: ClientSession, access_token: str, host: str) -> None: ...
    async def async_get_access_token(self) -> str: ...
    async def async_get_creds(self) -> Credentials: ...

async def new_subscriber(hass: HomeAssistant, entry: ConfigEntry) -> GoogleNestSubscriber | None: ...
def new_subscriber_with_token(hass: HomeAssistant, access_token: str, project_id: str, subscription_name: str) -> GoogleNestSubscriber: ...
def new_pubsub_admin_client(hass: HomeAssistant, access_token: str, cloud_project_id: str) -> AdminClient: ...
