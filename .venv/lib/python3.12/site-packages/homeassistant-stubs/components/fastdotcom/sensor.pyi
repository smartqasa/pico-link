from .const import DOMAIN as DOMAIN
from .coordinator import FastdotcomDataUpdateCoordinator as FastdotcomDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfDataRate as UnitOfDataRate
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SpeedtestSensor(CoordinatorEntity[FastdotcomDataUpdateCoordinator], SensorEntity):
    _attr_translation_key: str
    _attr_device_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_state_class: Incomplete
    _attr_should_poll: bool
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, entry_id: str, coordinator: FastdotcomDataUpdateCoordinator) -> None: ...
    @property
    def native_value(self) -> float: ...
