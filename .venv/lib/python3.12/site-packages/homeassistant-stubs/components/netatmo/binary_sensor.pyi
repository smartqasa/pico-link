from .const import NETATMO_CREATE_WEATHER_SENSOR as NETATMO_CREATE_WEATHER_SENSOR
from .data_handler import NetatmoDevice as NetatmoDevice
from .entity import NetatmoWeatherModuleEntity as NetatmoWeatherModuleEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

BINARY_SENSOR_TYPES: tuple[BinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NetatmoWeatherBinarySensor(NetatmoWeatherModuleEntity, BinarySensorEntity):
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, device: NetatmoDevice, description: BinarySensorEntityDescription) -> None: ...
    _attr_is_on: Incomplete
    @callback
    def async_update_callback(self) -> None: ...
