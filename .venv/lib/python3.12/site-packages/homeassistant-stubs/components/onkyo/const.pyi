from _typeshed import Incomplete
from enum import Enum
from typing import ClassVar, Literal, Self

DOMAIN: str
DEVICE_INTERVIEW_TIMEOUT: int
DEVICE_DISCOVERY_TIMEOUT: int
CONF_SOURCES: str
CONF_RECEIVER_MAX_VOLUME: str
type VolumeResolution = Literal[50, 80, 100, 200]
OPTION_VOLUME_RESOLUTION: str
OPTION_VOLUME_RESOLUTION_DEFAULT: VolumeResolution
VOLUME_RESOLUTION_ALLOWED: tuple[VolumeResolution, ...]
OPTION_MAX_VOLUME: str
OPTION_MAX_VOLUME_DEFAULT: float
OPTION_INPUT_SOURCES: str
_INPUT_SOURCE_MEANINGS: Incomplete

class InputSource(Enum):
    DVR = '00'
    CBL = '01'
    GAME = '02'
    AUX = '03'
    GAME2 = '04'
    PC = '05'
    VIDEO7 = '06'
    EXTRA1 = '07'
    EXTRA2 = '08'
    EXTRA3 = '09'
    DVD = '10'
    STRM_BOX = '11'
    TV = '12'
    TAPE = '20'
    TAPE2 = '21'
    PHONO = '22'
    CD = '23'
    FM = '24'
    AM = '25'
    TUNER = '26'
    MUSIC_SERVER = '27'
    INTERNET_RADIO = '28'
    USB = '29'
    USB_REAR = '2A'
    NETWORK = '2B'
    AIRPLAY = '2D'
    BLUETOOTH = '2E'
    USB_DAC_IN = '2F'
    MULTI_CH = '30'
    XM = '31'
    SIRIUS = '32'
    DAB = '33'
    UNIVERSAL_PORT = '40'
    LINE = '41'
    LINE2 = '42'
    OPTICAL = '44'
    COAXIAL = '45'
    HDMI_5 = '55'
    HDMI_6 = '56'
    HDMI_7 = '57'
    MAIN_SOURCE = '80'
    __meaning_mapping: ClassVar[dict[str, Self]]
    value_meaning: str
    def __new__(cls, value: str) -> Self: ...
    @classmethod
    def from_meaning(cls, meaning: str) -> Self: ...

ZONES: Incomplete
PYEISCP_COMMANDS: Incomplete
