from dataclasses import dataclass
from google_nest_sdm.device_manager import DeviceManager as DeviceManager
from google_nest_sdm.google_nest_subscriber import GoogleNestSubscriber as GoogleNestSubscriber
from homeassistant.config_entries import ConfigEntry as ConfigEntry

@dataclass
class NestData:
    subscriber: GoogleNestSubscriber
    device_manager: DeviceManager
type NestConfigEntry = ConfigEntry[NestData]
