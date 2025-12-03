from .const import CONF_PLACE_ID as CONF_PLACE_ID, CONF_SERVICE_ID as CONF_SERVICE_ID, DOMAIN as DOMAIN
from _typeshed import Incomplete
from aiorecollect.client import PickupEvent
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator

class ReCollectWasteEntity(CoordinatorEntity[DataUpdateCoordinator[list[PickupEvent]]]):
    _attr_has_entity_name: bool
    _identifier: Incomplete
    _attr_device_info: Incomplete
    _attr_extra_state_attributes: Incomplete
    _entry: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator[list[PickupEvent]], entry: ConfigEntry) -> None: ...
    async def async_added_to_hass(self) -> None: ...
