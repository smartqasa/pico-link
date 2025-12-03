from .const import DOMAIN as DOMAIN
from .coordinator import RitualsDataUpdateCoordinator as RitualsDataUpdateCoordinator
from .entity import DiffuserEntity as DiffuserEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyrituals import Diffuser as Diffuser

@dataclass(frozen=True, kw_only=True)
class RitualsSensorEntityDescription(SensorEntityDescription):
    has_fn: Callable[[Diffuser], bool] = ...
    value_fn: Callable[[Diffuser], int | str]

ENTITY_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RitualsSensorEntity(DiffuserEntity, SensorEntity):
    entity_description: RitualsSensorEntityDescription
    _attr_entity_category: Incomplete
    @property
    def native_value(self) -> str | int: ...
