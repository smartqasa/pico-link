from . import coordinator as coordinator
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.config_entry_oauth2_flow import OAuth2Session as OAuth2Session, async_get_config_entry_implementation as async_get_config_entry_implementation
from iottycloud.device import Device as Device

_LOGGER: Incomplete
PLATFORMS: list[Platform]
type IottyConfigEntry = ConfigEntry[IottyConfigEntryData]

@dataclass
class IottyConfigEntryData:
    known_devices: set[Device]
    coordinator: coordinator.IottyDataUpdateCoordinator

async def async_setup_entry(hass: HomeAssistant, entry: IottyConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
