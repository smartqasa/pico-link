from aiohttp.web import Application as Application, Request as Request, StreamResponse as StreamResponse
from collections.abc import Callable as Callable
from homeassistant.core import callback as callback

@callback
def setup_headers(app: Application, use_x_frame_options: bool) -> None: ...
