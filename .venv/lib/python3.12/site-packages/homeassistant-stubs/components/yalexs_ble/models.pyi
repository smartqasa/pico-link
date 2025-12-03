from dataclasses import dataclass
from yalexs_ble import PushLock as PushLock

@dataclass
class YaleXSBLEData:
    title: str
    lock: PushLock
    always_connected: bool
