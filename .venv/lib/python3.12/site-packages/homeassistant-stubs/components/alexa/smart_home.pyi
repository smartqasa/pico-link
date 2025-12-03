from .auth import Auth as Auth
from .config import AbstractConfig as AbstractConfig
from .const import API_DIRECTIVE as API_DIRECTIVE, API_HEADER as API_HEADER, CONF_ENDPOINT as CONF_ENDPOINT, CONF_ENTITY_CONFIG as CONF_ENTITY_CONFIG, CONF_FILTER as CONF_FILTER, CONF_LOCALE as CONF_LOCALE, EVENT_ALEXA_SMART_HOME as EVENT_ALEXA_SMART_HOME
from .diagnostics import async_redact_auth_data as async_redact_auth_data
from .errors import AlexaBridgeUnreachableError as AlexaBridgeUnreachableError, AlexaError as AlexaError
from .handlers import HANDLERS as HANDLERS
from .state_report import AlexaDirective as AlexaDirective
from _typeshed import Incomplete
from aiohttp import web as web
from homeassistant import core as core
from homeassistant.auth.models import User as User
from homeassistant.components.http import HomeAssistantRequest as HomeAssistantRequest, HomeAssistantView as HomeAssistantView, KEY_HASS as KEY_HASS
from homeassistant.const import CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_CLIENT_SECRET as CONF_CLIENT_SECRET
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any
from yarl import URL as URL

_LOGGER: Incomplete
SMART_HOME_HTTP_ENDPOINT: str

class AlexaConfig(AbstractConfig):
    _auth: Auth | None
    _config: Incomplete
    def __init__(self, hass: HomeAssistant, config: ConfigType) -> None: ...
    @property
    def supports_auth(self) -> bool: ...
    @property
    def should_report_state(self) -> bool: ...
    @property
    def endpoint(self) -> str | URL | None: ...
    @property
    def entity_config(self) -> dict[str, Any]: ...
    @property
    def locale(self) -> str | None: ...
    @core.callback
    def user_identifier(self) -> str: ...
    @core.callback
    def should_expose(self, entity_id: str) -> bool: ...
    @core.callback
    def async_invalidate_access_token(self) -> None: ...
    async def async_get_access_token(self) -> str | None: ...
    async def async_accept_grant(self, code: str) -> str | None: ...

async def async_setup(hass: HomeAssistant, config: ConfigType) -> None: ...

class SmartHomeView(HomeAssistantView):
    url = SMART_HOME_HTTP_ENDPOINT
    name: str
    smart_home_config: Incomplete
    def __init__(self, smart_home_config: AlexaConfig) -> None: ...
    async def post(self, request: HomeAssistantRequest) -> web.Response | bytes: ...

async def async_handle_message(hass: HomeAssistant, config: AbstractConfig, request: dict[str, Any], context: Context | None = None, enabled: bool = True) -> dict[str, Any]: ...
