import datetime
import tibber
from .const import MANUFACTURER as MANUFACTURER
from .coordinator import TibberDataCoordinator as TibberDataCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS as SIGNAL_STRENGTH_DECIBELS, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import PlatformNotReady as PlatformNotReady
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from homeassistant.util import Throttle as Throttle
from typing import Any

_LOGGER: Incomplete
ICON: str
SCAN_INTERVAL: Incomplete
MIN_TIME_BETWEEN_UPDATES: Incomplete
PARALLEL_UPDATES: int
TWENTY_MINUTES: Incomplete
RT_SENSORS_UNIQUE_ID_MIGRATION: Incomplete
RT_SENSORS_UNIQUE_ID_MIGRATION_SIMPLE: Incomplete
RT_SENSORS: tuple[SensorEntityDescription, ...]
SENSORS: tuple[SensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TibberSensor(SensorEntity):
    _attr_has_entity_name: bool
    _tibber_home: Incomplete
    _home_name: Incomplete
    _device_name: str | None
    _model: str | None
    def __init__(self, *args: Any, tibber_home: tibber.TibberHome, **kwargs: Any) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...

class TibberSensorElPrice(TibberSensor):
    _attr_state_class: Incomplete
    _attr_translation_key: str
    _last_updated: datetime.datetime | None
    _spread_load_constant: Incomplete
    _attr_available: bool
    _attr_extra_state_attributes: Incomplete
    _attr_icon: Incomplete
    _attr_unique_id: Incomplete
    _model: str
    _device_name: Incomplete
    def __init__(self, tibber_home: tibber.TibberHome) -> None: ...
    _attr_native_unit_of_measurement: Incomplete
    async def async_update(self) -> None: ...
    async def _fetch_data(self) -> None: ...

class TibberDataSensor(TibberSensor, CoordinatorEntity[TibberDataCoordinator]):
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _device_name: Incomplete
    def __init__(self, tibber_home: tibber.TibberHome, coordinator: TibberDataCoordinator, entity_description: SensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...

class TibberSensorRT(TibberSensor, CoordinatorEntity['TibberRtDataCoordinator']):
    entity_description: Incomplete
    _model: str
    _device_name: Incomplete
    _attr_native_value: Incomplete
    _attr_unique_id: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    def __init__(self, tibber_home: tibber.TibberHome, description: SensorEntityDescription, initial_state: float, coordinator: TibberRtDataCoordinator) -> None: ...
    @property
    def available(self) -> bool: ...
    _attr_last_reset: Incomplete
    @callback
    def _handle_coordinator_update(self) -> None: ...

class TibberRtEntityCreator:
    _async_add_entities: Incomplete
    _tibber_home: Incomplete
    _added_sensors: set[str]
    _entity_registry: Incomplete
    def __init__(self, async_add_entities: AddEntitiesCallback, tibber_home: tibber.TibberHome, entity_registry: er.EntityRegistry) -> None: ...
    @callback
    def _migrate_unique_id(self, sensor_description: SensorEntityDescription) -> None: ...
    @callback
    def add_sensors(self, coordinator: TibberRtDataCoordinator, live_measurement: Any) -> None: ...

class TibberRtDataCoordinator(DataUpdateCoordinator):
    _add_sensor_callback: Incomplete
    _async_remove_device_updates_handler: Incomplete
    def __init__(self, add_sensor_callback: Callable[[TibberRtDataCoordinator, Any], None], tibber_home: tibber.TibberHome, hass: HomeAssistant) -> None: ...
    @callback
    def _handle_ha_stop(self, _event: Event) -> None: ...
    @callback
    def _data_updated(self) -> None: ...
    def get_live_measurement(self) -> Any: ...
