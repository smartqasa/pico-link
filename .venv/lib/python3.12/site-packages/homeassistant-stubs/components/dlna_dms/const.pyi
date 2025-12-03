from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components.media_player import MediaClass as MediaClass
from typing import Final

LOGGER: Incomplete
DOMAIN: Final[str]
DEFAULT_NAME: Final[str]
CONF_SOURCE_ID: Final[str]
CONFIG_VERSION: Final[int]
SOURCE_SEP: Final[str]
ROOT_OBJECT_ID: Final[str]
PATH_SEP: Final[str]
PATH_SEARCH_FLAG: Final[str]
PATH_OBJECT_ID_FLAG: Final[str]
DLNA_BROWSE_FILTER: Final[Incomplete]
DLNA_RESOLVE_FILTER: Final[str]
DLNA_PATH_FILTER: Final[Incomplete]
DLNA_SORT_CRITERIA: Final[Incomplete]
PROTOCOL_HTTP: Final[str]
PROTOCOL_RTSP: Final[str]
PROTOCOL_ANY: Final[str]
STREAMABLE_PROTOCOLS: Final[Incomplete]
MEDIA_CLASS_MAP: Mapping[str, MediaClass]
