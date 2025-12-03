from .const import CONF_LICENSE_PLATE as CONF_LICENSE_PLATE, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import date
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from vehicle import Vehicle

@dataclass(frozen=True, kw_only=True)
class RDWSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Vehicle], date | str | float | None]

SENSORS: tuple[RDWSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RDWSensorEntity(CoordinatorEntity[DataUpdateCoordinator[Vehicle]], SensorEntity):
    entity_description: RDWSensorEntityDescription
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, *, coordinator: DataUpdateCoordinator[Vehicle], license_plate: str, description: RDWSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> date | str | float | None: ...
