from enum import IntFlag, StrEnum

MODE_NORMAL: str
MODE_ECO: str
MODE_AWAY: str
MODE_BOOST: str
MODE_COMFORT: str
MODE_HOME: str
MODE_SLEEP: str
MODE_AUTO: str
MODE_BABY: str

class HumidifierAction(StrEnum):
    HUMIDIFYING = 'humidifying'
    DRYING = 'drying'
    IDLE = 'idle'
    OFF = 'off'

ATTR_ACTION: str
ATTR_AVAILABLE_MODES: str
ATTR_CURRENT_HUMIDITY: str
ATTR_HUMIDITY: str
ATTR_MAX_HUMIDITY: str
ATTR_MIN_HUMIDITY: str
DEFAULT_MIN_HUMIDITY: int
DEFAULT_MAX_HUMIDITY: int
DOMAIN: str
SERVICE_SET_MODE: str
SERVICE_SET_HUMIDITY: str

class HumidifierEntityFeature(IntFlag):
    MODES = 1
