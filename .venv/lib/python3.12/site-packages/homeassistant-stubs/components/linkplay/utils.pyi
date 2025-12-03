from .const import DATA_SESSION as DATA_SESSION, DOMAIN as DOMAIN
from aiohttp import ClientSession as ClientSession
from homeassistant.const import EVENT_HOMEASSISTANT_CLOSE as EVENT_HOMEASSISTANT_CLOSE
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from typing import Final

MANUFACTURER_ARTSOUND: Final[str]
MANUFACTURER_ARYLIC: Final[str]
MANUFACTURER_IEAST: Final[str]
MANUFACTURER_WIIM: Final[str]
MANUFACTURER_GGMM: Final[str]
MANUFACTURER_MEDION: Final[str]
MANUFACTURER_GENERIC: Final[str]
MODELS_ARTSOUND_SMART_ZONE4: Final[str]
MODELS_ARTSOUND_SMART_HYDE: Final[str]
MODELS_ARYLIC_S50: Final[str]
MODELS_ARYLIC_S50_PRO: Final[str]
MODELS_ARYLIC_A30: Final[str]
MODELS_ARYLIC_A50: Final[str]
MODELS_ARYLIC_A50S: Final[str]
MODELS_ARYLIC_UP2STREAM_AMP: Final[str]
MODELS_ARYLIC_UP2STREAM_AMP_V3: Final[str]
MODELS_ARYLIC_UP2STREAM_AMP_V4: Final[str]
MODELS_ARYLIC_UP2STREAM_PRO: Final[str]
MODELS_ARYLIC_UP2STREAM_PRO_V3: Final[str]
MODELS_ARYLIC_UP2STREAM_PLATE_AMP: Final[str]
MODELS_IEAST_AUDIOCAST_M5: Final[str]
MODELS_WIIM_AMP: Final[str]
MODELS_WIIM_MINI: Final[str]
MODELS_GGMM_GGMM_E2: Final[str]
MODELS_MEDION_MD_43970: Final[str]
MODELS_GENERIC: Final[str]
PROJECTID_LOOKUP: Final[dict[str, tuple[str, str]]]

def get_info_from_project(project: str) -> tuple[str, str]: ...
async def async_get_client_session(hass: HomeAssistant) -> ClientSession: ...
