from . import PingConfigEntry as PingConfigEntry
from .const import CONF_IMPORTED_BY as CONF_IMPORTED_BY
from .coordinator import PingUpdateCoordinator as PingUpdateCoordinator
from .entity import PingEntity as PingEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: PingConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PingBinarySensor(PingEntity, BinarySensorEntity):
    _attr_device_class: Incomplete
    _attr_available: bool
    _attr_name: Incomplete
    _attr_entity_registry_enabled_default: Incomplete
    def __init__(self, config_entry: ConfigEntry, coordinator: PingUpdateCoordinator) -> None: ...
    @property
    def is_on(self) -> bool: ...
