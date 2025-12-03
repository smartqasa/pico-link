from .const import DOMAIN as DOMAIN
from .coordinator import ValloxDataUpdateCoordinator as ValloxDataUpdateCoordinator
from .entity import ValloxEntity as ValloxEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

class ValloxBinarySensorEntity(ValloxEntity, BinarySensorEntity):
    entity_description: ValloxBinarySensorEntityDescription
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, name: str, coordinator: ValloxDataUpdateCoordinator, description: ValloxBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool | None: ...

@dataclass(frozen=True, kw_only=True)
class ValloxBinarySensorEntityDescription(BinarySensorEntityDescription):
    metric_key: str

BINARY_SENSOR_ENTITIES: tuple[ValloxBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
