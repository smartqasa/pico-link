from .const import ATTR_DESTINATION as ATTR_DESTINATION, ATTR_DESTINATION_NAME as ATTR_DESTINATION_NAME, ATTR_DISTANCE as ATTR_DISTANCE, ATTR_DURATION as ATTR_DURATION, ATTR_DURATION_IN_TRAFFIC as ATTR_DURATION_IN_TRAFFIC, ATTR_ORIGIN as ATTR_ORIGIN, ATTR_ORIGIN_NAME as ATTR_ORIGIN_NAME, DOMAIN as DOMAIN, ICONS as ICONS, ICON_CAR as ICON_CAR
from .coordinator import HERERoutingDataUpdateCoordinator as HERERoutingDataUpdateCoordinator, HERETransitDataUpdateCoordinator as HERETransitDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components.sensor import RestoreSensor as RestoreSensor, SensorDeviceClass as SensorDeviceClass, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ATTRIBUTION as ATTR_ATTRIBUTION, ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, CONF_MODE as CONF_MODE, CONF_NAME as CONF_NAME, UnitOfLength as UnitOfLength, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

SCAN_INTERVAL: Incomplete

def sensor_descriptions(travel_mode: str) -> tuple[SensorEntityDescription, ...]: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HERETravelTimeSensor(CoordinatorEntity[HERERoutingDataUpdateCoordinator | HERETransitDataUpdateCoordinator], RestoreSensor):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, unique_id_prefix: str, name: str, sensor_description: SensorEntityDescription, coordinator: HERERoutingDataUpdateCoordinator | HERETransitDataUpdateCoordinator) -> None: ...
    _attr_native_value: Incomplete
    async def _async_restore_state(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    @property
    def attribution(self) -> str | None: ...

class OriginSensor(HERETravelTimeSensor):
    def __init__(self, unique_id_prefix: str, name: str, coordinator: HERERoutingDataUpdateCoordinator) -> None: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any] | None: ...

class DestinationSensor(HERETravelTimeSensor):
    def __init__(self, unique_id_prefix: str, name: str, coordinator: HERERoutingDataUpdateCoordinator) -> None: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any] | None: ...
