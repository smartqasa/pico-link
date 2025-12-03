from .api import PushBulletNotificationProvider as PushBulletNotificationProvider
from .const import DATA_UPDATED as DATA_UPDATED, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

SENSOR_TYPES: tuple[SensorEntityDescription, ...]
SENSOR_KEYS: list[str]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PushBulletNotificationSensor(SensorEntity):
    _attr_should_poll: bool
    _attr_has_entity_name: bool
    entity_description: Incomplete
    pb_provider: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, name: str, pb_provider: PushBulletNotificationProvider, description: SensorEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    _attr_extra_state_attributes: Incomplete
    @callback
    def async_update_callback(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
