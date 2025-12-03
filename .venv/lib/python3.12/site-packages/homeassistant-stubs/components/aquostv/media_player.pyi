import sharp_aquos_rc
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.media_player import MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_TIMEOUT as CONF_TIMEOUT, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any, Concatenate

_LOGGER: Incomplete
DEFAULT_NAME: str
DEFAULT_PORT: int
DEFAULT_USERNAME: str
DEFAULT_PASSWORD: str
DEFAULT_TIMEOUT: float
DEFAULT_RETRIES: int
PLATFORM_SCHEMA: Incomplete
SOURCES: Incomplete

def setup_platform(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...
def _retry[_SharpAquosTVDeviceT: SharpAquosTVDevice, **_P](func: Callable[Concatenate[_SharpAquosTVDeviceT, _P], Any]) -> Callable[Concatenate[_SharpAquosTVDeviceT, _P], None]: ...

class SharpAquosTVDevice(MediaPlayerEntity):
    _attr_source_list: Incomplete
    _attr_supported_features: Incomplete
    _power_on_enabled: Incomplete
    _attr_name: Incomplete
    _remote: Incomplete
    def __init__(self, name: str, remote: sharp_aquos_rc.TV, power_on_enabled: bool = False) -> None: ...
    _attr_state: Incomplete
    def set_state(self, state: MediaPlayerState) -> None: ...
    _attr_is_volume_muted: bool
    _attr_source: Incomplete
    _attr_volume_level: Incomplete
    @_retry
    def update(self) -> None: ...
    @_retry
    def turn_off(self) -> None: ...
    @_retry
    def volume_up(self) -> None: ...
    @_retry
    def volume_down(self) -> None: ...
    @_retry
    def set_volume_level(self, volume: float) -> None: ...
    @_retry
    def mute_volume(self, mute: bool) -> None: ...
    @_retry
    def turn_on(self) -> None: ...
    @_retry
    def media_play_pause(self) -> None: ...
    @_retry
    def media_play(self) -> None: ...
    @_retry
    def media_pause(self) -> None: ...
    @_retry
    def media_next_track(self) -> None: ...
    @_retry
    def media_previous_track(self) -> None: ...
    def select_source(self, source: str) -> None: ...
