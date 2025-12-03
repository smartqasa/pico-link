from . import WLEDConfigEntry as WLEDConfigEntry
from .coordinator import WLEDDataUpdateCoordinator as WLEDDataUpdateCoordinator
from .entity import WLEDEntity as WLEDEntity
from .helpers import wled_exception_handler as wled_exception_handler
from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: WLEDConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WLEDLiveOverrideSelect(WLEDEntity, SelectEntity):
    _attr_entity_category: Incomplete
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    _attr_options: Incomplete
    def __init__(self, coordinator: WLEDDataUpdateCoordinator) -> None: ...
    @property
    def current_option(self) -> str: ...
    @wled_exception_handler
    async def async_select_option(self, option: str) -> None: ...

class WLEDPresetSelect(WLEDEntity, SelectEntity):
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    _attr_options: Incomplete
    def __init__(self, coordinator: WLEDDataUpdateCoordinator) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def current_option(self) -> str | None: ...
    @wled_exception_handler
    async def async_select_option(self, option: str) -> None: ...

class WLEDPlaylistSelect(WLEDEntity, SelectEntity):
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    _attr_options: Incomplete
    def __init__(self, coordinator: WLEDDataUpdateCoordinator) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def current_option(self) -> str | None: ...
    @wled_exception_handler
    async def async_select_option(self, option: str) -> None: ...

class WLEDPaletteSelect(WLEDEntity, SelectEntity):
    _attr_entity_category: Incomplete
    _attr_translation_key: str
    _segment: int
    _attr_translation_placeholders: Incomplete
    _attr_unique_id: Incomplete
    _attr_options: Incomplete
    def __init__(self, coordinator: WLEDDataUpdateCoordinator, segment: int) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def current_option(self) -> str | None: ...
    @wled_exception_handler
    async def async_select_option(self, option: str) -> None: ...

@callback
def async_update_segments(coordinator: WLEDDataUpdateCoordinator, current_ids: set[int], async_add_entities: AddEntitiesCallback) -> None: ...
