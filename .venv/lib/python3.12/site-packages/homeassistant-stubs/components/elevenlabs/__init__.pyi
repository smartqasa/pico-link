from .const import CONF_MODEL as CONF_MODEL
from dataclasses import dataclass
from elevenlabs import AsyncElevenLabs, Model as Model
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryError as ConfigEntryError, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.httpx_client import get_async_client as get_async_client

PLATFORMS: list[Platform]

async def get_model_by_id(client: AsyncElevenLabs, model_id: str) -> Model | None: ...

@dataclass(kw_only=True, slots=True)
class ElevenLabsData:
    client: AsyncElevenLabs
    model: Model
type ElevenLabsConfigEntry = ConfigEntry[ElevenLabsData]

async def async_setup_entry(hass: HomeAssistant, entry: ElevenLabsConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ElevenLabsConfigEntry) -> bool: ...
async def update_listener(hass: HomeAssistant, config_entry: ElevenLabsConfigEntry) -> None: ...
