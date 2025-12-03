import asyncio
from .const import DATA_FFMPEG_PROXY as DATA_FFMPEG_PROXY
from _typeshed import Incomplete
from aiohttp import web
from aiohttp.abc import AbstractStreamWriter as AbstractStreamWriter, BaseRequest as BaseRequest
from dataclasses import dataclass, field
from homeassistant.components.ffmpeg import FFmpegManager as FFmpegManager
from homeassistant.components.http import HomeAssistantView as HomeAssistantView
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Final

_LOGGER: Incomplete
_MAX_CONVERSIONS_PER_DEVICE: Final[int]

def async_create_proxy_url(hass: HomeAssistant, device_id: str, media_url: str, media_format: str, rate: int | None = None, channels: int | None = None, width: int | None = None) -> str: ...

@dataclass
class FFmpegConversionInfo:
    convert_id: str
    media_url: str
    media_format: str
    rate: int | None
    channels: int | None
    width: int | None
    proc: asyncio.subprocess.Process | None = ...
    is_finished: bool = ...

@dataclass
class FFmpegProxyData:
    conversions: dict[str, list[FFmpegConversionInfo]] = field(default_factory=Incomplete)
    def async_create_proxy_url(self, device_id: str, media_url: str, media_format: str, rate: int | None, channels: int | None, width: int | None) -> str: ...

class FFmpegConvertResponse(web.StreamResponse):
    hass: Incomplete
    manager: Incomplete
    convert_info: Incomplete
    device_id: Incomplete
    proxy_data: Incomplete
    chunk_size: Incomplete
    def __init__(self, manager: FFmpegManager, convert_info: FFmpegConversionInfo, device_id: str, proxy_data: FFmpegProxyData, chunk_size: int = 2048) -> None: ...
    async def transcode(self, request: BaseRequest, writer: AbstractStreamWriter) -> None: ...
    async def _write_ffmpeg_data(self, request: BaseRequest, writer: AbstractStreamWriter, proc: asyncio.subprocess.Process) -> None: ...
    async def _dump_ffmpeg_stderr(self, proc: asyncio.subprocess.Process) -> None: ...

class FFmpegProxyView(HomeAssistantView):
    requires_auth: bool
    url: str
    name: str
    manager: Incomplete
    proxy_data: Incomplete
    def __init__(self, manager: FFmpegManager, proxy_data: FFmpegProxyData) -> None: ...
    async def get(self, request: web.Request, device_id: str, filename: str) -> web.StreamResponse: ...
