from .coordinator import SFRDataUpdateCoordinator as SFRDataUpdateCoordinator
from dataclasses import dataclass
from sfrbox_api.bridge import SFRBox as SFRBox
from sfrbox_api.models import DslInfo as DslInfo, FtthInfo as FtthInfo, SystemInfo as SystemInfo, WanInfo as WanInfo

@dataclass
class DomainData:
    box: SFRBox
    dsl: SFRDataUpdateCoordinator[DslInfo]
    ftth: SFRDataUpdateCoordinator[FtthInfo]
    system: SFRDataUpdateCoordinator[SystemInfo]
    wan: SFRDataUpdateCoordinator[WanInfo]
