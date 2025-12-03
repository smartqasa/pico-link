from .const import CONTENT_AUTH_EXPIRY_TIME as CONTENT_AUTH_EXPIRY_TIME, MediaClass as MediaClass, MediaType as MediaType
from _typeshed import Incomplete
from collections.abc import Sequence
from homeassistant.components.http.auth import async_sign_path as async_sign_path
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.network import NoURLAvailableError as NoURLAvailableError, get_supervisor_network_url as get_supervisor_network_url, get_url as get_url, is_hass_url as is_hass_url
from typing import Any

PATHS_WITHOUT_AUTH: Incomplete

@callback
def async_process_play_media_url(hass: HomeAssistant, media_content_id: str, *, allow_relative_url: bool = False, for_supervisor_network: bool = False) -> str: ...

class BrowseMedia:
    media_class: Incomplete
    media_content_id: Incomplete
    media_content_type: Incomplete
    title: Incomplete
    can_play: Incomplete
    can_expand: Incomplete
    children: Incomplete
    children_media_class: Incomplete
    thumbnail: Incomplete
    not_shown: Incomplete
    def __init__(self, *, media_class: MediaClass | str, media_content_id: str, media_content_type: MediaType | str, title: str, can_play: bool, can_expand: bool, children: Sequence[BrowseMedia] | None = None, children_media_class: MediaClass | str | None = None, thumbnail: str | None = None, not_shown: int = 0) -> None: ...
    def as_dict(self, *, parent: bool = True) -> dict[str, Any]: ...
    def calculate_children_class(self) -> None: ...
    def __repr__(self) -> str: ...
