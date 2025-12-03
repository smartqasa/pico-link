from .const import KEY_HASS as KEY_HASS
from .view import HomeAssistantView as HomeAssistantView
from _typeshed import Incomplete
from aiohttp.web import Application as Application, Request as Request, Response as Response, StreamResponse as StreamResponse, middleware
from collections.abc import Awaitable, Callable as Callable, Coroutine
from datetime import datetime
from homeassistant.config import load_yaml_config_file as load_yaml_config_file
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.hassio import get_supervisor_ip as get_supervisor_ip, is_hassio as is_hassio
from homeassistant.util import yaml as yaml
from ipaddress import IPv4Address, IPv6Address
from typing import Any, Concatenate, Final

_LOGGER: Final[Incomplete]
KEY_BAN_MANAGER: Incomplete
KEY_FAILED_LOGIN_ATTEMPTS: Incomplete
KEY_LOGIN_THRESHOLD: Incomplete
NOTIFICATION_ID_BAN: Final[str]
NOTIFICATION_ID_LOGIN: Final[str]
IP_BANS_FILE: Final[str]
ATTR_BANNED_AT: Final[str]
SCHEMA_IP_BAN_ENTRY: Final[Incomplete]

@callback
def setup_bans(hass: HomeAssistant, app: Application, login_threshold: int) -> None: ...
@middleware
async def ban_middleware(request: Request, handler: Callable[[Request], Awaitable[StreamResponse]]) -> StreamResponse: ...
def log_invalid_auth[_HassViewT: HomeAssistantView, **_P](func: Callable[Concatenate[_HassViewT, Request, _P], Awaitable[Response]]) -> Callable[Concatenate[_HassViewT, Request, _P], Coroutine[Any, Any, Response]]: ...
async def process_wrong_login(request: Request) -> None: ...
@callback
def process_success_login(request: Request) -> None: ...

class IpBan:
    ip_address: Incomplete
    banned_at: Incomplete
    def __init__(self, ip_ban: str | IPv4Address | IPv6Address, banned_at: datetime | None = None) -> None: ...

class IpBanManager:
    hass: Incomplete
    path: Incomplete
    ip_bans_lookup: dict[IPv4Address | IPv6Address, IpBan]
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_load(self) -> None: ...
    def _add_ban(self, ip_ban: IpBan) -> None: ...
    async def async_add_ban(self, remote_addr: IPv4Address | IPv6Address) -> None: ...
