from bleak.backends.device import BLEDevice as BLEDevice
from dataclasses import dataclass
from pysnooz.device import SnoozDevice as SnoozDevice

@dataclass
class SnoozConfigurationData:
    ble_device: BLEDevice
    device: SnoozDevice
    title: str
