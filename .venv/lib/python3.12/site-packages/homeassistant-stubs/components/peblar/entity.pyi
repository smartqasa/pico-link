from .const import DOMAIN as DOMAIN
from .coordinator import PeblarConfigEntry as PeblarConfigEntry
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

class PeblarEntity[_DataUpdateCoordinatorT: DataUpdateCoordinator[Any]](CoordinatorEntity[_DataUpdateCoordinatorT]):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, *, entry: PeblarConfigEntry, coordinator: _DataUpdateCoordinatorT, description: EntityDescription) -> None: ...
