import asyncio
from .entity import EsphomeEntity as EsphomeEntity, platform_async_setup_entry as platform_async_setup_entry
from _typeshed import Incomplete
from aioesphomeapi import CameraInfo, CameraState
from aiohttp import web as web
from collections.abc import Callable as Callable
from homeassistant.components import camera as camera
from homeassistant.components.camera import Camera as Camera
from homeassistant.core import callback as callback
from typing import Any

class EsphomeCamera(Camera, EsphomeEntity[CameraInfo, CameraState]):
    _loop: Incomplete
    _image_futures: list[asyncio.Future[bool | None]]
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @callback
    def _set_futures(self, result: bool) -> None: ...
    @callback
    def _on_device_update(self) -> None: ...
    @callback
    def _on_state_update(self) -> None: ...
    async def async_camera_image(self, width: int | None = None, height: int | None = None) -> bytes | None: ...
    async def _async_request_image(self, request_method: Callable[[], None]) -> bytes | None: ...
    async def handle_async_mjpeg_stream(self, request: web.Request) -> web.StreamResponse: ...

async_setup_entry: Incomplete
