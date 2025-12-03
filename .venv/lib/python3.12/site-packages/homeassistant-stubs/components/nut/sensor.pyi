from . import NutConfigEntry as NutConfigEntry, PyNUTData as PyNUTData
from .const import DOMAIN as DOMAIN, KEY_STATUS as KEY_STATUS, KEY_STATUS_DISPLAY as KEY_STATUS_DISPLAY, STATE_TYPES as STATE_TYPES
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import ATTR_MANUFACTURER as ATTR_MANUFACTURER, ATTR_MODEL as ATTR_MODEL, ATTR_SERIAL_NUMBER as ATTR_SERIAL_NUMBER, ATTR_SW_VERSION as ATTR_SW_VERSION, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, STATE_UNKNOWN as STATE_UNKNOWN, UnitOfApparentPower as UnitOfApparentPower, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfFrequency as UnitOfFrequency, UnitOfPower as UnitOfPower, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Final

NUT_DEV_INFO_TO_DEV_INFO: dict[str, str]
_LOGGER: Incomplete
SENSOR_TYPES: Final[dict[str, SensorEntityDescription]]

def _get_nut_device_info(data: PyNUTData) -> DeviceInfo: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: NutConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NUTSensor(CoordinatorEntity[DataUpdateCoordinator[dict[str, str]]], SensorEntity):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator[dict[str, str]], sensor_description: SensorEntityDescription, data: PyNUTData, unique_id: str) -> None: ...
    @property
    def native_value(self) -> str | None: ...

def _format_display_state(status: dict[str, str]) -> str: ...
