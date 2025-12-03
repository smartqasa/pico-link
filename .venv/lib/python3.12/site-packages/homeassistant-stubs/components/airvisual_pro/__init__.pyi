from .const import LOGGER as LOGGER
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_PASSWORD as CONF_PASSWORD, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pyairvisual.node import NodeSamba

PLATFORMS: Incomplete
UPDATE_INTERVAL: Incomplete
type AirVisualProConfigEntry = ConfigEntry[AirVisualProData]

@dataclass
class AirVisualProData:
    coordinator: DataUpdateCoordinator
    node: NodeSamba

async def async_setup_entry(hass: HomeAssistant, entry: AirVisualProConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AirVisualProConfigEntry) -> bool: ...
