from .coordinator import TPLinkDataUpdateCoordinator as TPLinkDataUpdateCoordinator
from dataclasses import dataclass
from kasa import Credentials as Credentials

@dataclass(slots=True)
class TPLinkData:
    parent_coordinator: TPLinkDataUpdateCoordinator
    children_coordinators: list[TPLinkDataUpdateCoordinator]
    camera_credentials: Credentials | None
    live_view: bool | None
