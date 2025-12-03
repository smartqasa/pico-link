from enum import StrEnum

DOMAIN: str

class OmadaDeviceStatus(StrEnum):
    DISCONNECTED = 'disconnected'
    CONNECTED = 'connected'
    PENDING = 'pending'
    HEARTBEAT_MISSED = 'heartbeat_missed'
    ISOLATED = 'isolated'
    ADOPT_FAILED = 'adopt_failed'
    MANAGED_EXTERNALLY = 'managed_externally'
