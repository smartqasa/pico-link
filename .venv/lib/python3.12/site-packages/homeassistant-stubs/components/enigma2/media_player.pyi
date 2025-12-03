from . import Enigma2ConfigEntry as Enigma2ConfigEntry
from .coordinator import Enigma2UpdateCoordinator as Enigma2UpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.media_player import MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState, MediaType as MediaType
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

ATTR_MEDIA_CURRENTLY_RECORDING: str
ATTR_MEDIA_DESCRIPTION: str
ATTR_MEDIA_END_TIME: str
ATTR_MEDIA_START_TIME: str
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: Enigma2ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class Enigma2Device(CoordinatorEntity[Enigma2UpdateCoordinator], MediaPlayerEntity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_media_content_type: Incomplete
    _attr_supported_features: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: Enigma2UpdateCoordinator) -> None: ...
    _attr_available: bool
    async def async_turn_off(self) -> None: ...
    async def async_turn_on(self) -> None: ...
    async def async_set_volume_level(self, volume: float) -> None: ...
    async def async_volume_up(self) -> None: ...
    async def async_volume_down(self) -> None: ...
    async def async_media_stop(self) -> None: ...
    async def async_media_play(self) -> None: ...
    async def async_media_pause(self) -> None: ...
    async def async_media_next_track(self) -> None: ...
    async def async_media_previous_track(self) -> None: ...
    async def async_mute_volume(self, mute: bool) -> None: ...
    async def async_select_source(self, source: str) -> None: ...
    _attr_extra_state_attributes: Incomplete
    _attr_media_title: Incomplete
    _attr_media_series_title: Incomplete
    _attr_media_channel: Incomplete
    _attr_is_volume_muted: Incomplete
    _attr_media_content_id: Incomplete
    _attr_media_image_url: Incomplete
    _attr_source: Incomplete
    _attr_source_list: Incomplete
    _attr_state: Incomplete
    _attr_volume_level: Incomplete
    @callback
    def _handle_coordinator_update(self) -> None: ...
