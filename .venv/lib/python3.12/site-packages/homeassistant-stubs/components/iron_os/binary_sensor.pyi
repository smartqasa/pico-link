from . import IronOSConfigEntry as IronOSConfigEntry
from .coordinator import IronOSLiveDataCoordinator as IronOSLiveDataCoordinator
from .entity import IronOSBaseEntity as IronOSBaseEntity
from enum import StrEnum
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

PARALLEL_UPDATES: int

class PinecilBinarySensor(StrEnum):
    TIP_CONNECTED = 'tip_connected'

async def async_setup_entry(hass: HomeAssistant, entry: IronOSConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class IronOSBinarySensorEntity(IronOSBaseEntity, BinarySensorEntity):
    coordinator: IronOSLiveDataCoordinator
    @property
    def is_on(self) -> bool | None: ...
