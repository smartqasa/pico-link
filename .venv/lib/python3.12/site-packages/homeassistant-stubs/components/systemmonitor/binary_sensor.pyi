from . import SystemMonitorConfigEntry as SystemMonitorConfigEntry
from .const import CONF_PROCESS as CONF_PROCESS, DOMAIN as DOMAIN
from .coordinator import SystemMonitorCoordinator as SystemMonitorCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from functools import lru_cache
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from homeassistant.util import slugify as slugify
from typing import Literal

_LOGGER: Incomplete
CONF_ARG: str
SENSOR_TYPE_NAME: int
SENSOR_TYPE_UOM: int
SENSOR_TYPE_ICON: int
SENSOR_TYPE_DEVICE_CLASS: int
SENSOR_TYPE_MANDATORY_ARG: int
SIGNAL_SYSTEMMONITOR_UPDATE: str

@lru_cache
def get_cpu_icon() -> Literal['mdi:cpu-64-bit', 'mdi:cpu-32-bit']: ...
def get_process(entity: SystemMonitorSensor) -> bool: ...

@dataclass(frozen=True, kw_only=True)
class SysMonitorBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[SystemMonitorSensor], bool]
    add_to_update: Callable[[SystemMonitorSensor], tuple[str, str]]

SENSOR_TYPES: tuple[SysMonitorBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: SystemMonitorConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SystemMonitorSensor(CoordinatorEntity[SystemMonitorCoordinator], BinarySensorEntity):
    _attr_has_entity_name: bool
    _attr_entity_category: Incomplete
    entity_description: SysMonitorBinarySensorEntityDescription
    _attr_translation_placeholders: Incomplete
    _attr_unique_id: str
    _attr_device_info: Incomplete
    argument: Incomplete
    def __init__(self, coordinator: SystemMonitorCoordinator, sensor_description: SysMonitorBinarySensorEntityDescription, entry_id: str, argument: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
