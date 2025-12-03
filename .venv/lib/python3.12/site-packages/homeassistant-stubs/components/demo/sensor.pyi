from . import DOMAIN as DOMAIN
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.sensor import RestoreSensor as RestoreSensor, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_BATTERY_LEVEL as ATTR_BATTERY_LEVEL, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, PERCENTAGE as PERCENTAGE, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower, UnitOfTemperature as UnitOfTemperature, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DemoSensor(SensorEntity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_should_poll: bool
    _attr_device_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_native_value: Incomplete
    _attr_state_class: Incomplete
    _attr_unique_id: Incomplete
    _attr_options: Incomplete
    _attr_translation_key: Incomplete
    _attr_device_info: Incomplete
    _attr_extra_state_attributes: Incomplete
    def __init__(self, unique_id: str, device_name: str | None, state: float | str | None, device_class: SensorDeviceClass, state_class: SensorStateClass | None, unit_of_measurement: str | None, battery: int | None, options: list[str] | None = None, translation_key: str | None = None) -> None: ...

class DemoSumSensor(RestoreSensor):
    _attr_should_poll: bool
    _attr_native_value: float
    entity_id: Incomplete
    _attr_device_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_state_class: Incomplete
    _attr_unique_id: Incomplete
    _five_minute_increase: Incomplete
    _attr_device_info: Incomplete
    _attr_extra_state_attributes: Incomplete
    def __init__(self, unique_id: str, device_name: str, five_minute_increase: float, device_class: SensorDeviceClass, state_class: SensorStateClass | None, unit_of_measurement: str | None, battery: int | None, suggested_entity_id: str) -> None: ...
    @callback
    def _async_bump_sum(self, now: datetime) -> None: ...
    async def async_added_to_hass(self) -> None: ...
