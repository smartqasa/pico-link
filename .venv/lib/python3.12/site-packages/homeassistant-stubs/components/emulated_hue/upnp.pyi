import asyncio
import socket
from .config import Config as Config
from .const import HUE_SERIAL_NUMBER as HUE_SERIAL_NUMBER, HUE_UUID as HUE_UUID
from _typeshed import Incomplete
from aiohttp import web
from homeassistant import core as core
from homeassistant.components.http import HomeAssistantView as HomeAssistantView

_LOGGER: Incomplete
BROADCAST_PORT: int
BROADCAST_ADDR: str

class DescriptionXmlView(HomeAssistantView):
    url: str
    name: str
    requires_auth: bool
    config: Incomplete
    def __init__(self, config: Config) -> None: ...
    @core.callback
    def get(self, request: web.Request) -> web.Response: ...

class UPNPResponderProtocol(asyncio.Protocol):
    transport: asyncio.DatagramTransport | None
    _loop: Incomplete
    _sock: Incomplete
    advertise_ip: Incomplete
    advertise_port: Incomplete
    _upnp_root_response: Incomplete
    _upnp_device_response: Incomplete
    def __init__(self, loop: asyncio.AbstractEventLoop, ssdp_socket: socket.socket, advertise_ip: str, advertise_port: int) -> None: ...
    def connection_made(self, transport: asyncio.BaseTransport) -> None: ...
    def connection_lost(self, exc: Exception | None) -> None: ...
    def datagram_received(self, data: bytes, addr: tuple[str, int]) -> None: ...
    def error_received(self, exc: Exception) -> None: ...
    def close(self) -> None: ...
    def _handle_request(self, decoded_data: str) -> bytes: ...
    def _prepare_response(self, search_target: str, unique_service_name: str) -> bytes: ...

async def async_create_upnp_datagram_endpoint(host_ip_addr: str, upnp_bind_multicast: bool, advertise_ip: str, advertise_port: int) -> UPNPResponderProtocol: ...
