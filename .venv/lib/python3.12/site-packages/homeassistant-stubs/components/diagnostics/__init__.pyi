from .const import REDACTED as REDACTED
from .util import async_redact_data as async_redact_data
from _typeshed import Incomplete
from aiohttp import web
from collections.abc import Callable, Coroutine, Mapping
from dataclasses import dataclass, field
from homeassistant.components import http, websocket_api
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.device_registry import DeviceEntry
from typing import Any, Protocol

__all__ = ['REDACTED', 'async_redact_data']

@dataclass(slots=True)
class DiagnosticsPlatformData:
    config_entry_diagnostics: Callable[[HomeAssistant, ConfigEntry], Coroutine[Any, Any, Mapping[str, Any]]] | None
    device_diagnostics: Callable[[HomeAssistant, ConfigEntry, DeviceEntry], Coroutine[Any, Any, Mapping[str, Any]]] | None

@dataclass(slots=True)
class DiagnosticsData:
    platforms: dict[str, DiagnosticsPlatformData] = field(default_factory=dict)

class DiagnosticsProtocol(Protocol):
    async def async_get_config_entry_diagnostics(self, hass: HomeAssistant, config_entry: ConfigEntry) -> Mapping[str, Any]: ...
    async def async_get_device_diagnostics(self, hass: HomeAssistant, config_entry: ConfigEntry, device: DeviceEntry) -> Mapping[str, Any]: ...

class DownloadDiagnosticsView(http.HomeAssistantView):
    url: str
    extra_urls: Incomplete
    name: str
    async def get(self, request: web.Request, d_type: str, d_id: str, sub_type: str | None = None, sub_id: str | None = None) -> web.Response: ...
