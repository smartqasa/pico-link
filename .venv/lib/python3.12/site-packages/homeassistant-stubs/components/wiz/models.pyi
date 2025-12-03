from dataclasses import dataclass
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from pywizlight import wizlight as wizlight

@dataclass
class WizData:
    coordinator: DataUpdateCoordinator[float | None]
    bulb: wizlight
    scenes: list
