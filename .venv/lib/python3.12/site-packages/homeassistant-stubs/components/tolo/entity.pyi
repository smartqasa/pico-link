from .const import DOMAIN as DOMAIN
from .coordinator import ToloSaunaUpdateCoordinator as ToloSaunaUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class ToloSaunaCoordinatorEntity(CoordinatorEntity[ToloSaunaUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: ToloSaunaUpdateCoordinator, entry: ConfigEntry) -> None: ...
