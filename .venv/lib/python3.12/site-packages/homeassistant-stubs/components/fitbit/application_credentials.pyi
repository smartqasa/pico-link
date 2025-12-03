from .const import CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_CLIENT_SECRET as CONF_CLIENT_SECRET, OAUTH2_AUTHORIZE as OAUTH2_AUTHORIZE, OAUTH2_TOKEN as OAUTH2_TOKEN
from .exceptions import FitbitApiException as FitbitApiException, FitbitAuthException as FitbitAuthException
from _typeshed import Incomplete
from homeassistant.components.application_credentials import AuthImplementation as AuthImplementation, AuthorizationServer as AuthorizationServer, ClientCredential as ClientCredential
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

_LOGGER: Incomplete

class FitbitOAuth2Implementation(AuthImplementation):
    async def async_resolve_external_data(self, external_data: dict[str, Any]) -> dict: ...
    async def _token_request(self, data: dict) -> dict: ...
    async def _post(self, data: dict[str, Any]) -> dict[str, Any]: ...
    @property
    def _headers(self) -> dict[str, str]: ...

async def async_get_auth_implementation(hass: HomeAssistant, auth_domain: str, credential: ClientCredential) -> config_entry_oauth2_flow.AbstractOAuth2Implementation: ...
