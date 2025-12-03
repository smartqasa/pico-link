from _typeshed import Incomplete
from aiohttp.web import Application as Application, Request as Request, StreamResponse as StreamResponse
from collections.abc import Callable as Callable
from homeassistant.core import callback as callback
from typing import Final

_LOGGER: Incomplete
FILTERS: Final[Incomplete]
UNSAFE_URL_BYTES: Incomplete

@callback
def setup_security_filter(app: Application) -> None: ...
