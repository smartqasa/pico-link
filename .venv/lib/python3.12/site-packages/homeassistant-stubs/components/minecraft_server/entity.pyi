from .api import MinecraftServerType as MinecraftServerType
from .const import DOMAIN as DOMAIN
from .coordinator import MinecraftServerCoordinator as MinecraftServerCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_TYPE as CONF_TYPE
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

MANUFACTURER: str

class MinecraftServerEntity(CoordinatorEntity[MinecraftServerCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: MinecraftServerCoordinator, config_entry: ConfigEntry) -> None: ...
