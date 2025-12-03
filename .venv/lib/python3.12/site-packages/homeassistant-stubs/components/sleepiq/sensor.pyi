from .const import DOMAIN as DOMAIN, PRESSURE as PRESSURE, SLEEP_NUMBER as SLEEP_NUMBER
from .coordinator import SleepIQData as SleepIQData, SleepIQDataUpdateCoordinator as SleepIQDataUpdateCoordinator
from .entity import SleepIQSleeperEntity as SleepIQSleeperEntity
from _typeshed import Incomplete
from asyncsleepiq import SleepIQBed as SleepIQBed, SleepIQSleeper as SleepIQSleeper
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SleepIQSensorEntity(SleepIQSleeperEntity[SleepIQDataUpdateCoordinator], SensorEntity):
    _attr_icon: str
    sensor_type: Incomplete
    _attr_state_class: Incomplete
    def __init__(self, coordinator: SleepIQDataUpdateCoordinator, bed: SleepIQBed, sleeper: SleepIQSleeper, sensor_type: str) -> None: ...
    _attr_native_value: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...
