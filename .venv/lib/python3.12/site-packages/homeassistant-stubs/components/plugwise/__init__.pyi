from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, PLATFORMS as PLATFORMS
from .coordinator import PlugwiseDataUpdateCoordinator as PlugwiseDataUpdateCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import entity_registry as er
from typing import Any

type PlugwiseConfigEntry = ConfigEntry[PlugwiseDataUpdateCoordinator]
async def async_setup_entry(hass: HomeAssistant, entry: PlugwiseConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: PlugwiseConfigEntry) -> bool: ...
@callback
def async_migrate_entity_entry(entry: er.RegistryEntry) -> dict[str, Any] | None: ...
def migrate_sensor_entities(hass: HomeAssistant, coordinator: PlugwiseDataUpdateCoordinator) -> None: ...
