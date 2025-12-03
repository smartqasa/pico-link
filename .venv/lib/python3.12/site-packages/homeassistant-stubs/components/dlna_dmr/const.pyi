from _typeshed import Incomplete
from async_upnp_client.profiles.dlna import PlayMode as _PlayMode
from collections.abc import Mapping
from homeassistant.components.media_player import MediaType as MediaType, RepeatMode as RepeatMode
from typing import Final

LOGGER: Incomplete
DOMAIN: Final[str]
CONF_LISTEN_PORT: Final[str]
CONF_CALLBACK_URL_OVERRIDE: Final[str]
CONF_POLL_AVAILABILITY: Final[str]
CONF_BROWSE_UNFILTERED: Final[str]
DEFAULT_NAME: Final[str]
CONNECT_TIMEOUT: Final[int]
PROTOCOL_HTTP: Final[str]
PROTOCOL_RTSP: Final[str]
PROTOCOL_ANY: Final[str]
STREAMABLE_PROTOCOLS: Final[Incomplete]
MEDIA_TYPE_MAP: Mapping[str, MediaType]
MEDIA_UPNP_CLASS_MAP: Mapping[MediaType | str, str]
MEDIA_METADATA_DIDL: Mapping[str, str]
REPEAT_PLAY_MODES: Mapping[tuple[bool, RepeatMode], list[_PlayMode]]
SHUFFLE_PLAY_MODES: Mapping[tuple[bool, str], list[_PlayMode]]
