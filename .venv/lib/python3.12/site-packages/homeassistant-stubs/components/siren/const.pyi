from enum import IntFlag
from typing import Final

DOMAIN: Final[str]
ATTR_TONE: Final[str]
ATTR_AVAILABLE_TONES: Final[str]
ATTR_DURATION: Final[str]
ATTR_VOLUME_LEVEL: Final[str]

class SirenEntityFeature(IntFlag):
    TURN_ON = 1
    TURN_OFF = 2
    TONES = 4
    VOLUME_SET = 8
    DURATION = 16
