from . import HomeKit as HomeKit
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry

type HomeKitConfigEntry = ConfigEntry[HomeKitEntryData]
@dataclass
class HomeKitEntryData:
    homekit: HomeKit
    pairing_qr: bytes | None = ...
    pairing_qr_secret: str | None = ...
