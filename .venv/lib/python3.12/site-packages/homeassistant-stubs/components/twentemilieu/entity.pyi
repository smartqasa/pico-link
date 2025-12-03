from .const import DOMAIN as DOMAIN
from .coordinator import TwenteMilieuConfigEntry as TwenteMilieuConfigEntry, TwenteMilieuDataUpdateCoordinator as TwenteMilieuDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_ID as CONF_ID
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class TwenteMilieuEntity(CoordinatorEntity[TwenteMilieuDataUpdateCoordinator], Entity):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, entry: TwenteMilieuConfigEntry) -> None: ...
