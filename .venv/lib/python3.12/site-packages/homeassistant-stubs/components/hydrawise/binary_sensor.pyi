from .const import DOMAIN as DOMAIN, SERVICE_RESUME as SERVICE_RESUME, SERVICE_START_WATERING as SERVICE_START_WATERING, SERVICE_SUSPEND as SERVICE_SUSPEND
from .coordinator import HydrawiseUpdateCoordinators as HydrawiseUpdateCoordinators
from .entity import HydrawiseEntity as HydrawiseEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import VolDictType as VolDictType
from pydrawise import Zone as Zone

@dataclass(frozen=True, kw_only=True)
class HydrawiseBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[HydrawiseBinarySensor], bool | None]
    always_available: bool = ...

CONTROLLER_BINARY_SENSORS: tuple[HydrawiseBinarySensorEntityDescription, ...]
RAIN_SENSOR_BINARY_SENSOR: tuple[HydrawiseBinarySensorEntityDescription, ...]
ZONE_BINARY_SENSORS: tuple[HydrawiseBinarySensorEntityDescription, ...]
SCHEMA_START_WATERING: VolDictType
SCHEMA_SUSPEND: VolDictType

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HydrawiseBinarySensor(HydrawiseEntity, BinarySensorEntity):
    entity_description: HydrawiseBinarySensorEntityDescription
    _attr_is_on: Incomplete
    def _update_attrs(self) -> None: ...
    @property
    def available(self) -> bool: ...

class HydrawiseZoneBinarySensor(HydrawiseBinarySensor):
    zone: Zone
    async def start_watering(self, duration: int | None = None) -> None: ...
    async def suspend(self, until: datetime) -> None: ...
    async def resume(self) -> None: ...
