from .const import DOMAIN as DOMAIN
from .coordinator import StarlinkData as StarlinkData
from .entity import StarlinkEntity as StarlinkEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

@dataclass(frozen=True, kw_only=True)
class StarlinkBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[StarlinkData], bool | None]

class StarlinkBinarySensorEntity(StarlinkEntity, BinarySensorEntity):
    entity_description: StarlinkBinarySensorEntityDescription
    @property
    def is_on(self) -> bool | None: ...

BINARY_SENSORS: Incomplete
