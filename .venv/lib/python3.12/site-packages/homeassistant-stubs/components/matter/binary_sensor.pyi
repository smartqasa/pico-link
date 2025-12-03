from .entity import MatterEntity as MatterEntity, MatterEntityDescription as MatterEntityDescription
from .helpers import get_matter as get_matter
from .models import MatterDiscoverySchema as MatterDiscoverySchema
from _typeshed import Incomplete
from chip.clusters.Objects import uint as uint
from chip.clusters.Types import Nullable as Nullable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

@dataclass(frozen=True)
class MatterBinarySensorEntityDescription(BinarySensorEntityDescription, MatterEntityDescription): ...

class MatterBinarySensor(MatterEntity, BinarySensorEntity):
    entity_description: MatterBinarySensorEntityDescription
    _attr_is_on: Incomplete
    @callback
    def _update_from_device(self) -> None: ...

DISCOVERY_SCHEMAS: Incomplete
