from . import update_client_key as update_client_key
from .const import ATTR_PAYLOAD as ATTR_PAYLOAD, ATTR_SOUND_OUTPUT as ATTR_SOUND_OUTPUT, CONF_SOURCES as CONF_SOURCES, DATA_CONFIG_ENTRY as DATA_CONFIG_ENTRY, DOMAIN as DOMAIN, LIVE_TV_APP_ID as LIVE_TV_APP_ID, WEBOSTV_EXCEPTIONS as WEBOSTV_EXCEPTIONS
from .triggers.turn_on import async_get_turn_on_trigger as async_get_turn_on_trigger
from _typeshed import Incomplete
from aiowebostv import WebOsClient as WebOsClient
from collections.abc import Awaitable, Callable as Callable, Coroutine
from homeassistant import util as util
from homeassistant.components.media_player import MediaPlayerDeviceClass as MediaPlayerDeviceClass, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState, MediaType as MediaType
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, ENTITY_MATCH_ALL as ENTITY_MATCH_ALL, ENTITY_MATCH_NONE as ENTITY_MATCH_NONE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.trigger import PluggableAction as PluggableAction
from typing import Any, Concatenate

_LOGGER: Incomplete
SUPPORT_WEBOSTV: Incomplete
SUPPORT_WEBOSTV_VOLUME: Incomplete
MIN_TIME_BETWEEN_SCANS: Incomplete
MIN_TIME_BETWEEN_FORCED_SCANS: Incomplete
SCAN_INTERVAL: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def cmd[_T: LgWebOSMediaPlayerEntity, **_P](func: Callable[Concatenate[_T, _P], Awaitable[None]]) -> Callable[Concatenate[_T, _P], Coroutine[Any, Any, None]]: ...

class LgWebOSMediaPlayerEntity(RestoreEntity, MediaPlayerEntity):
    _attr_device_class: Incomplete
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _entry: Incomplete
    _client: Incomplete
    _attr_assumed_state: bool
    _device_name: Incomplete
    _attr_unique_id: Incomplete
    _sources: Incomplete
    _paused: bool
    _turn_on: Incomplete
    _current_source: Incomplete
    _source_list: dict
    _supported_features: Incomplete
    def __init__(self, entry: ConfigEntry, client: WebOsClient) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    async def async_signal_handler(self, data: dict[str, Any]) -> None: ...
    async def async_handle_state_update(self, _client: WebOsClient) -> None: ...
    _attr_state: Incomplete
    _attr_is_volume_muted: Incomplete
    _attr_volume_level: Incomplete
    _attr_source: Incomplete
    _attr_source_list: Incomplete
    _attr_media_content_type: Incomplete
    _attr_media_title: Incomplete
    _attr_media_image_url: Incomplete
    _attr_device_info: Incomplete
    _attr_extra_state_attributes: Incomplete
    def _update_states(self) -> None: ...
    def _update_sources(self) -> None: ...
    async def async_update(self) -> None: ...
    @property
    def supported_features(self) -> MediaPlayerEntityFeature: ...
    @cmd
    async def async_turn_off(self) -> None: ...
    async def async_turn_on(self) -> None: ...
    @cmd
    async def async_volume_up(self) -> None: ...
    @cmd
    async def async_volume_down(self) -> None: ...
    @cmd
    async def async_set_volume_level(self, volume: float) -> None: ...
    @cmd
    async def async_mute_volume(self, mute: bool) -> None: ...
    @cmd
    async def async_select_sound_output(self, sound_output: str) -> None: ...
    @cmd
    async def async_media_play_pause(self) -> None: ...
    @cmd
    async def async_select_source(self, source: str) -> None: ...
    @cmd
    async def async_play_media(self, media_type: MediaType | str, media_id: str, **kwargs: Any) -> None: ...
    @cmd
    async def async_media_play(self) -> None: ...
    @cmd
    async def async_media_pause(self) -> None: ...
    @cmd
    async def async_media_stop(self) -> None: ...
    @cmd
    async def async_media_next_track(self) -> None: ...
    @cmd
    async def async_media_previous_track(self) -> None: ...
    @cmd
    async def async_button(self, button: str) -> None: ...
    @cmd
    async def async_command(self, command: str, **kwargs: Any) -> None: ...
    async def _async_fetch_image(self, url: str) -> tuple[bytes | None, str | None]: ...
