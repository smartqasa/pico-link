from .const import CONF_TIME_FORMAT as CONF_TIME_FORMAT, DEFAULT_NAME as DEFAULT_NAME, DEFAULT_TIME_STR_FORMAT as DEFAULT_TIME_STR_FORMAT, DOMAIN as DOMAIN
from _typeshed import Incomplete
from datetime import tzinfo
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_TIME_ZONE as CONF_TIME_ZONE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType

PLATFORM_SCHEMA: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WorldClockSensor(SensorEntity):
    _attr_icon: str
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _time_zone: Incomplete
    _time_format: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, time_zone: tzinfo | None, name: str, time_format: str, unique_id: str) -> None: ...
    _attr_native_value: Incomplete
    async def async_update(self) -> None: ...
