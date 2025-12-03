from .data import ProtectDeviceType as ProtectDeviceType, UFPConfigEntry as UFPConfigEntry
from .entity import ProtectDeviceEntity as ProtectDeviceEntity
from _typeshed import Incomplete
from homeassistant.components import media_source as media_source
from homeassistant.components.media_player import BrowseMedia as BrowseMedia, MediaPlayerDeviceClass as MediaPlayerDeviceClass, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityDescription as MediaPlayerEntityDescription, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState, MediaType as MediaType, async_process_play_media_url as async_process_play_media_url
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any
from uiprotect.data import Camera, ProtectAdoptableDeviceModel as ProtectAdoptableDeviceModel

_LOGGER: Incomplete
_SPEAKER_DESCRIPTION: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: UFPConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ProtectMediaPlayer(ProtectDeviceEntity, MediaPlayerEntity):
    device: Camera
    entity_description: MediaPlayerEntityDescription
    _attr_supported_features: Incomplete
    _attr_media_content_type: Incomplete
    _state_attrs: Incomplete
    _attr_volume_level: Incomplete
    _attr_state: Incomplete
    _attr_available: Incomplete
    @callback
    def _async_update_device_from_protect(self, device: ProtectDeviceType) -> None: ...
    async def async_set_volume_level(self, volume: float) -> None: ...
    async def async_media_stop(self) -> None: ...
    async def async_play_media(self, media_type: MediaType | str, media_id: str, **kwargs: Any) -> None: ...
    async def async_browse_media(self, media_content_type: MediaType | str | None = None, media_content_id: str | None = None) -> BrowseMedia: ...
