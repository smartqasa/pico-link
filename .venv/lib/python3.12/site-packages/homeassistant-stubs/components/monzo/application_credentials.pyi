from homeassistant.components.application_credentials import AuthorizationServer as AuthorizationServer
from homeassistant.core import HomeAssistant as HomeAssistant

OAUTH2_AUTHORIZE: str
OAUTH2_TOKEN: str

async def async_get_authorization_server(hass: HomeAssistant) -> AuthorizationServer: ...
