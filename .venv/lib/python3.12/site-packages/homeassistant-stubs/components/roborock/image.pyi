from . import RoborockConfigEntry as RoborockConfigEntry
from .const import DEFAULT_DRAWABLES as DEFAULT_DRAWABLES, DOMAIN as DOMAIN, DRAWABLES as DRAWABLES, IMAGE_CACHE_INTERVAL as IMAGE_CACHE_INTERVAL, MAP_SLEEP as MAP_SLEEP
from .coordinator import RoborockDataUpdateCoordinator as RoborockDataUpdateCoordinator
from .entity import RoborockCoordinatedEntityV1 as RoborockCoordinatedEntityV1
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.image import ImageEntity as ImageEntity
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util import slugify as slugify
from vacuum_map_parser_base.config.drawable import Drawable as Drawable

async def async_setup_entry(hass: HomeAssistant, config_entry: RoborockConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RoborockMap(RoborockCoordinatedEntityV1, ImageEntity):
    _attr_has_entity_name: bool
    image_last_updated: datetime
    _attr_name: Incomplete
    parser: Incomplete
    _attr_image_last_updated: Incomplete
    map_flag: Incomplete
    cached_map: Incomplete
    _attr_entity_category: Incomplete
    def __init__(self, unique_id: str, coordinator: RoborockDataUpdateCoordinator, map_flag: int, starting_map: bytes, map_name: str, drawables: list[Drawable]) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def is_selected(self) -> bool: ...
    def is_map_valid(self) -> bool: ...
    def _handle_coordinator_update(self) -> None: ...
    async def async_image(self) -> bytes | None: ...
    def _create_image(self, map_bytes: bytes) -> bytes: ...

async def create_coordinator_maps(coord: RoborockDataUpdateCoordinator, drawables: list[Drawable]) -> list[RoborockMap]: ...
