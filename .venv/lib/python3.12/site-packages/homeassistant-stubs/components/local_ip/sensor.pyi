from .const import SENSOR as SENSOR
from _typeshed import Incomplete
from homeassistant.components.network import async_get_source_ip as async_get_source_ip
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class IPSensor(SensorEntity):
    _attr_unique_id = SENSOR
    _attr_translation_key: str
    _attr_name: Incomplete
    def __init__(self, name: str) -> None: ...
    _attr_native_value: Incomplete
    async def async_update(self) -> None: ...
