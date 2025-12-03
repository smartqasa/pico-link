import greeneye
from .const import CONF_CHANNELS as CONF_CHANNELS, CONF_COUNTED_QUANTITY as CONF_COUNTED_QUANTITY, CONF_COUNTED_QUANTITY_PER_PULSE as CONF_COUNTED_QUANTITY_PER_PULSE, CONF_MONITORS as CONF_MONITORS, CONF_NET_METERING as CONF_NET_METERING, CONF_NUMBER as CONF_NUMBER, CONF_PULSE_COUNTERS as CONF_PULSE_COUNTERS, CONF_SERIAL_NUMBER as CONF_SERIAL_NUMBER, CONF_TEMPERATURE_SENSORS as CONF_TEMPERATURE_SENSORS, CONF_TIME_UNIT as CONF_TIME_UNIT, CONF_VOLTAGE_SENSORS as CONF_VOLTAGE_SENSORS, DATA_GREENEYE_MONITOR as DATA_GREENEYE_MONITOR
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_SENSORS as CONF_SENSORS, CONF_TEMPERATURE_UNIT as CONF_TEMPERATURE_UNIT, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfPower as UnitOfPower, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

DATA_PULSES: str
DATA_WATT_SECONDS: str
COUNTER_ICON: str

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...
type UnderlyingSensorType = greeneye.monitor.Channel | greeneye.monitor.PulseCounter | greeneye.monitor.TemperatureSensor | greeneye.monitor.VoltageSensor

class GEMSensor(SensorEntity):
    _attr_should_poll: bool
    _monitor: Incomplete
    _monitor_serial_number: Incomplete
    _attr_name: Incomplete
    _sensor_type: Incomplete
    _sensor: UnderlyingSensorType
    _number: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, monitor: greeneye.monitor.Monitor, name: str, sensor_type: str, sensor: UnderlyingSensorType, number: int) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...

class CurrentSensor(GEMSensor):
    _attr_native_unit_of_measurement: Incomplete
    _attr_device_class: Incomplete
    _sensor: greeneye.monitor.Channel
    _net_metering: Incomplete
    def __init__(self, monitor: greeneye.monitor.Monitor, number: int, name: str, net_metering: bool) -> None: ...
    @property
    def native_value(self) -> float | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...

class PulseCounter(GEMSensor):
    _attr_icon = COUNTER_ICON
    _sensor: greeneye.monitor.PulseCounter
    _counted_quantity_per_pulse: Incomplete
    _time_unit: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    def __init__(self, monitor: greeneye.monitor.Monitor, number: int, name: str, counted_quantity: str, time_unit: str, counted_quantity_per_pulse: float) -> None: ...
    @property
    def native_value(self) -> float | None: ...
    @property
    def _seconds_per_time_unit(self) -> int: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...

class TemperatureSensor(GEMSensor):
    _attr_device_class: Incomplete
    _sensor: greeneye.monitor.TemperatureSensor
    _attr_native_unit_of_measurement: Incomplete
    def __init__(self, monitor: greeneye.monitor.Monitor, number: int, name: str, unit: str) -> None: ...
    @property
    def native_value(self) -> float | None: ...

class VoltageSensor(GEMSensor):
    _attr_native_unit_of_measurement: Incomplete
    _attr_device_class: Incomplete
    _sensor: greeneye.monitor.VoltageSensor
    def __init__(self, monitor: greeneye.monitor.Monitor, number: int, name: str) -> None: ...
    @property
    def native_value(self) -> float | None: ...
