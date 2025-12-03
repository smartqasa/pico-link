from _typeshed import Incomplete
from aiohttp.web import Application as Application, Request as Request, StreamResponse as StreamResponse
from collections.abc import Callable as Callable
from homeassistant.core import callback as callback
from ipaddress import IPv4Network, IPv6Network

_LOGGER: Incomplete

@callback
def async_setup_forwarded(app: Application, use_x_forwarded_for: bool | None, trusted_proxies: list[IPv4Network | IPv6Network]) -> None: ...
