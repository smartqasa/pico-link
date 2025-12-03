from .api import GoogleHybridAuth as GoogleHybridAuth
from _typeshed import Incomplete
from homeassistant.components.application_credentials import AuthorizationServer as AuthorizationServer, ClientCredential as ClientCredential
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow

AUTHORIZATION_SERVER: Incomplete

async def async_get_auth_implementation(hass: HomeAssistant, auth_domain: str, credential: ClientCredential) -> config_entry_oauth2_flow.AbstractOAuth2Implementation: ...
async def async_get_description_placeholders(hass: HomeAssistant) -> dict[str, str]: ...
