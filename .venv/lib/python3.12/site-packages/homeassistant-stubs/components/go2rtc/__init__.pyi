from .const import CONF_DEBUG_UI as CONF_DEBUG_UI, DEBUG_UI_URL_MESSAGE as DEBUG_UI_URL_MESSAGE, DOMAIN as DOMAIN, HA_MANAGED_URL as HA_MANAGED_URL, RECOMMENDED_VERSION as RECOMMENDED_VERSION
from .server import Server as Server
from _typeshed import Incomplete
from go2rtc_client.ws import Go2RtcWsClient, ReceiveMessages as ReceiveMessages
from homeassistant.components.camera import Camera as Camera, CameraWebRTCProvider as CameraWebRTCProvider, WebRTCError as WebRTCError, WebRTCMessage as WebRTCMessage, WebRTCSendMessage as WebRTCSendMessage, async_register_webrtc_provider as async_register_webrtc_provider
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_SYSTEM as SOURCE_SYSTEM
from homeassistant.const import CONF_URL as CONF_URL, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import discovery_flow as discovery_flow
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.hass_dict import HassKey as HassKey
from homeassistant.util.package import is_docker_env as is_docker_env
from webrtc_models import RTCIceCandidateInit

_LOGGER: Incomplete
_SUPPORTED_STREAMS: Incomplete
CONFIG_SCHEMA: Incomplete
_DATA_GO2RTC: HassKey[str]
_RETRYABLE_ERRORS: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def _remove_go2rtc_entries(hass: HomeAssistant) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def _get_binary(hass: HomeAssistant) -> str | None: ...

class WebRTCProvider(CameraWebRTCProvider):
    _hass: Incomplete
    _url: Incomplete
    _session: Incomplete
    _rest_client: Incomplete
    _sessions: dict[str, Go2RtcWsClient]
    def __init__(self, hass: HomeAssistant, url: str) -> None: ...
    @property
    def domain(self) -> str: ...
    @callback
    def async_is_supported(self, stream_source: str) -> bool: ...
    async def async_handle_async_webrtc_offer(self, camera: Camera, offer_sdp: str, session_id: str, send_message: WebRTCSendMessage) -> None: ...
    async def async_on_webrtc_candidate(self, session_id: str, candidate: RTCIceCandidateInit) -> None: ...
    @callback
    def async_close_session(self, session_id: str) -> None: ...
