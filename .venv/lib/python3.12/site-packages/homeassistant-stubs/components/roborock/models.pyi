from dataclasses import dataclass
from roborock.containers import HomeDataDevice as HomeDataDevice, HomeDataProduct as HomeDataProduct, NetworkInfo as NetworkInfo
from roborock.roborock_typing import DeviceProp as DeviceProp
from typing import Any

@dataclass
class RoborockHassDeviceInfo:
    device: HomeDataDevice
    network_info: NetworkInfo
    product: HomeDataProduct
    props: DeviceProp
    def as_dict(self) -> dict[str, dict[str, Any]]: ...

@dataclass
class RoborockA01HassDeviceInfo:
    device: HomeDataDevice
    product: HomeDataProduct
    def as_dict(self) -> dict[str, dict[str, Any]]: ...

@dataclass
class RoborockMapInfo:
    flag: int
    name: str
    rooms: dict[int, str]
