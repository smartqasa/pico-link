from .const import CONF_GATEWAY_ID as CONF_GATEWAY_ID, COORDINATOR as COORDINATOR, COORDINATOR_LIST as COORDINATOR_LIST, DOMAIN as DOMAIN, KEY_API as KEY_API, LOGGER as LOGGER
from .coordinator import TradfriDeviceDataUpdateCoordinator as TradfriDeviceDataUpdateCoordinator
from .entity import TradfriBaseEntity as TradfriBaseEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, PERCENTAGE as PERCENTAGE, Platform as Platform, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pytradfri.command import Command as Command
from pytradfri.device import Device as Device
from typing import Any

@dataclass(frozen=True, kw_only=True)
class TradfriSensorEntityDescription(SensorEntityDescription):
    value: Callable[[Device], Any | None]

def _get_air_quality(device: Device) -> int | None: ...
def _get_filter_time_left(device: Device) -> int: ...

SENSOR_DESCRIPTIONS_BATTERY: tuple[TradfriSensorEntityDescription, ...]
SENSOR_DESCRIPTIONS_FAN: tuple[TradfriSensorEntityDescription, ...]

@callback
def _migrate_old_unique_ids(hass: HomeAssistant, old_unique_id: str, key: str) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TradfriSensor(TradfriBaseEntity, SensorEntity):
    entity_description: TradfriSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, device_coordinator: TradfriDeviceDataUpdateCoordinator, api: Callable[[Command | list[Command]], Any], gateway_id: str, description: TradfriSensorEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    def _refresh(self) -> None: ...
