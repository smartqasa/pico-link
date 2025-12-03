from dataclasses import dataclass
from homeassistant.data_entry_flow import BaseServiceInfo as BaseServiceInfo
from typing import Any

@dataclass(slots=True)
class HassioServiceInfo(BaseServiceInfo):
    config: dict[str, Any]
    name: str
    slug: str
    uuid: str
