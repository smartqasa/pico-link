from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import callback as callback
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator

class AirVisualEntity(CoordinatorEntity):
    _attr_extra_state_attributes: Incomplete
    _entry: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator, entry: ConfigEntry, description: EntityDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def update_from_latest_data(self) -> None: ...
