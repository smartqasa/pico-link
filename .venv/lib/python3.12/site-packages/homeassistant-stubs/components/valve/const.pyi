from enum import StrEnum

DOMAIN: str

class ValveState(StrEnum):
    OPENING = 'opening'
    CLOSING = 'closing'
    CLOSED = 'closed'
    OPEN = 'open'
