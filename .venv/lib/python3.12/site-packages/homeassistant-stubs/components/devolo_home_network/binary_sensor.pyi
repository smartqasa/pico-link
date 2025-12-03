from . import DevoloHomeNetworkConfigEntry as DevoloHomeNetworkConfigEntry
from .const import CONNECTED_PLC_DEVICES as CONNECTED_PLC_DEVICES, CONNECTED_TO_ROUTER as CONNECTED_TO_ROUTER
from .coordinator import DevoloDataUpdateCoordinator as DevoloDataUpdateCoordinator
from .entity import DevoloCoordinatorEntity as DevoloCoordinatorEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from devolo_plc_api.plcnet_api import LogicalNetwork
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

PARALLEL_UPDATES: int

def _is_connected_to_router(entity: DevoloBinarySensorEntity) -> bool: ...

@dataclass(frozen=True, kw_only=True)
class DevoloBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_func: Callable[[DevoloBinarySensorEntity], bool]

SENSOR_TYPES: dict[str, DevoloBinarySensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: DevoloHomeNetworkConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DevoloBinarySensorEntity(DevoloCoordinatorEntity[LogicalNetwork], BinarySensorEntity):
    entity_description: DevoloBinarySensorEntityDescription
    def __init__(self, entry: DevoloHomeNetworkConfigEntry, coordinator: DevoloDataUpdateCoordinator[LogicalNetwork], description: DevoloBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
