from aiohttp.web import Application as Application, Request as Request, StreamResponse as StreamResponse
from collections.abc import Callable as Callable
from contextvars import ContextVar
from homeassistant.core import callback as callback
from homeassistant.helpers.http import current_request as current_request

@callback
def setup_request_context(app: Application, context: ContextVar[Request | None]) -> None: ...
