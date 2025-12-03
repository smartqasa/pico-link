from . import YaleConfigEntry as YaleConfigEntry
from .coordinator import YaleDataUpdateCoordinator as YaleDataUpdateCoordinator
from .entity import YaleLockEntity as YaleLockEntity
from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from yalesmartalarmclient import YaleLock as YaleLock

VOLUME_OPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: YaleConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class YaleLockVolumeSelect(YaleLockEntity, SelectEntity):
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    _attr_current_option: Incomplete
    _attr_options: Incomplete
    def __init__(self, coordinator: YaleDataUpdateCoordinator, lock: YaleLock) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
