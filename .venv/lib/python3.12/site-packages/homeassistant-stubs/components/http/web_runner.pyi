from _typeshed import Incomplete
from aiohttp import web
from ssl import SSLContext

class HomeAssistantTCPSite(web.BaseSite):
    __slots__: Incomplete
    _host: Incomplete
    _port: Incomplete
    _reuse_address: Incomplete
    _reuse_port: Incomplete
    def __init__(self, runner: web.BaseRunner, host: str | list[str] | None, port: int, *, ssl_context: SSLContext | None = None, backlog: int = 128, reuse_address: bool | None = None, reuse_port: bool | None = None) -> None: ...
    @property
    def name(self) -> str: ...
    _server: Incomplete
    async def start(self) -> None: ...
