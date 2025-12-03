from . import RainMachineConfigEntry as RainMachineConfigEntry
from .const import DATA_PROVISION_SETTINGS as DATA_PROVISION_SETTINGS, DATA_RESTRICTIONS_CURRENT as DATA_RESTRICTIONS_CURRENT
from .entity import RainMachineEntity as RainMachineEntity, RainMachineEntityDescription as RainMachineEntityDescription
from .util import EntityDomainReplacementStrategy as EntityDomainReplacementStrategy, async_finish_entity_domain_replacements as async_finish_entity_domain_replacements, key_exists as key_exists
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

TYPE_FLOW_SENSOR: str
TYPE_FREEZE: str
TYPE_HOURLY: str
TYPE_MONTH: str
TYPE_RAINDELAY: str
TYPE_RAINSENSOR: str
TYPE_WEEKDAY: str

@dataclass(frozen=True, kw_only=True)
class RainMachineBinarySensorDescription(BinarySensorEntityDescription, RainMachineEntityDescription):
    data_key: str

BINARY_SENSOR_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: RainMachineConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class CurrentRestrictionsBinarySensor(RainMachineEntity, BinarySensorEntity):
    entity_description: RainMachineBinarySensorDescription
    _attr_is_on: Incomplete
    @callback
    def update_from_latest_data(self) -> None: ...

class ProvisionSettingsBinarySensor(RainMachineEntity, BinarySensorEntity):
    entity_description: RainMachineBinarySensorDescription
    _attr_is_on: Incomplete
    @callback
    def update_from_latest_data(self) -> None: ...
