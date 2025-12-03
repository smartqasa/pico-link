from . import RenaultConfigEntry as RenaultConfigEntry
from .entity import RenaultDataEntity as RenaultDataEntity, RenaultDataEntityDescription as RenaultDataEntityDescription
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from renault_api.kamereon.models import KamereonVehicleBatteryStatusData

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class RenaultBinarySensorEntityDescription(BinarySensorEntityDescription, RenaultDataEntityDescription):
    on_key: str
    on_value: StateType | list[StateType]

async def async_setup_entry(hass: HomeAssistant, config_entry: RenaultConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RenaultBinarySensor(RenaultDataEntity[KamereonVehicleBatteryStatusData], BinarySensorEntity):
    entity_description: RenaultBinarySensorEntityDescription
    @property
    def is_on(self) -> bool | None: ...

BINARY_SENSOR_TYPES: tuple[RenaultBinarySensorEntityDescription, ...]
