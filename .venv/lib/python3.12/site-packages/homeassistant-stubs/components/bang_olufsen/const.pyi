from _typeshed import Incomplete
from enum import StrEnum
from homeassistant.components.media_player import MediaPlayerState as MediaPlayerState, MediaType as MediaType, RepeatMode as RepeatMode
from mozart_api.models import Source, SourceArray
from typing import Final

class BangOlufsenSource:
    LINE_IN: Final[Source]
    SPDIF: Final[Source]
    URI_STREAMER: Final[Source]

BANG_OLUFSEN_STATES: dict[str, MediaPlayerState]
BANG_OLUFSEN_REPEAT_FROM_HA: dict[RepeatMode, str]
BANG_OLUFSEN_REPEAT_TO_HA: dict[str, RepeatMode]

class BangOlufsenMediaType(StrEnum):
    FAVOURITE = 'favourite'
    DEEZER = 'deezer'
    RADIO = 'radio'
    TIDAL = 'tidal'
    TTS = 'provider'
    OVERLAY_TTS = 'overlay_tts'

class BangOlufsenModel(StrEnum):
    BEOCONNECT_CORE = 'Beoconnect Core'
    BEOLAB_8 = 'BeoLab 8'
    BEOLAB_28 = 'BeoLab 28'
    BEOSOUND_2 = 'Beosound 2 3rd Gen'
    BEOSOUND_A5 = 'Beosound A5'
    BEOSOUND_A9 = 'Beosound A9 5th Gen'
    BEOSOUND_BALANCE = 'Beosound Balance'
    BEOSOUND_EMERGE = 'Beosound Emerge'
    BEOSOUND_LEVEL = 'Beosound Level'
    BEOSOUND_THEATRE = 'Beosound Theatre'

class WebsocketNotification(StrEnum):
    ACTIVE_LISTENING_MODE = 'active_listening_mode'
    PLAYBACK_ERROR = 'playback_error'
    PLAYBACK_METADATA = 'playback_metadata'
    PLAYBACK_PROGRESS = 'playback_progress'
    PLAYBACK_SOURCE = 'playback_source'
    PLAYBACK_STATE = 'playback_state'
    SOFTWARE_UPDATE_STATE = 'software_update_state'
    SOURCE_CHANGE = 'source_change'
    VOLUME = 'volume'
    BEOLINK = 'beolink'
    BEOLINK_PEERS = 'beolinkPeers'
    BEOLINK_LISTENERS = 'beolinkListeners'
    BEOLINK_AVAILABLE_LISTENERS = 'beolinkAvailableListeners'
    CONFIGURATION = 'configuration'
    NOTIFICATION = 'notification'
    REMOTE_MENU_CHANGED = 'remoteMenuChanged'
    ALL = 'all'

DOMAIN: Final[str]
DEFAULT_MODEL: Final[str]
CONF_SERIAL_NUMBER: Final[str]
CONF_BEOLINK_JID: Final[str]
COMPATIBLE_MODELS: list[str]
ATTR_TYPE_NUMBER: Final[str]
ATTR_SERIAL_NUMBER: Final[str]
ATTR_ITEM_NUMBER: Final[str]
ATTR_FRIENDLY_NAME: Final[str]
BANG_OLUFSEN_ON: Final[str]
VALID_MEDIA_TYPES: Final[tuple]
FALLBACK_SOURCES: Final[SourceArray]
BANG_OLUFSEN_WEBSOCKET_EVENT: Final[str]
CONNECTION_STATUS: Final[str]
BEOLINK_JOIN_SOURCES_TO_UPPER: Incomplete
BEOLINK_JOIN_SOURCES: Incomplete
