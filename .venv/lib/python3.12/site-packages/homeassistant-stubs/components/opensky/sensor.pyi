from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from .coordinator import OpenSkyDataUpdateCoordinator as OpenSkyDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OpenSkySensor(CoordinatorEntity[OpenSkyDataUpdateCoordinator], SensorEntity):
    _attr_attribution: str
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_translation_key: str
    _attr_native_unit_of_measurement: str
    _attr_state_class: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: OpenSkyDataUpdateCoordinator, config_entry: ConfigEntry) -> None: ...
    @property
    def native_value(self) -> int: ...
