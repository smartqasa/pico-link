from dataclasses import dataclass
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from py_dormakaba_dkey import DKEYLock as DKEYLock

@dataclass
class DormakabaDkeyData:
    lock: DKEYLock
    coordinator: DataUpdateCoordinator[None]
