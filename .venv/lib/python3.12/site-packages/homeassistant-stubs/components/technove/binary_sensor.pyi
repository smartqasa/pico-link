from . import TechnoVEConfigEntry as TechnoVEConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import TechnoVEDataUpdateCoordinator as TechnoVEDataUpdateCoordinator
from .entity import TechnoVEEntity as TechnoVEEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue, async_delete_issue as async_delete_issue
from technove import Station as TechnoVEStation

@dataclass(frozen=True, kw_only=True)
class TechnoVEBinarySensorDescription(BinarySensorEntityDescription):
    deprecated_version: str | None = ...
    value_fn: Callable[[TechnoVEStation], bool | None]

BINARY_SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: TechnoVEConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TechnoVEBinarySensorEntity(TechnoVEEntity, BinarySensorEntity):
    entity_description: TechnoVEBinarySensorDescription
    def __init__(self, coordinator: TechnoVEDataUpdateCoordinator, description: TechnoVEBinarySensorDescription) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
    async def async_added_to_hass(self) -> None: ...
