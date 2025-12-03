from . import NextDnsConfigEntry as NextDnsConfigEntry
from .const import ATTR_DNSSEC as ATTR_DNSSEC, ATTR_ENCRYPTION as ATTR_ENCRYPTION, ATTR_IP_VERSIONS as ATTR_IP_VERSIONS, ATTR_PROTOCOLS as ATTR_PROTOCOLS, ATTR_STATUS as ATTR_STATUS
from .coordinator import CoordinatorDataT as CoordinatorDataT, NextDnsUpdateCoordinator as NextDnsUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Generic

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class NextDnsSensorEntityDescription(SensorEntityDescription, Generic[CoordinatorDataT]):
    coordinator_type: str
    value: Callable[[CoordinatorDataT], StateType]

SENSORS: tuple[NextDnsSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: NextDnsConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NextDnsSensor(CoordinatorEntity[NextDnsUpdateCoordinator[CoordinatorDataT]], SensorEntity):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    _attr_native_value: Incomplete
    entity_description: NextDnsSensorEntityDescription
    def __init__(self, coordinator: NextDnsUpdateCoordinator[CoordinatorDataT], description: NextDnsSensorEntityDescription) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
