from .const import ATTR_ACTIVE as ATTR_ACTIVE, ATTR_ALBUM as ATTR_ALBUM, ATTR_ALBUMS as ATTR_ALBUMS, ATTR_ARTISTS as ATTR_ARTISTS, ATTR_BIT_DEPTH as ATTR_BIT_DEPTH, ATTR_CONTENT_TYPE as ATTR_CONTENT_TYPE, ATTR_CURRENT_INDEX as ATTR_CURRENT_INDEX, ATTR_CURRENT_ITEM as ATTR_CURRENT_ITEM, ATTR_DURATION as ATTR_DURATION, ATTR_ELAPSED_TIME as ATTR_ELAPSED_TIME, ATTR_IMAGE as ATTR_IMAGE, ATTR_ITEMS as ATTR_ITEMS, ATTR_ITEM_ID as ATTR_ITEM_ID, ATTR_LIMIT as ATTR_LIMIT, ATTR_MEDIA_ITEM as ATTR_MEDIA_ITEM, ATTR_MEDIA_TYPE as ATTR_MEDIA_TYPE, ATTR_NEXT_ITEM as ATTR_NEXT_ITEM, ATTR_OFFSET as ATTR_OFFSET, ATTR_ORDER_BY as ATTR_ORDER_BY, ATTR_PLAYLISTS as ATTR_PLAYLISTS, ATTR_PROVIDER as ATTR_PROVIDER, ATTR_QUEUE_ID as ATTR_QUEUE_ID, ATTR_QUEUE_ITEM_ID as ATTR_QUEUE_ITEM_ID, ATTR_RADIO as ATTR_RADIO, ATTR_REPEAT_MODE as ATTR_REPEAT_MODE, ATTR_SAMPLE_RATE as ATTR_SAMPLE_RATE, ATTR_SHUFFLE_ENABLED as ATTR_SHUFFLE_ENABLED, ATTR_STREAM_DETAILS as ATTR_STREAM_DETAILS, ATTR_STREAM_TITLE as ATTR_STREAM_TITLE, ATTR_TRACKS as ATTR_TRACKS, ATTR_URI as ATTR_URI, ATTR_VERSION as ATTR_VERSION
from _typeshed import Incomplete
from homeassistant.const import ATTR_NAME as ATTR_NAME
from music_assistant_client import MusicAssistantClient as MusicAssistantClient
from music_assistant_models.media_items import ItemMapping as ItemMapping, MediaItemType as MediaItemType
from music_assistant_models.queue_item import QueueItem as QueueItem
from typing import Any

MEDIA_ITEM_SCHEMA: Incomplete

def media_item_dict_from_mass_item(mass: MusicAssistantClient, item: MediaItemType | ItemMapping | None) -> dict[str, Any] | None: ...

SEARCH_RESULT_SCHEMA: Incomplete
LIBRARY_RESULTS_SCHEMA: Incomplete
AUDIO_FORMAT_SCHEMA: Incomplete
QUEUE_ITEM_SCHEMA: Incomplete

def queue_item_dict_from_mass_item(mass: MusicAssistantClient, item: QueueItem | None) -> dict[str, Any] | None: ...

QUEUE_DETAILS_SCHEMA: Incomplete
