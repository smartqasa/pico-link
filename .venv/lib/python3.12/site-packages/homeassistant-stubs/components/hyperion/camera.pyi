from . import get_hyperion_device_id as get_hyperion_device_id, get_hyperion_unique_id as get_hyperion_unique_id, listen_for_instance_updates as listen_for_instance_updates
from .const import CONF_INSTANCE_CLIENTS as CONF_INSTANCE_CLIENTS, DOMAIN as DOMAIN, HYPERION_MANUFACTURER_NAME as HYPERION_MANUFACTURER_NAME, HYPERION_MODEL_NAME as HYPERION_MODEL_NAME, SIGNAL_ENTITY_REMOVE as SIGNAL_ENTITY_REMOVE, TYPE_HYPERION_CAMERA as TYPE_HYPERION_CAMERA
from _typeshed import Incomplete
from aiohttp import web as web
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from homeassistant.components.camera import Camera as Camera, DEFAULT_CONTENT_TYPE as DEFAULT_CONTENT_TYPE, async_get_still_stream as async_get_still_stream
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from hyperion import client as client
from typing import Any

IMAGE_STREAM_JPG_SENTINEL: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HyperionCamera(Camera):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _device_id: Incomplete
    _instance_name: Incomplete
    _client: Incomplete
    _image_cond: Incomplete
    _image: bytes | None
    _image_stream_clients: int
    _client_callbacks: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, server_id: str, instance_num: int, instance_name: str, hyperion_client: client.HyperionClient) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def available(self) -> bool: ...
    async def _update_imagestream(self, img: dict[str, Any] | None = None) -> None: ...
    async def _async_wait_for_camera_image(self) -> bytes | None: ...
    _attr_is_streaming: bool
    async def _start_image_streaming_for_client(self) -> bool: ...
    async def _stop_image_streaming_for_client(self) -> None: ...
    @asynccontextmanager
    async def _image_streaming(self) -> AsyncGenerator: ...
    async def async_camera_image(self, width: int | None = None, height: int | None = None) -> bytes | None: ...
    async def handle_async_mjpeg_stream(self, request: web.Request) -> web.StreamResponse | None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...

CAMERA_TYPES: Incomplete
