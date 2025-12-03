from .const import DOMAIN as DOMAIN
from .coordinator import FluxLedUpdateCoordinator as FluxLedUpdateCoordinator
from .entity import FluxEntity as FluxEntity
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FluxPairedRemotes(FluxEntity, SensorEntity):
    _attr_entity_category: Incomplete
    _attr_translation_key: str
    @property
    def native_value(self) -> int: ...
