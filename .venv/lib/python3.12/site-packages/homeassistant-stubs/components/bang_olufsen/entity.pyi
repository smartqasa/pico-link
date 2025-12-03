from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from mozart_api.models import PlaybackContentMetadata, PlaybackProgress, RenderingState, Source, VolumeState
from mozart_api.mozart_client import MozartClient as MozartClient

class BangOlufsenBase:
    _client: Incomplete
    entry: ConfigEntry
    _host: str
    _unique_id: str
    _playback_metadata: PlaybackContentMetadata
    _playback_progress: PlaybackProgress
    _playback_source: Source
    _playback_state: RenderingState
    _source_change: Source
    _volume: VolumeState
    def __init__(self, entry: ConfigEntry, client: MozartClient) -> None: ...

class BangOlufsenEntity(Entity, BangOlufsenBase):
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _attr_device_info: Incomplete
    def __init__(self, entry: ConfigEntry, client: MozartClient) -> None: ...
    _attr_available: Incomplete
    @callback
    def _async_update_connection_state(self, connection_state: bool) -> None: ...
