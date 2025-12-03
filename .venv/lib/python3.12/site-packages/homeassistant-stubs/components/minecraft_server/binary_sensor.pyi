from .const import DOMAIN as DOMAIN
from .coordinator import MinecraftServerCoordinator as MinecraftServerCoordinator
from .entity import MinecraftServerEntity as MinecraftServerEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

KEY_STATUS: str
BINARY_SENSOR_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MinecraftServerBinarySensorEntity(MinecraftServerEntity, BinarySensorEntity):
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_is_on: bool
    def __init__(self, coordinator: MinecraftServerCoordinator, description: BinarySensorEntityDescription, config_entry: ConfigEntry) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def is_on(self) -> bool: ...
