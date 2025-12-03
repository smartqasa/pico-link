from .const import DOMAIN as DOMAIN, EVENT_RECORDING as EVENT_RECORDING, OPTION_PREFERRED as OPTION_PREFERRED, SAMPLES_PER_CHUNK as SAMPLES_PER_CHUNK, SAMPLE_CHANNELS as SAMPLE_CHANNELS, SAMPLE_RATE as SAMPLE_RATE, SAMPLE_WIDTH as SAMPLE_WIDTH
from .error import PipelineNotFound as PipelineNotFound
from .pipeline import AudioSettings as AudioSettings, Pipeline as Pipeline, PipelineEvent as PipelineEvent, PipelineEventCallback, PipelineEventType as PipelineEventType, PipelineStage, WakeWordSettings as WakeWordSettings, async_create_default_pipeline as async_create_default_pipeline, async_get_pipelines as async_get_pipelines, async_migrate_engine as async_migrate_engine, async_update_pipeline as async_update_pipeline
from collections.abc import AsyncIterable
from homeassistant.components import stt
from homeassistant.core import Context, HomeAssistant
from homeassistant.helpers.typing import ConfigType
from typing import Any

__all__ = ['DOMAIN', 'async_create_default_pipeline', 'async_get_pipelines', 'async_migrate_engine', 'async_setup', 'async_pipeline_from_audio_stream', 'async_update_pipeline', 'AudioSettings', 'Pipeline', 'PipelineEvent', 'PipelineEventType', 'PipelineNotFound', 'WakeWordSettings', 'EVENT_RECORDING', 'OPTION_PREFERRED', 'SAMPLES_PER_CHUNK', 'SAMPLE_RATE', 'SAMPLE_WIDTH', 'SAMPLE_CHANNELS']

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_pipeline_from_audio_stream(hass: HomeAssistant, *, context: Context, event_callback: PipelineEventCallback, stt_metadata: stt.SpeechMetadata, stt_stream: AsyncIterable[bytes], wake_word_phrase: str | None = None, pipeline_id: str | None = None, conversation_id: str | None = None, tts_audio_output: str | dict[str, Any] | None = None, wake_word_settings: WakeWordSettings | None = None, audio_settings: AudioSettings | None = None, device_id: str | None = None, start_stage: PipelineStage = ..., end_stage: PipelineStage = ...) -> None: ...
