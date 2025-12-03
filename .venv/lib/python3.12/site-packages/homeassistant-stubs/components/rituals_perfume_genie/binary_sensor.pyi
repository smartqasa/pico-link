from .const import DOMAIN as DOMAIN
from .coordinator import RitualsDataUpdateCoordinator as RitualsDataUpdateCoordinator
from .entity import DiffuserEntity as DiffuserEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyrituals import Diffuser as Diffuser

@dataclass(frozen=True, kw_only=True)
class RitualsBinarySensorEntityDescription(BinarySensorEntityDescription):
    is_on_fn: Callable[[Diffuser], bool]
    has_fn: Callable[[Diffuser], bool]

ENTITY_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RitualsBinarySensorEntity(DiffuserEntity, BinarySensorEntity):
    entity_description: RitualsBinarySensorEntityDescription
    @property
    def is_on(self) -> bool: ...
