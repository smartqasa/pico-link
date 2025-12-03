from .const import DATA_PLATFORMS_SETUP as DATA_PLATFORMS_SETUP, DOMAIN as DOMAIN, STT_ENTITY_UNIQUE_ID as STT_ENTITY_UNIQUE_ID, TTS_ENTITY_UNIQUE_ID as TTS_ENTITY_UNIQUE_ID
from homeassistant.components.assist_pipeline import async_create_default_pipeline as async_create_default_pipeline, async_get_pipelines as async_get_pipelines, async_setup_pipeline_store as async_setup_pipeline_store, async_update_pipeline as async_update_pipeline
from homeassistant.components.conversation import HOME_ASSISTANT_AGENT as HOME_ASSISTANT_AGENT
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

async def async_create_cloud_pipeline(hass: HomeAssistant) -> str | None: ...
async def async_migrate_cloud_pipeline_engine(hass: HomeAssistant, platform: Platform, engine_id: str) -> None: ...
