from .const import DOMAIN as DOMAIN
from .coordinator import OpenexchangeratesCoordinator as OpenexchangeratesCoordinator
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_QUOTE as CONF_QUOTE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

ATTRIBUTION: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OpenexchangeratesSensor(CoordinatorEntity[OpenexchangeratesCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    _attr_attribution = ATTRIBUTION
    _attr_device_info: Incomplete
    _attr_entity_registry_enabled_default: Incomplete
    _attr_name: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_unique_id: Incomplete
    _quote: Incomplete
    def __init__(self, config_entry: ConfigEntry, coordinator: OpenexchangeratesCoordinator, quote: str, enabled: bool) -> None: ...
    @property
    def native_value(self) -> float: ...
