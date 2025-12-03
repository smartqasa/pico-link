from . import AnthemavConfigEntry as AnthemavConfigEntry
from .const import ANTHEMAV_UPDATE_SIGNAL as ANTHEMAV_UPDATE_SIGNAL, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from _typeshed import Incomplete
from anthemav.protocol import AVR as AVR
from homeassistant.components.media_player import MediaPlayerDeviceClass as MediaPlayerDeviceClass, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState
from homeassistant.const import CONF_MAC as CONF_MAC, CONF_MODEL as CONF_MODEL
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: AnthemavConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AnthemAVR(MediaPlayerEntity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_should_poll: bool
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    avr: Incomplete
    _entry_id: Incomplete
    _zone_number: Incomplete
    _zone: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, avr: AVR, name: str, mac_address: str, model: str, zone_number: int, entry_id: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def update_states(self) -> None: ...
    _attr_state: Incomplete
    _attr_is_volume_muted: Incomplete
    _attr_volume_level: Incomplete
    _attr_media_title: Incomplete
    _attr_app_name: Incomplete
    _attr_source: Incomplete
    _attr_source_list: Incomplete
    def set_states(self) -> None: ...
    async def async_select_source(self, source: str) -> None: ...
    async def async_turn_off(self) -> None: ...
    async def async_turn_on(self) -> None: ...
    async def async_set_volume_level(self, volume: float) -> None: ...
    async def async_mute_volume(self, mute: bool) -> None: ...
