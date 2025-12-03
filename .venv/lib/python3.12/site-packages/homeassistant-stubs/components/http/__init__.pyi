import asyncio
import ssl
from .auth import async_setup_auth as async_setup_auth
from .ban import setup_bans as setup_bans
from .const import DOMAIN as DOMAIN, KEY_HASS_REFRESH_TOKEN_ID as KEY_HASS_REFRESH_TOKEN_ID, KEY_HASS_USER as KEY_HASS_USER
from .cors import setup_cors as setup_cors
from .decorators import require_admin as require_admin
from .forwarded import async_setup_forwarded as async_setup_forwarded
from .headers import setup_headers as setup_headers
from .request_context import setup_request_context as setup_request_context
from .security_filter import setup_security_filter as setup_security_filter
from .static import CACHE_HEADERS as CACHE_HEADERS, CachingStaticResource as CachingStaticResource
from .web_runner import HomeAssistantTCPSite as HomeAssistantTCPSite
from _typeshed import Incomplete
from aiohttp import web
from aiohttp.abc import AbstractStreamWriter as AbstractStreamWriter
from aiohttp.http_parser import RawRequestMessage as RawRequestMessage
from aiohttp.streams import StreamReader as StreamReader
from aiohttp.typedefs import JSONDecoder as JSONDecoder, StrOrURL as StrOrURL
from aiohttp.web_exceptions import HTTPRedirection as HTTPRedirection
from aiohttp.web_protocol import RequestHandler as RequestHandler
from collections.abc import Collection
from dataclasses import dataclass
from homeassistant.components.network import async_get_source_ip as async_get_source_ip
from homeassistant.const import EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, SERVER_PORT as SERVER_PORT
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import frame as frame, storage as storage
from homeassistant.helpers.http import HomeAssistantView as HomeAssistantView, KEY_ALLOW_CONFIGURED_CORS as KEY_ALLOW_CONFIGURED_CORS, KEY_AUTHENTICATED as KEY_AUTHENTICATED, KEY_HASS as KEY_HASS, current_request as current_request
from homeassistant.helpers.importlib import async_import_module as async_import_module
from homeassistant.helpers.network import NoURLAvailableError as NoURLAvailableError, get_url as get_url
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.setup import SetupPhases as SetupPhases, async_start_setup as async_start_setup, async_when_setup_or_start as async_when_setup_or_start
from homeassistant.util.async_ import create_eager_task as create_eager_task
from homeassistant.util.json import json_loads as json_loads
from ipaddress import IPv4Network, IPv6Network
from typing import Any, Final, TypedDict

CONF_SERVER_HOST: Final[str]
CONF_SERVER_PORT: Final[str]
CONF_BASE_URL: Final[str]
CONF_SSL_CERTIFICATE: Final[str]
CONF_SSL_PEER_CERTIFICATE: Final[str]
CONF_SSL_KEY: Final[str]
CONF_CORS_ORIGINS: Final[str]
CONF_USE_X_FORWARDED_FOR: Final[str]
CONF_USE_X_FRAME_OPTIONS: Final[str]
CONF_TRUSTED_PROXIES: Final[str]
CONF_LOGIN_ATTEMPTS_THRESHOLD: Final[str]
CONF_IP_BAN_ENABLED: Final[str]
CONF_SSL_PROFILE: Final[str]
SSL_MODERN: Final[str]
SSL_INTERMEDIATE: Final[str]
_LOGGER: Final[Incomplete]
DEFAULT_DEVELOPMENT: Final[str]
DEFAULT_CORS: Final[list[str]]
NO_LOGIN_ATTEMPT_THRESHOLD: Final[int]
MAX_CLIENT_SIZE: Final[Incomplete]
MAX_LINE_SIZE: Final[int]
STORAGE_KEY: Final[Incomplete]
STORAGE_VERSION: Final[int]
SAVE_DELAY: Final[int]
_HAS_IPV6: Incomplete
_DEFAULT_BIND: Incomplete
HTTP_SCHEMA: Final[Incomplete]
CONFIG_SCHEMA: Final[Incomplete]

@dataclass(slots=True)
class StaticPathConfig:
    url_path: str
    path: str
    cache_headers: bool = ...

_STATIC_CLASSES: Incomplete

class ConfData(TypedDict, total=False):
    server_host: list[str]
    server_port: int
    base_url: str
    ssl_certificate: str
    ssl_peer_certificate: str
    ssl_key: str
    cors_allowed_origins: list[str]
    use_x_forwarded_for: bool
    use_x_frame_options: bool
    trusted_proxies: list[IPv4Network | IPv6Network]
    login_attempts_threshold: int
    ip_ban_enabled: bool
    ssl_profile: str

@bind_hass
async def async_get_last_config(hass: HomeAssistant) -> dict[str, Any] | None: ...

class ApiConfig:
    local_ip: Incomplete
    host: Incomplete
    port: Incomplete
    use_ssl: Incomplete
    def __init__(self, local_ip: str, host: str, port: int, use_ssl: bool) -> None: ...

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class HomeAssistantRequest(web.Request):
    async def json(self, *, loads: JSONDecoder = ...) -> Any: ...

class HomeAssistantApplication(web.Application):
    def _make_request(self, message: RawRequestMessage, payload: StreamReader, protocol: RequestHandler, writer: AbstractStreamWriter, task: asyncio.Task[None], _cls: type[web.Request] = ...) -> web.Request: ...

async def _serve_file_with_cache_headers(path: str, request: web.Request) -> web.FileResponse: ...
async def _serve_file(path: str, request: web.Request) -> web.FileResponse: ...

class HomeAssistantHTTP:
    app: Incomplete
    hass: Incomplete
    ssl_certificate: Incomplete
    ssl_peer_certificate: Incomplete
    ssl_key: Incomplete
    server_host: Incomplete
    server_port: Incomplete
    trusted_proxies: Incomplete
    ssl_profile: Incomplete
    runner: web.AppRunner | None
    site: HomeAssistantTCPSite | None
    context: ssl.SSLContext | None
    def __init__(self, hass: HomeAssistant, ssl_certificate: str | None, ssl_peer_certificate: str | None, ssl_key: str | None, server_host: list[str] | None, server_port: int, trusted_proxies: list[IPv4Network | IPv6Network], ssl_profile: str) -> None: ...
    async def async_initialize(self, *, cors_origins: list[str], use_x_forwarded_for: bool, login_threshold: int, is_ban_enabled: bool, use_x_frame_options: bool) -> None: ...
    def register_view(self, view: HomeAssistantView | type[HomeAssistantView]) -> None: ...
    def register_redirect(self, url: str, redirect_to: StrOrURL, *, redirect_exc: type[HTTPRedirection] = ...) -> None: ...
    def _make_static_resources(self, configs: Collection[StaticPathConfig]) -> dict[str, CachingStaticResource | web.StaticResource | None]: ...
    async def async_register_static_paths(self, configs: Collection[StaticPathConfig]) -> None: ...
    @callback
    def _async_register_static_paths(self, configs: Collection[StaticPathConfig], resources: dict[str, CachingStaticResource | web.StaticResource | None]) -> None: ...
    def register_static_path(self, url_path: str, path: str, cache_headers: bool = True) -> None: ...
    def _create_ssl_context(self) -> ssl.SSLContext | None: ...
    def _create_emergency_ssl_context(self) -> ssl.SSLContext: ...
    async def start(self) -> None: ...
    async def stop(self) -> None: ...

async def start_http_server_and_save_config(hass: HomeAssistant, conf: dict, server: HomeAssistantHTTP) -> None: ...
