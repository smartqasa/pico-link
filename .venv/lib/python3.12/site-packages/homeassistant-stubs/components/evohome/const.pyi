from _typeshed import Incomplete
from enum import StrEnum
from typing import Final

DOMAIN: Final[str]
STORAGE_VER: Final[int]
STORAGE_KEY: Final[Incomplete]
EVO_RESET: Final[str]
EVO_AUTO: Final[str]
EVO_AUTOECO: Final[str]
EVO_AWAY: Final[str]
EVO_DAYOFF: Final[str]
EVO_CUSTOM: Final[str]
EVO_HEATOFF: Final[str]
EVO_FOLLOW: Final[str]
EVO_TEMPOVER: Final[str]
EVO_PERMOVER: Final[str]
GWS: Final[str]
TCS: Final[str]
UTC_OFFSET: Final[str]
CONF_LOCATION_IDX: Final[str]
ACCESS_TOKEN: Final[str]
ACCESS_TOKEN_EXPIRES: Final[str]
REFRESH_TOKEN: Final[str]
USER_DATA: Final[str]
SCAN_INTERVAL_DEFAULT: Final[Incomplete]
SCAN_INTERVAL_MINIMUM: Final[Incomplete]
ATTR_SYSTEM_MODE: Final[str]
ATTR_DURATION_DAYS: Final[str]
ATTR_DURATION_HOURS: Final[str]
ATTR_ZONE_TEMP: Final[str]
ATTR_DURATION_UNTIL: Final[str]

class EvoService(StrEnum):
    REFRESH_SYSTEM = 'refresh_system'
    SET_SYSTEM_MODE = 'set_system_mode'
    RESET_SYSTEM = 'reset_system'
    SET_ZONE_OVERRIDE = 'set_zone_override'
    RESET_ZONE_OVERRIDE = 'clear_zone_override'
