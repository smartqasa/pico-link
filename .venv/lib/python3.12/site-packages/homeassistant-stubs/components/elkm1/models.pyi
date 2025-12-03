from dataclasses import dataclass
from elkm1_lib import Elk as Elk
from typing import Any

@dataclass(slots=True)
class ELKM1Data:
    elk: Elk
    prefix: str
    mac: str | None
    auto_configure: bool
    config: dict[str, Any]
    keypads: dict[str, Any]
