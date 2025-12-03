from . import IslamicPrayerTimesConfigEntry as IslamicPrayerTimesConfigEntry
from .const import DOMAIN as DOMAIN, NAME as NAME
from .coordinator import IslamicPrayerDataUpdateCoordinator as IslamicPrayerDataUpdateCoordinator
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

SENSOR_TYPES: tuple[SensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: IslamicPrayerTimesConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class IslamicPrayerTimeSensor(CoordinatorEntity[IslamicPrayerDataUpdateCoordinator], SensorEntity):
    _attr_device_class: Incomplete
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: IslamicPrayerDataUpdateCoordinator, description: SensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> datetime: ...
