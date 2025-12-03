from . import SensiboConfigEntry as SensiboConfigEntry
from .coordinator import SensiboDataUpdateCoordinator as SensiboDataUpdateCoordinator
from .entity import SensiboDeviceBaseEntity as SensiboDeviceBaseEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pysensibo.model import SensiboDevice as SensiboDevice

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class SensiboDeviceUpdateEntityDescription(UpdateEntityDescription):
    value_version: Callable[[SensiboDevice], str | None]
    value_available: Callable[[SensiboDevice], str | None]

DEVICE_SENSOR_TYPES: tuple[SensiboDeviceUpdateEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: SensiboConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SensiboDeviceUpdate(SensiboDeviceBaseEntity, UpdateEntity):
    entity_description: SensiboDeviceUpdateEntityDescription
    _attr_unique_id: Incomplete
    _attr_title: Incomplete
    def __init__(self, coordinator: SensiboDataUpdateCoordinator, device_id: str, entity_description: SensiboDeviceUpdateEntityDescription) -> None: ...
    @property
    def installed_version(self) -> str | None: ...
    @property
    def latest_version(self) -> str | None: ...
