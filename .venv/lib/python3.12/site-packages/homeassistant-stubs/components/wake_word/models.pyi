from dataclasses import dataclass

@dataclass(frozen=True)
class WakeWord:
    id: str
    name: str
    phrase: str | None = ...

@dataclass
class DetectionResult:
    wake_word_id: str
    wake_word_phrase: str
    timestamp: int | None
    queued_audio: list[tuple[bytes, int]] | None = ...
