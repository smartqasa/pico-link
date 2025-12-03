from .const import DATA_COORDINATOR as DATA_COORDINATOR, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from .coordinator import CanaryDataUpdateCoordinator as CanaryDataUpdateCoordinator
from _typeshed import Incomplete
from canary.model import Device as Device, Location as Location
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Final

type SensorTypeItem = tuple[str, str | None, str | None, SensorDeviceClass | None, list[str]]
SENSOR_VALUE_PRECISION: Final[int]
ATTR_AIR_QUALITY: Final[str]
CANARY_PRO: Final[str]
CANARY_FLEX: Final[str]
SENSOR_TYPES: Final[list[SensorTypeItem]]
STATE_AIR_QUALITY_NORMAL: Final[str]
STATE_AIR_QUALITY_ABNORMAL: Final[str]
STATE_AIR_QUALITY_VERY_ABNORMAL: Final[str]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class CanarySensor(CoordinatorEntity[CanaryDataUpdateCoordinator], SensorEntity):
    _sensor_type: Incomplete
    _device_id: Incomplete
    _attr_name: Incomplete
    _canary_type: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_device_class: Incomplete
    _attr_icon: Incomplete
    def __init__(self, coordinator: CanaryDataUpdateCoordinator, sensor_type: SensorTypeItem, location: Location, device: Device) -> None: ...
    @property
    def reading(self) -> float | None: ...
    @property
    def native_value(self) -> float | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, str] | None: ...
