from . import SpeechToTextEntity as SpeechToTextEntity
from .legacy import Provider as Provider
from enum import Enum
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.util.hass_dict import HassKey as HassKey

DOMAIN: str
DATA_COMPONENT: HassKey[EntityComponent[SpeechToTextEntity]]
DATA_PROVIDERS: HassKey[dict[str, Provider]]

class AudioCodecs(str, Enum):
    PCM = 'pcm'
    OPUS = 'opus'

class AudioFormats(str, Enum):
    WAV = 'wav'
    OGG = 'ogg'

class AudioBitRates(int, Enum):
    BITRATE_8 = 8
    BITRATE_16 = 16
    BITRATE_24 = 24
    BITRATE_32 = 32

class AudioSampleRates(int, Enum):
    SAMPLERATE_8000 = 8000
    SAMPLERATE_11000 = 11000
    SAMPLERATE_16000 = 16000
    SAMPLERATE_18900 = 18900
    SAMPLERATE_22000 = 22000
    SAMPLERATE_32000 = 32000
    SAMPLERATE_37800 = 37800
    SAMPLERATE_44100 = 44100
    SAMPLERATE_48000 = 48000

class AudioChannels(int, Enum):
    CHANNEL_MONO = 1
    CHANNEL_STEREO = 2

class SpeechResultState(str, Enum):
    SUCCESS = 'success'
    ERROR = 'error'
