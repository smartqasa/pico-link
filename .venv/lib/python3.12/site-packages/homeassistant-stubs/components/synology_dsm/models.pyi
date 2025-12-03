from .common import SynoApi as SynoApi
from .coordinator import SynologyDSMCameraUpdateCoordinator as SynologyDSMCameraUpdateCoordinator, SynologyDSMCentralUpdateCoordinator as SynologyDSMCentralUpdateCoordinator, SynologyDSMSwitchUpdateCoordinator as SynologyDSMSwitchUpdateCoordinator
from dataclasses import dataclass

@dataclass
class SynologyDSMData:
    api: SynoApi
    coordinator_central: SynologyDSMCentralUpdateCoordinator
    coordinator_cameras: SynologyDSMCameraUpdateCoordinator | None
    coordinator_switches: SynologyDSMSwitchUpdateCoordinator | None
