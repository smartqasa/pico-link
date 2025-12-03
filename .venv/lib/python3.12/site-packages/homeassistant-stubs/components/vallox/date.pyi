from .const import DOMAIN as DOMAIN
from .coordinator import ValloxDataUpdateCoordinator as ValloxDataUpdateCoordinator
from .entity import ValloxEntity as ValloxEntity
from _typeshed import Incomplete
from datetime import date
from homeassistant.components.date import DateEntity as DateEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from vallox_websocket_api import Vallox as Vallox

class ValloxFilterChangeDateEntity(ValloxEntity, DateEntity):
    _attr_entity_category: Incomplete
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    _client: Incomplete
    def __init__(self, name: str, coordinator: ValloxDataUpdateCoordinator, client: Vallox) -> None: ...
    @property
    def native_value(self) -> date | None: ...
    async def async_set_value(self, value: date) -> None: ...

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
