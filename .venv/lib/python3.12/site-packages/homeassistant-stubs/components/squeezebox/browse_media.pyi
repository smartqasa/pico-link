from _typeshed import Incomplete
from homeassistant.components import media_source as media_source
from homeassistant.components.media_player import BrowseError as BrowseError, BrowseMedia as BrowseMedia, MediaClass as MediaClass, MediaPlayerEntity as MediaPlayerEntity, MediaType as MediaType
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.network import is_internal_request as is_internal_request
from pysqueezebox import Player as Player

LIBRARY: Incomplete
MEDIA_TYPE_TO_SQUEEZEBOX: Incomplete
SQUEEZEBOX_ID_BY_TYPE: Incomplete
CONTENT_TYPE_MEDIA_CLASS: dict[str | MediaType, dict[str, MediaClass | None]]
CONTENT_TYPE_TO_CHILD_TYPE: Incomplete
BROWSE_LIMIT: int

async def build_item_response(entity: MediaPlayerEntity, player: Player, payload: dict[str, str | None]) -> BrowseMedia: ...
async def library_payload(hass: HomeAssistant, player: Player) -> BrowseMedia: ...
def media_source_content_filter(item: BrowseMedia) -> bool: ...
async def generate_playlist(player: Player, payload: dict[str, str]) -> list | None: ...
