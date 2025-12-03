from .coordinator import SteamistDataUpdateCoordinator as SteamistDataUpdateCoordinator
from _typeshed import Incomplete
from aiosteamist import SteamistStatus as SteamistStatus
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MODEL as CONF_MODEL
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class SteamistEntity(CoordinatorEntity[SteamistDataUpdateCoordinator], Entity):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: SteamistDataUpdateCoordinator, entry: ConfigEntry, description: EntityDescription) -> None: ...
    @property
    def _status(self) -> SteamistStatus: ...
