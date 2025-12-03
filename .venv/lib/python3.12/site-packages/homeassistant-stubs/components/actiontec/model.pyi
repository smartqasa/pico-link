from dataclasses import dataclass

@dataclass
class Device:
    ip_address: str
    mac_address: str
    timevalid: int
