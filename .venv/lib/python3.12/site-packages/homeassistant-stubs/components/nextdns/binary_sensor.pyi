from . import NextDnsConfigEntry as NextDnsConfigEntry
from .coordinator import NextDnsUpdateCoordinator as NextDnsUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from nextdns import ConnectionStatus

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class NextDnsBinarySensorEntityDescription(BinarySensorEntityDescription):
    state: Callable[[ConnectionStatus, str], bool]

SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: NextDnsConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NextDnsBinarySensor(CoordinatorEntity[NextDnsUpdateCoordinator[ConnectionStatus]], BinarySensorEntity):
    _attr_has_entity_name: bool
    entity_description: NextDnsBinarySensorEntityDescription
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    _attr_is_on: Incomplete
    def __init__(self, coordinator: NextDnsUpdateCoordinator[ConnectionStatus], description: NextDnsBinarySensorEntityDescription) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
