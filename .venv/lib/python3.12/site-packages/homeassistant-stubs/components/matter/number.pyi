from .entity import MatterEntity as MatterEntity, MatterEntityDescription as MatterEntityDescription
from .helpers import get_matter as get_matter
from .models import MatterDiscoverySchema as MatterDiscoverySchema
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription, NumberMode as NumberMode
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, Platform as Platform, UnitOfLength as UnitOfLength, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

@dataclass(frozen=True)
class MatterNumberEntityDescription(NumberEntityDescription, MatterEntityDescription): ...

class MatterNumber(MatterEntity, NumberEntity):
    entity_description: MatterNumberEntityDescription
    async def async_set_native_value(self, value: float) -> None: ...
    _attr_native_value: Incomplete
    @callback
    def _update_from_device(self) -> None: ...

DISCOVERY_SCHEMAS: Incomplete
