from dataclasses import dataclass

@dataclass(frozen=True)
class Voice:
    voice_id: str
    name: str
