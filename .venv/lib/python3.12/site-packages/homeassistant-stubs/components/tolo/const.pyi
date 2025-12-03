from enum import Enum

DOMAIN: str
DEFAULT_NAME: str
DEFAULT_RETRY_TIMEOUT: int
DEFAULT_RETRY_COUNT: int

class AromaTherapySlot(Enum):
    A = ...
    B = ...

class LampMode(Enum):
    MANUAL = ...
    AUTOMATIC = ...
