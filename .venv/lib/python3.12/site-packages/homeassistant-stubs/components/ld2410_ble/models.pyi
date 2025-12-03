from .coordinator import LD2410BLECoordinator as LD2410BLECoordinator
from dataclasses import dataclass
from ld2410_ble import LD2410BLE as LD2410BLE

@dataclass
class LD2410BLEData:
    title: str
    device: LD2410BLE
    coordinator: LD2410BLECoordinator
