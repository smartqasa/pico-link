from . import AirzoneConfigEntry as AirzoneConfigEntry
from .coordinator import AirzoneUpdateCoordinator as AirzoneUpdateCoordinator
from .entity import AirzoneEntity as AirzoneEntity, AirzoneSystemEntity as AirzoneSystemEntity, AirzoneZoneEntity as AirzoneZoneEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Final

@dataclass(frozen=True)
class AirzoneBinarySensorEntityDescription(BinarySensorEntityDescription):
    attributes: dict[str, str] | None = ...

SYSTEM_BINARY_SENSOR_TYPES: Final[tuple[AirzoneBinarySensorEntityDescription, ...]]
ZONE_BINARY_SENSOR_TYPES: Final[tuple[AirzoneBinarySensorEntityDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: AirzoneConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AirzoneBinarySensor(AirzoneEntity, BinarySensorEntity):
    entity_description: AirzoneBinarySensorEntityDescription
    @callback
    def _handle_coordinator_update(self) -> None: ...
    _attr_is_on: Incomplete
    _attr_extra_state_attributes: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...

class AirzoneSystemBinarySensor(AirzoneSystemEntity, AirzoneBinarySensor):
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: AirzoneUpdateCoordinator, description: AirzoneBinarySensorEntityDescription, entry: ConfigEntry, system_id: str, system_data: dict[str, Any]) -> None: ...

class AirzoneZoneBinarySensor(AirzoneZoneEntity, AirzoneBinarySensor):
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: AirzoneUpdateCoordinator, description: AirzoneBinarySensorEntityDescription, entry: ConfigEntry, system_zone_id: str, zone_data: dict[str, Any]) -> None: ...
