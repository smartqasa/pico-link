from . import MusicAssistantConfigEntry as MusicAssistantConfigEntry
from .const import ATTR_ALBUMS as ATTR_ALBUMS, ATTR_ALBUM_ARTISTS_ONLY as ATTR_ALBUM_ARTISTS_ONLY, ATTR_ALBUM_TYPE as ATTR_ALBUM_TYPE, ATTR_ARTISTS as ATTR_ARTISTS, ATTR_CONFIG_ENTRY_ID as ATTR_CONFIG_ENTRY_ID, ATTR_FAVORITE as ATTR_FAVORITE, ATTR_ITEMS as ATTR_ITEMS, ATTR_LIBRARY_ONLY as ATTR_LIBRARY_ONLY, ATTR_LIMIT as ATTR_LIMIT, ATTR_MEDIA_TYPE as ATTR_MEDIA_TYPE, ATTR_OFFSET as ATTR_OFFSET, ATTR_ORDER_BY as ATTR_ORDER_BY, ATTR_PLAYLISTS as ATTR_PLAYLISTS, ATTR_RADIO as ATTR_RADIO, ATTR_SEARCH as ATTR_SEARCH, ATTR_SEARCH_ALBUM as ATTR_SEARCH_ALBUM, ATTR_SEARCH_ARTIST as ATTR_SEARCH_ARTIST, ATTR_SEARCH_NAME as ATTR_SEARCH_NAME, ATTR_TRACKS as ATTR_TRACKS, DOMAIN as DOMAIN
from .schemas import LIBRARY_RESULTS_SCHEMA as LIBRARY_RESULTS_SCHEMA, SEARCH_RESULT_SCHEMA as SEARCH_RESULT_SCHEMA, media_item_dict_from_mass_item as media_item_dict_from_mass_item
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from music_assistant_client import MusicAssistantClient as MusicAssistantClient

SERVICE_SEARCH: str
SERVICE_GET_LIBRARY: str
DEFAULT_OFFSET: int
DEFAULT_LIMIT: int
DEFAULT_SORT_ORDER: str

@callback
def get_music_assistant_client(hass: HomeAssistant, config_entry_id: str) -> MusicAssistantClient: ...
@callback
def register_actions(hass: HomeAssistant) -> None: ...
async def handle_search(call: ServiceCall) -> ServiceResponse: ...
async def handle_get_library(call: ServiceCall) -> ServiceResponse: ...
