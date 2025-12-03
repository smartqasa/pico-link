from .config import Config as Config
from _typeshed import Incomplete
from aiohttp import web as web
from collections.abc import Iterable
from homeassistant import core as core
from homeassistant.components import climate as climate, cover as cover, fan as fan, humidifier as humidifier, light as light, media_player as media_player, scene as scene, script as script
from homeassistant.components.climate import ClimateEntityFeature as ClimateEntityFeature, SERVICE_SET_TEMPERATURE as SERVICE_SET_TEMPERATURE
from homeassistant.components.cover import ATTR_CURRENT_POSITION as ATTR_CURRENT_POSITION, ATTR_POSITION as ATTR_POSITION, CoverEntityFeature as CoverEntityFeature
from homeassistant.components.fan import ATTR_PERCENTAGE as ATTR_PERCENTAGE, FanEntityFeature as FanEntityFeature
from homeassistant.components.http import HomeAssistantView as HomeAssistantView, KEY_HASS as KEY_HASS
from homeassistant.components.humidifier import ATTR_HUMIDITY as ATTR_HUMIDITY, SERVICE_SET_HUMIDITY as SERVICE_SET_HUMIDITY
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP_KELVIN as ATTR_COLOR_TEMP_KELVIN, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_TRANSITION as ATTR_TRANSITION, ATTR_XY_COLOR as ATTR_XY_COLOR, ColorMode as ColorMode, LightEntityFeature as LightEntityFeature
from homeassistant.components.media_player import ATTR_MEDIA_VOLUME_LEVEL as ATTR_MEDIA_VOLUME_LEVEL, MediaPlayerEntityFeature as MediaPlayerEntityFeature
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, ATTR_TEMPERATURE as ATTR_TEMPERATURE, SERVICE_CLOSE_COVER as SERVICE_CLOSE_COVER, SERVICE_OPEN_COVER as SERVICE_OPEN_COVER, SERVICE_SET_COVER_POSITION as SERVICE_SET_COVER_POSITION, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, SERVICE_VOLUME_SET as SERVICE_VOLUME_SET, STATE_CLOSED as STATE_CLOSED, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE
from homeassistant.core import Event as Event, EventStateChangedData as EventStateChangedData, State as State
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.util.json import json_loads as json_loads
from homeassistant.util.network import is_local as is_local
from typing import Any

_LOGGER: Incomplete
_OFF_STATES: dict[str, str]
STATE_CHANGE_WAIT_TIMEOUT: float
STATE_CACHED_TIMEOUT: float
STATE_BRIGHTNESS: str
STATE_COLORMODE: str
STATE_HUE: str
STATE_SATURATION: str
STATE_COLOR_TEMP: str
STATE_TRANSITION: str
STATE_XY: str
HUE_API_STATE_ON: str
HUE_API_STATE_BRI: str
HUE_API_STATE_COLORMODE: str
HUE_API_STATE_HUE: str
HUE_API_STATE_SAT: str
HUE_API_STATE_CT: str
HUE_API_STATE_XY: str
HUE_API_STATE_EFFECT: str
HUE_API_STATE_TRANSITION: str
HUE_API_STATE_BRI_MIN: int
HUE_API_STATE_BRI_MAX: int
HUE_API_STATE_HUE_MIN: int
HUE_API_STATE_HUE_MAX: int
HUE_API_STATE_SAT_MIN: int
HUE_API_STATE_SAT_MAX: int
HUE_API_STATE_CT_MIN: int
HUE_API_STATE_CT_MAX: int
HUE_API_USERNAME: str
UNAUTHORIZED_USER: Incomplete
DIMMABLE_SUPPORTED_FEATURES_BY_DOMAIN: Incomplete
ENTITY_FEATURES_BY_DOMAIN: Incomplete

def _remote_is_allowed(address: str) -> bool: ...

class HueUnauthorizedUser(HomeAssistantView):
    url: str
    name: str
    extra_urls: Incomplete
    requires_auth: bool
    async def get(self, request: web.Request) -> web.Response: ...

class HueUsernameView(HomeAssistantView):
    url: str
    name: str
    extra_urls: Incomplete
    requires_auth: bool
    async def post(self, request: web.Request) -> web.Response: ...

class HueAllGroupsStateView(HomeAssistantView):
    url: str
    name: str
    requires_auth: bool
    config: Incomplete
    def __init__(self, config: Config) -> None: ...
    @core.callback
    def get(self, request: web.Request, username: str) -> web.Response: ...

class HueGroupView(HomeAssistantView):
    url: str
    name: str
    requires_auth: bool
    config: Incomplete
    def __init__(self, config: Config) -> None: ...
    @core.callback
    def put(self, request: web.Request, username: str) -> web.Response: ...

class HueAllLightsStateView(HomeAssistantView):
    url: str
    name: str
    requires_auth: bool
    config: Incomplete
    def __init__(self, config: Config) -> None: ...
    @core.callback
    def get(self, request: web.Request, username: str) -> web.Response: ...

class HueFullStateView(HomeAssistantView):
    url: str
    name: str
    requires_auth: bool
    config: Incomplete
    def __init__(self, config: Config) -> None: ...
    @core.callback
    def get(self, request: web.Request, username: str) -> web.Response: ...

class HueConfigView(HomeAssistantView):
    url: str
    extra_urls: Incomplete
    name: str
    requires_auth: bool
    config: Incomplete
    def __init__(self, config: Config) -> None: ...
    @core.callback
    def get(self, request: web.Request, username: str = '') -> web.Response: ...

class HueOneLightStateView(HomeAssistantView):
    url: str
    name: str
    requires_auth: bool
    config: Incomplete
    def __init__(self, config: Config) -> None: ...
    @core.callback
    def get(self, request: web.Request, username: str, entity_id: str) -> web.Response: ...

class HueOneLightChangeView(HomeAssistantView):
    url: str
    name: str
    requires_auth: bool
    config: Incomplete
    def __init__(self, config: Config) -> None: ...
    async def put(self, request: web.Request, username: str, entity_number: str) -> web.Response: ...

def get_entity_state_dict(config: Config, entity: State) -> dict[str, Any]: ...
def _build_entity_state_dict(entity: State) -> dict[str, Any]: ...
def _clamp_values(data: dict[str, Any]) -> None: ...
def _entity_unique_id(entity_id: str) -> str: ...
def state_to_json(config: Config, state: State) -> dict[str, Any]: ...
def state_supports_hue_brightness(state: State, color_modes: Iterable[ColorMode]) -> bool: ...
def create_hue_success_response(entity_number: str, attr: str, value: str) -> dict[str, Any]: ...
def create_config_model(config: Config, request: web.Request) -> dict[str, Any]: ...
def create_list_of_entities(config: Config, request: web.Request) -> dict[str, Any]: ...
def hue_brightness_to_hass(value: int) -> int: ...
def hass_to_hue_brightness(value: int) -> int: ...
def _hass_to_hue_state(entity: State) -> bool: ...
async def wait_for_state_change_or_timeout(hass: core.HomeAssistant, entity_id: str, timeout: float) -> None: ...
