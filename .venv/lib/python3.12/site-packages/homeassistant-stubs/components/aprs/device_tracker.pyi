import threading
from _typeshed import Incomplete
from homeassistant.components.device_tracker import SeeCallback as SeeCallback
from homeassistant.const import ATTR_GPS_ACCURACY as ATTR_GPS_ACCURACY, ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_TIMEOUT as CONF_TIMEOUT, CONF_USERNAME as CONF_USERNAME, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util import slugify as slugify
from typing import Any

DOMAIN: str
_LOGGER: Incomplete
ATTR_ALTITUDE: str
ATTR_COURSE: str
ATTR_COMMENT: str
ATTR_FROM: str
ATTR_FORMAT: str
ATTR_OBJECT_NAME: str
ATTR_POS_AMBIGUITY: str
ATTR_SPEED: str
CONF_CALLSIGNS: str
DEFAULT_HOST: str
DEFAULT_PASSWORD: str
DEFAULT_TIMEOUT: float
FILTER_PORT: int
MSG_FORMATS: Incomplete
PLATFORM_SCHEMA: Incomplete

def make_filter(callsigns: list) -> str: ...
def gps_accuracy(gps: tuple[float, float], posambiguity: int) -> int: ...
def setup_scanner(hass: HomeAssistant, config: ConfigType, see: SeeCallback, discovery_info: DiscoveryInfoType | None = None) -> bool: ...

class AprsListenerThread(threading.Thread):
    callsign: Incomplete
    host: Incomplete
    start_event: Incomplete
    see: Incomplete
    server_filter: Incomplete
    start_message: str
    start_success: bool
    ais: Incomplete
    def __init__(self, callsign: str, password: str, host: str, server_filter: str, see: SeeCallback) -> None: ...
    def start_complete(self, success: bool, message: str) -> None: ...
    def run(self) -> None: ...
    def stop(self) -> None: ...
    def rx_msg(self, msg: dict[str, Any]) -> None: ...
