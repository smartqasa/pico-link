from . import SpeechManager as SpeechManager, TextToSpeechEntity as TextToSpeechEntity
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.util.hass_dict import HassKey as HassKey

ATTR_CACHE: str
ATTR_LANGUAGE: str
ATTR_MESSAGE: str
ATTR_OPTIONS: str
CONF_CACHE: str
CONF_CACHE_DIR: str
CONF_FIELDS: str
CONF_TIME_MEMORY: str
DEFAULT_CACHE: bool
DEFAULT_CACHE_DIR: str
DEFAULT_TIME_MEMORY: int
DOMAIN: str
DATA_COMPONENT: HassKey[EntityComponent[TextToSpeechEntity]]
DATA_TTS_MANAGER: HassKey[SpeechManager]
type TtsAudioType = tuple[str | None, bytes | None]
