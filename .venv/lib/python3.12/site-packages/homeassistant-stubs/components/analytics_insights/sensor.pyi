from . import AnalyticsInsightsConfigEntry as AnalyticsInsightsConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import AnalyticsData as AnalyticsData, HomeassistantAnalyticsDataUpdateCoordinator as HomeassistantAnalyticsDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

@dataclass(frozen=True, kw_only=True)
class AnalyticsSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[AnalyticsData], StateType]

def get_addon_entity_description(name_slug: str) -> AnalyticsSensorEntityDescription: ...
def get_core_integration_entity_description(domain: str, name: str) -> AnalyticsSensorEntityDescription: ...
def get_custom_integration_entity_description(domain: str) -> AnalyticsSensorEntityDescription: ...

GENERAL_SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: AnalyticsInsightsConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HomeassistantAnalyticsSensor(CoordinatorEntity[HomeassistantAnalyticsDataUpdateCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    _attr_entity_category: Incomplete
    entity_description: AnalyticsSensorEntityDescription
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: HomeassistantAnalyticsDataUpdateCoordinator, entity_description: AnalyticsSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
