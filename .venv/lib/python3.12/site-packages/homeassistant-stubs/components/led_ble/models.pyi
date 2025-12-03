from dataclasses import dataclass
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from led_ble import LEDBLE as LEDBLE

@dataclass
class LEDBLEData:
    title: str
    device: LEDBLE
    coordinator: DataUpdateCoordinator[None]
