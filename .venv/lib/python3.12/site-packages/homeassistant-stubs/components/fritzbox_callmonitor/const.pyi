from _typeshed import Incomplete
from enum import StrEnum
from homeassistant.const import Platform as Platform
from typing import Final

class FritzState(StrEnum):
    RING = 'RING'
    CALL = 'CALL'
    CONNECT = 'CONNECT'
    DISCONNECT = 'DISCONNECT'

ATTR_PREFIXES: str
FRITZ_ATTR_NAME: str
FRITZ_ATTR_SERIAL_NUMBER: str
UNKNOWN_NAME: str
SERIAL_NUMBER: str
REGEX_NUMBER: str
CONF_PHONEBOOK: str
CONF_PHONEBOOK_NAME: str
CONF_PREFIXES: str
DEFAULT_HOST: str
DEFAULT_PORT: int
DEFAULT_USERNAME: str
DEFAULT_PHONEBOOK: int
DEFAULT_NAME: str
DOMAIN: Final[str]
MANUFACTURER: Final[str]
PLATFORMS: Incomplete
