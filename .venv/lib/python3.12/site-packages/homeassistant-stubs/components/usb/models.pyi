from dataclasses import dataclass

@dataclass
class USBDevice:
    device: str
    vid: str
    pid: str
    serial_number: str | None
    manufacturer: str | None
    description: str | None
