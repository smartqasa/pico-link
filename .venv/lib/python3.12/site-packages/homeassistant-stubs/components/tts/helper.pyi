from . import TextToSpeechEntity as TextToSpeechEntity
from .const import DATA_COMPONENT as DATA_COMPONENT, DATA_TTS_MANAGER as DATA_TTS_MANAGER
from .legacy import Provider as Provider
from homeassistant.core import HomeAssistant as HomeAssistant

def get_engine_instance(hass: HomeAssistant, engine: str) -> TextToSpeechEntity | Provider | None: ...
