import abc
from .const import BYTES_PER_CHUNK as BYTES_PER_CHUNK
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pymicro_vad import MicroVad
from pyspeex_noise import AudioProcessor

_LOGGER: Incomplete

@dataclass(frozen=True, slots=True)
class EnhancedAudioChunk:
    audio: bytes
    timestamp_ms: int
    speech_probability: float | None

class AudioEnhancer(ABC, metaclass=abc.ABCMeta):
    auto_gain: Incomplete
    noise_suppression: Incomplete
    is_vad_enabled: Incomplete
    def __init__(self, auto_gain: int, noise_suppression: int, is_vad_enabled: bool) -> None: ...
    @abstractmethod
    def enhance_chunk(self, audio: bytes, timestamp_ms: int) -> EnhancedAudioChunk: ...

class MicroVadSpeexEnhancer(AudioEnhancer):
    audio_processor: AudioProcessor | None
    noise_suppression: Incomplete
    auto_gain: Incomplete
    vad: MicroVad | None
    def __init__(self, auto_gain: int, noise_suppression: int, is_vad_enabled: bool) -> None: ...
    def enhance_chunk(self, audio: bytes, timestamp_ms: int) -> EnhancedAudioChunk: ...
