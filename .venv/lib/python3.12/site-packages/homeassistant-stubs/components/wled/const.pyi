from _typeshed import Incomplete
from homeassistant.components.light import ColorMode as ColorMode
from wled import LightCapability

DOMAIN: str
LOGGER: Incomplete
SCAN_INTERVAL: Incomplete
RELEASES_SCAN_INTERVAL: Incomplete
CONF_KEEP_MAIN_LIGHT: str
DEFAULT_KEEP_MAIN_LIGHT: bool
ATTR_CCT: str
ATTR_COLOR_PRIMARY: str
ATTR_DURATION: str
ATTR_FADE: str
ATTR_INTENSITY: str
ATTR_ON: str
ATTR_SEGMENT_ID: str
ATTR_SOFTWARE_VERSION: str
ATTR_SPEED: str
ATTR_TARGET_BRIGHTNESS: str
ATTR_UDP_PORT: str
COLOR_TEMP_K_MIN: int
COLOR_TEMP_K_MAX: int
LIGHT_CAPABILITIES_COLOR_MODE_MAPPING: dict[LightCapability, list[ColorMode]]
