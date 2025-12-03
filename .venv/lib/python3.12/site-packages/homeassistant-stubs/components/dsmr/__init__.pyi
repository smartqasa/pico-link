from .const import CONF_DSMR_VERSION as CONF_DSMR_VERSION, PLATFORMS as PLATFORMS
from asyncio import Task
from dataclasses import dataclass
from dsmr_parser.objects import Telegram as Telegram
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import entity_registry as er
from typing import Any

@dataclass
class DsmrState:
    task: Task | None = ...
    telegram: Telegram | None = ...
type DsmrConfigEntry = ConfigEntry[DsmrState]

async def async_setup_entry(hass: HomeAssistant, entry: DsmrConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: DsmrConfigEntry) -> bool: ...
async def async_update_options(hass: HomeAssistant, entry: DsmrConfigEntry) -> None: ...
@callback
def async_migrate_entity_entry(config_entry: ConfigEntry, entity_entry: er.RegistryEntry) -> dict[str, Any] | None: ...
