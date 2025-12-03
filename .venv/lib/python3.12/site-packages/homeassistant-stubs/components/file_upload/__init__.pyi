import asyncio
from _typeshed import Incomplete
from aiohttp import web
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import dataclass
from homeassistant.components.http import HomeAssistantView as HomeAssistantView, KEY_HASS as KEY_HASS
from homeassistant.components.http.data_validator import RequestDataValidator as RequestDataValidator
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util import raise_if_invalid_filename as raise_if_invalid_filename
from homeassistant.util.ulid import ulid_hex as ulid_hex
from pathlib import Path

DOMAIN: str
ONE_MEGABYTE: Incomplete
MAX_SIZE: Incomplete
TEMP_DIR_NAME: Incomplete
CONFIG_SCHEMA: Incomplete

@contextmanager
def process_uploaded_file(hass: HomeAssistant, file_id: str) -> Iterator[Path]: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

@dataclass(frozen=True)
class FileUploadData:
    temp_dir: Path
    files: dict[str, str]
    @classmethod
    async def create(cls, hass: HomeAssistant) -> FileUploadData: ...
    def has_file(self, file_id: str) -> bool: ...
    def file_dir(self, file_id: str) -> Path: ...
    def file_path(self, file_id: str) -> Path: ...

class FileUploadView(HomeAssistantView):
    url: str
    name: str
    _upload_lock: asyncio.Lock | None
    @callback
    def _get_upload_lock(self) -> asyncio.Lock: ...
    async def post(self, request: web.Request) -> web.Response: ...
    async def _upload_file(self, request: web.Request) -> web.Response: ...
    async def delete(self, request: web.Request, data: dict[str, str]) -> web.Response: ...
