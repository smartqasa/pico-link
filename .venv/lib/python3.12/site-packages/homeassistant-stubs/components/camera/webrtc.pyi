import abc
from . import Camera as Camera
from .const import DATA_COMPONENT as DATA_COMPONENT, DOMAIN as DOMAIN, StreamType as StreamType
from .helper import get_camera_from_entity_id as get_camera_from_entity_id
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from collections.abc import Awaitable, Callable, Iterable
from dataclasses import dataclass, field
from functools import cache
from homeassistant.components import websocket_api as websocket_api
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.deprecation import deprecated_function as deprecated_function
from homeassistant.util.hass_dict import HassKey as HassKey
from homeassistant.util.ulid import ulid as ulid
from typing import Any, Protocol
from webrtc_models import RTCConfiguration, RTCIceCandidate as RTCIceCandidate, RTCIceCandidateInit, RTCIceServer as RTCIceServer

_LOGGER: Incomplete
DATA_WEBRTC_PROVIDERS: HassKey[set[CameraWebRTCProvider]]
DATA_WEBRTC_LEGACY_PROVIDERS: HassKey[dict[str, CameraWebRTCLegacyProvider]]
DATA_ICE_SERVERS: HassKey[list[Callable[[], Iterable[RTCIceServer]]]]
_WEBRTC: str

@dataclass(frozen=True)
class WebRTCMessage:
    @classmethod
    @cache
    def _get_type(cls) -> str: ...
    def as_dict(self) -> dict[str, Any]: ...

@dataclass(frozen=True)
class WebRTCSession(WebRTCMessage):
    session_id: str

@dataclass(frozen=True)
class WebRTCAnswer(WebRTCMessage):
    answer: str

@dataclass(frozen=True)
class WebRTCCandidate(WebRTCMessage):
    candidate: RTCIceCandidate | RTCIceCandidateInit
    def as_dict(self) -> dict[str, Any]: ...

@dataclass(frozen=True)
class WebRTCError(WebRTCMessage):
    code: str
    message: str
type WebRTCSendMessage = Callable[[WebRTCMessage], None]

@dataclass(kw_only=True)
class WebRTCClientConfiguration:
    configuration: RTCConfiguration = field(default_factory=RTCConfiguration)
    data_channel: str | None = ...
    get_candidates_upfront: bool = ...
    def to_frontend_dict(self) -> dict[str, Any]: ...

class CameraWebRTCProvider(ABC, metaclass=abc.ABCMeta):
    @property
    @abstractmethod
    def domain(self) -> str: ...
    @callback
    @abstractmethod
    def async_is_supported(self, stream_source: str) -> bool: ...
    @abstractmethod
    async def async_handle_async_webrtc_offer(self, camera: Camera, offer_sdp: str, session_id: str, send_message: WebRTCSendMessage) -> None: ...
    @abstractmethod
    async def async_on_webrtc_candidate(self, session_id: str, candidate: RTCIceCandidateInit) -> None: ...
    @callback
    def async_close_session(self, session_id: str) -> None: ...

class CameraWebRTCLegacyProvider(Protocol):
    async def async_is_supported(self, stream_source: str) -> bool: ...
    async def async_handle_web_rtc_offer(self, camera: Camera, offer_sdp: str) -> str | None: ...

@callback
def async_register_webrtc_provider(hass: HomeAssistant, provider: CameraWebRTCProvider) -> Callable[[], None]: ...
async def _async_refresh_providers(hass: HomeAssistant) -> None: ...
type WsCommandWithCamera = Callable[[websocket_api.ActiveConnection, dict[str, Any], Camera], Awaitable[None]]
def require_webrtc_support(error_code: str) -> Callable[[WsCommandWithCamera], websocket_api.AsyncWebSocketCommandHandler]: ...
@websocket_api.async_response
async def ws_webrtc_offer(connection: websocket_api.ActiveConnection, msg: dict[str, Any], camera: Camera) -> None: ...
@websocket_api.async_response
async def ws_get_client_config(connection: websocket_api.ActiveConnection, msg: dict[str, Any], camera: Camera) -> None: ...
def _parse_webrtc_candidate_init(value: Any) -> RTCIceCandidateInit: ...
@websocket_api.async_response
async def ws_candidate(connection: websocket_api.ActiveConnection, msg: dict[str, Any], camera: Camera) -> None: ...
@callback
def async_register_ws(hass: HomeAssistant) -> None: ...
async def async_get_supported_provider(hass: HomeAssistant, camera: Camera) -> CameraWebRTCProvider | None: ...
async def async_get_supported_legacy_provider(hass: HomeAssistant, camera: Camera) -> CameraWebRTCLegacyProvider | None: ...
@callback
def async_register_ice_servers(hass: HomeAssistant, get_ice_server_fn: Callable[[], Iterable[RTCIceServer]]) -> Callable[[], None]: ...

_RTSP_PREFIXES: Incomplete
type RtspToWebRtcProviderType = Callable[[str, str, str], Awaitable[str | None]]

class _CameraRtspToWebRTCProvider(CameraWebRTCLegacyProvider):
    _fn: Incomplete
    def __init__(self, fn: RtspToWebRtcProviderType) -> None: ...
    async def async_is_supported(self, stream_source: str) -> bool: ...
    async def async_handle_web_rtc_offer(self, camera: Camera, offer_sdp: str) -> str | None: ...

def async_register_rtsp_to_web_rtc_provider(hass: HomeAssistant, domain: str, provider: RtspToWebRtcProviderType) -> Callable[[], None]: ...
@callback
def _async_check_conflicting_legacy_provider(hass: HomeAssistant) -> None: ...
