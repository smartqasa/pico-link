from dataclasses import dataclass
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo

@dataclass
class OWDeviceDescription:
    device_info: DeviceInfo
    family: str
    id: str
    path: str
    type: str | None
