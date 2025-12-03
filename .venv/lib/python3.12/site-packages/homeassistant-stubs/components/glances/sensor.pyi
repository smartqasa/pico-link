from . import GlancesConfigEntry as GlancesConfigEntry, GlancesDataUpdateCoordinator as GlancesDataUpdateCoordinator
from .const import CPU_ICON as CPU_ICON, DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import PERCENTAGE as PERCENTAGE, REVOLUTIONS_PER_MINUTE as REVOLUTIONS_PER_MINUTE, UnitOfDataRate as UnitOfDataRate, UnitOfInformation as UnitOfInformation, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

@dataclass(frozen=True, kw_only=True)
class GlancesSensorEntityDescription(SensorEntityDescription):
    type: str

SENSOR_TYPES: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: GlancesConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class GlancesSensor(CoordinatorEntity[GlancesDataUpdateCoordinator], SensorEntity):
    entity_description: GlancesSensorEntityDescription
    _attr_has_entity_name: bool
    _data_valid: bool
    _sensor_label: Incomplete
    _attr_translation_placeholders: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: GlancesDataUpdateCoordinator, description: GlancesSensorEntityDescription, sensor_label: str = '') -> None: ...
    @property
    def available(self) -> bool: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    _attr_native_value: Incomplete
    def _update_native_value(self) -> None: ...
    def _update_data_valid(self) -> None: ...
