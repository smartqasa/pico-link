from .const import DOMAIN as DOMAIN
from .coordinator import LaundrifyUpdateCoordinator as LaundrifyUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from laundrify_aio import LaundrifyDevice as LaundrifyDevice

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LaundrifyBaseSensor(SensorEntity):
    _attr_has_entity_name: bool
    _device: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, device: LaundrifyDevice) -> None: ...

class LaundrifyPowerSensor(LaundrifyBaseSensor):
    _attr_device_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_state_class: Incomplete
    _attr_suggested_display_precision: int
    _attr_available: bool
    _attr_native_value: Incomplete
    async def async_update(self) -> None: ...

class LaundrifyEnergySensor(CoordinatorEntity[LaundrifyUpdateCoordinator], LaundrifyBaseSensor):
    _attr_device_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_state_class: Incomplete
    _attr_suggested_unit_of_measurement: Incomplete
    _attr_suggested_display_precision: int
    def __init__(self, coordinator: LaundrifyUpdateCoordinator, device: LaundrifyDevice) -> None: ...
    @property
    def native_value(self) -> float: ...
