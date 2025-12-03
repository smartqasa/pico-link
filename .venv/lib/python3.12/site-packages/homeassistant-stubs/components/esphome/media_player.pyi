from .entity import EsphomeEntity as EsphomeEntity, convert_api_error_ha_error as convert_api_error_ha_error, esphome_float_state_property as esphome_float_state_property, esphome_state_property as esphome_state_property, platform_async_setup_entry as platform_async_setup_entry
from .enum_mapper import EsphomeEnumMapper as EsphomeEnumMapper
from .ffmpeg_proxy import async_create_proxy_url as async_create_proxy_url
from _typeshed import Incomplete
from aioesphomeapi import EntityInfo as EntityInfo, MediaPlayerEntityState, MediaPlayerInfo, MediaPlayerState as EspMediaPlayerState, MediaPlayerSupportedFormat as MediaPlayerSupportedFormat
from homeassistant.components import media_source as media_source
from homeassistant.components.media_player import ATTR_MEDIA_ANNOUNCE as ATTR_MEDIA_ANNOUNCE, ATTR_MEDIA_EXTRA as ATTR_MEDIA_EXTRA, BrowseMedia as BrowseMedia, MediaPlayerDeviceClass as MediaPlayerDeviceClass, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState, MediaType as MediaType, async_process_play_media_url as async_process_play_media_url
from homeassistant.core import callback as callback
from typing import Any

_LOGGER: Incomplete
_STATES: EsphomeEnumMapper[EspMediaPlayerState, MediaPlayerState]
ATTR_BYPASS_PROXY: str

class EsphomeMediaPlayer(EsphomeEntity[MediaPlayerInfo, MediaPlayerEntityState], MediaPlayerEntity):
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    @callback
    def _on_static_info_update(self, static_info: EntityInfo) -> None: ...
    @property
    @esphome_state_property
    def state(self) -> MediaPlayerState | None: ...
    @property
    @esphome_state_property
    def is_volume_muted(self) -> bool: ...
    @property
    @esphome_float_state_property
    def volume_level(self) -> float | None: ...
    @convert_api_error_ha_error
    async def async_play_media(self, media_type: MediaType | str, media_id: str, **kwargs: Any) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    def _get_proxy_url(self, supported_formats: list[MediaPlayerSupportedFormat], url: str, announcement: bool) -> str | None: ...
    async def async_browse_media(self, media_content_type: MediaType | str | None = None, media_content_id: str | None = None) -> BrowseMedia: ...
    @convert_api_error_ha_error
    async def async_set_volume_level(self, volume: float) -> None: ...
    @convert_api_error_ha_error
    async def async_media_pause(self) -> None: ...
    @convert_api_error_ha_error
    async def async_media_play(self) -> None: ...
    @convert_api_error_ha_error
    async def async_media_stop(self) -> None: ...
    @convert_api_error_ha_error
    async def async_mute_volume(self, mute: bool) -> None: ...

def _is_url(url: str) -> bool: ...

async_setup_entry: Incomplete
