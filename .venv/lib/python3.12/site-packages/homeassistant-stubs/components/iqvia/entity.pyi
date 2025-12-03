from .const import CONF_ZIP_CODE as CONF_ZIP_CODE, DOMAIN as DOMAIN, TYPE_ALLERGY_FORECAST as TYPE_ALLERGY_FORECAST, TYPE_ALLERGY_OUTLOOK as TYPE_ALLERGY_OUTLOOK
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import callback as callback
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

class IQVIAEntity(CoordinatorEntity[DataUpdateCoordinator[dict[str, Any]]]):
    _attr_has_entity_name: bool
    _attr_extra_state_attributes: Incomplete
    _attr_unique_id: Incomplete
    _entry: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator[dict[str, Any]], entry: ConfigEntry, description: EntityDescription) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def update_from_latest_data(self) -> None: ...
