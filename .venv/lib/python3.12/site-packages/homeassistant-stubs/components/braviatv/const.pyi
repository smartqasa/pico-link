from enum import StrEnum
from typing import Final

ATTR_CID: Final[str]
ATTR_MAC: Final[str]
ATTR_MANUFACTURER: Final[str]
ATTR_MODEL: Final[str]
CONF_NICKNAME: Final[str]
CONF_USE_PSK: Final[str]
DOMAIN: Final[str]
LEGACY_CLIENT_ID: Final[str]
NICKNAME_PREFIX: Final[str]

class SourceType(StrEnum):
    APP = 'app'
    CHANNEL = 'channel'
    INPUT = 'input'
