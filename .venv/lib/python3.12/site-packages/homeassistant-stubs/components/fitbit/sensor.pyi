from .api import FitbitApi as FitbitApi
from .const import ATTRIBUTION as ATTRIBUTION, BATTERY_LEVELS as BATTERY_LEVELS, DOMAIN as DOMAIN, FitbitScope as FitbitScope, FitbitUnitSystem as FitbitUnitSystem
from .coordinator import FitbitData as FitbitData, FitbitDeviceCoordinator as FitbitDeviceCoordinator
from .exceptions import FitbitApiException as FitbitApiException, FitbitAuthException as FitbitAuthException
from .model import FitbitDevice as FitbitDevice, config_from_entry_data as config_from_entry_data
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfLength as UnitOfLength, UnitOfMass as UnitOfMass, UnitOfTime as UnitOfTime, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.icon import icon_for_battery_level as icon_for_battery_level
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any, Final

_LOGGER: Final[Incomplete]
_CONFIGURING: dict[str, str]
SCAN_INTERVAL: Final[Incomplete]
FITBIT_TRACKER_SUBSTRING: str

def _default_value_fn(result: dict[str, Any]) -> str: ...
def _distance_value_fn(result: dict[str, Any]) -> int | str: ...
def _body_value_fn(result: dict[str, Any]) -> int | str: ...
def _clock_format_12h(result: dict[str, Any]) -> str: ...
def _weight_unit(unit_system: FitbitUnitSystem) -> UnitOfMass: ...
def _distance_unit(unit_system: FitbitUnitSystem) -> UnitOfLength: ...
def _elevation_unit(unit_system: FitbitUnitSystem) -> UnitOfLength: ...
def _water_unit(unit_system: FitbitUnitSystem) -> UnitOfVolume: ...
def _int_value_or_none(field: str) -> Callable[[dict[str, Any]], int | None]: ...

@dataclass(frozen=True)
class FitbitSensorEntityDescription(SensorEntityDescription):
    unit_type: str | None = ...
    value_fn: Callable[[dict[str, Any]], Any] = ...
    unit_fn: Callable[[FitbitUnitSystem], str | None] = ...
    scope: FitbitScope | None = ...
    @property
    def is_tracker(self) -> bool: ...

def _build_device_info(config_entry: ConfigEntry, entity_description: FitbitSensorEntityDescription) -> DeviceInfo: ...

FITBIT_RESOURCES_LIST: Final[tuple[FitbitSensorEntityDescription, ...]]
SLEEP_START_TIME: Incomplete
SLEEP_START_TIME_12HR: Incomplete
FITBIT_RESOURCE_BATTERY: Incomplete
FITBIT_RESOURCE_BATTERY_LEVEL: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FitbitSensor(SensorEntity):
    entity_description: FitbitSensorEntityDescription
    _attr_attribution = ATTRIBUTION
    _attr_has_entity_name: bool
    config_entry: Incomplete
    api: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_entity_registry_enabled_default: bool
    def __init__(self, config_entry: ConfigEntry, api: FitbitApi, user_profile_id: str, description: FitbitSensorEntityDescription, units: str | None, enable_default_override: bool, device_info: DeviceInfo) -> None: ...
    _attr_available: bool
    _attr_native_value: Incomplete
    async def async_update(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...

class FitbitBatterySensor(CoordinatorEntity[FitbitDeviceCoordinator], SensorEntity):
    entity_description: FitbitSensorEntityDescription
    _attr_attribution = ATTRIBUTION
    device: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_entity_registry_enabled_default: bool
    def __init__(self, coordinator: FitbitDeviceCoordinator, user_profile_id: str, description: FitbitSensorEntityDescription, device: FitbitDevice, enable_default_override: bool) -> None: ...
    @property
    def icon(self) -> str | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, str | None]: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_native_value: Incomplete
    @callback
    def _handle_coordinator_update(self) -> None: ...

class FitbitBatteryLevelSensor(CoordinatorEntity[FitbitDeviceCoordinator], SensorEntity):
    entity_description: FitbitSensorEntityDescription
    _attr_attribution = ATTRIBUTION
    device: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: FitbitDeviceCoordinator, user_profile_id: str, description: FitbitSensorEntityDescription, device: FitbitDevice) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_native_value: Incomplete
    @callback
    def _handle_coordinator_update(self) -> None: ...
