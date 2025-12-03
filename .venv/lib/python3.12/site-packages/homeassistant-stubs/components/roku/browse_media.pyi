from .coordinator import RokuDataUpdateCoordinator as RokuDataUpdateCoordinator
from .helpers import format_channel_name as format_channel_name
from _typeshed import Incomplete
from collections.abc import Callable
from homeassistant.components import media_source as media_source
from homeassistant.components.media_player import BrowseError as BrowseError, BrowseMedia as BrowseMedia, MediaClass as MediaClass, MediaType as MediaType
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.network import is_internal_request as is_internal_request

CONTENT_TYPE_MEDIA_CLASS: Incomplete
CONTAINER_TYPES_SPECIFIC_MEDIA_CLASS: Incomplete
PLAYABLE_MEDIA_TYPES: Incomplete
EXPANDABLE_MEDIA_TYPES: Incomplete
type GetBrowseImageUrlType = Callable[[str, str, str | None], str | None]

def get_thumbnail_url_full(coordinator: RokuDataUpdateCoordinator, is_internal: bool, get_browse_image_url: GetBrowseImageUrlType, media_content_type: str, media_content_id: str, media_image_id: str | None = None) -> str | None: ...
async def async_browse_media(hass: HomeAssistant, coordinator: RokuDataUpdateCoordinator, get_browse_image_url: GetBrowseImageUrlType, media_content_id: str | None, media_content_type: str | None) -> BrowseMedia: ...
async def root_payload(hass: HomeAssistant, coordinator: RokuDataUpdateCoordinator, get_browse_image_url: GetBrowseImageUrlType) -> BrowseMedia: ...
def build_item_response(coordinator: RokuDataUpdateCoordinator, payload: dict, get_browse_image_url: GetBrowseImageUrlType) -> BrowseMedia | None: ...
def item_payload(item: dict, coordinator: RokuDataUpdateCoordinator, get_browse_image_url: GetBrowseImageUrlType) -> BrowseMedia: ...
