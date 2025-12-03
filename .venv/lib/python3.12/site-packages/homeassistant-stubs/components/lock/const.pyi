from enum import StrEnum

DOMAIN: str

class LockState(StrEnum):
    JAMMED = 'jammed'
    OPENING = 'opening'
    LOCKING = 'locking'
    OPEN = 'open'
    UNLOCKING = 'unlocking'
    LOCKED = 'locked'
    UNLOCKED = 'unlocked'
