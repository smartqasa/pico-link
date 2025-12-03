from enum import StrEnum

DOMAIN: str
REDACTED: str

class DiagnosticsType(StrEnum):
    CONFIG_ENTRY = 'config_entry'

class DiagnosticsSubType(StrEnum):
    DEVICE = 'device'
