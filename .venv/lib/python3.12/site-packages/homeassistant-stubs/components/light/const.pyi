from . import LightEntity as LightEntity, Profiles as Profiles
from _typeshed import Incomplete
from enum import IntFlag, StrEnum
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.util.hass_dict import HassKey as HassKey

DOMAIN: str
DATA_COMPONENT: HassKey[EntityComponent[LightEntity]]
SCAN_INTERVAL: Incomplete
DATA_PROFILES: HassKey[Profiles]

class LightEntityFeature(IntFlag):
    EFFECT = 4
    FLASH = 8
    TRANSITION = 32

class ColorMode(StrEnum):
    UNKNOWN = 'unknown'
    ONOFF = 'onoff'
    BRIGHTNESS = 'brightness'
    COLOR_TEMP = 'color_temp'
    HS = 'hs'
    XY = 'xy'
    RGB = 'rgb'
    RGBW = 'rgbw'
    RGBWW = 'rgbww'
    WHITE = 'white'

VALID_COLOR_MODES: Incomplete
COLOR_MODES_BRIGHTNESS: Incomplete
COLOR_MODES_COLOR: Incomplete
DEFAULT_MIN_KELVIN: int
DEFAULT_MAX_KELVIN: int
