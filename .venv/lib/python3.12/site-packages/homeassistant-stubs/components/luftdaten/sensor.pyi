from .const import ATTR_SENSOR_ID as ATTR_SENSOR_ID, CONF_SENSOR_ID as CONF_SENSOR_ID, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONF_SHOW_ON_MAP as CONF_SHOW_ON_MAP, PERCENTAGE as PERCENTAGE, UnitOfPressure as UnitOfPressure, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator

SENSORS: tuple[SensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SensorCommunitySensor(CoordinatorEntity, SensorEntity):
    _attr_attribution: str
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_extra_state_attributes: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, *, coordinator: DataUpdateCoordinator, description: SensorEntityDescription, sensor_id: int, show_on_map: bool) -> None: ...
    @property
    def native_value(self) -> float | None: ...
