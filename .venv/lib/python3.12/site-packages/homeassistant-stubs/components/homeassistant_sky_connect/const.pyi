import dataclasses
import enum
from typing import Self

DOMAIN: str
DOCS_WEB_FLASHER_URL: str

@dataclasses.dataclass(frozen=True)
class VariantInfo:
    usb_product_name: str
    short_name: str
    full_name: str

class HardwareVariant(VariantInfo, enum.Enum):
    SKYCONNECT = ('SkyConnect v1.0', 'SkyConnect', 'Home Assistant SkyConnect')
    CONNECT_ZBT1 = ('Home Assistant Connect ZBT-1', 'Connect ZBT-1', 'Home Assistant Connect ZBT-1')
    @classmethod
    def from_usb_product_name(cls, usb_product_name: str) -> Self: ...
