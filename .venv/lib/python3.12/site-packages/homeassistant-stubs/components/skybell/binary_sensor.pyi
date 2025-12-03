from . import DOMAIN as DOMAIN
from .coordinator import SkybellDataUpdateCoordinator as SkybellDataUpdateCoordinator
from .entity import SkybellEntity as SkybellEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

BINARY_SENSOR_TYPES: tuple[BinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SkybellBinarySensor(SkybellEntity, BinarySensorEntity):
    _event: dict[str, str]
    def __init__(self, coordinator: SkybellDataUpdateCoordinator, description: BinarySensorEntityDescription) -> None: ...
    _attr_is_on: Incomplete
    @callback
    def _handle_coordinator_update(self) -> None: ...
