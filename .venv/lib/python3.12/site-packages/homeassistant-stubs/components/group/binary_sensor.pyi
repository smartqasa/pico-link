from .entity import GroupEntity as GroupEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, DEVICE_CLASSES_SCHEMA as DEVICE_CLASSES_SCHEMA
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_ENTITIES as CONF_ENTITIES, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, STATE_ON as STATE_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

DEFAULT_NAME: str
CONF_ALL: str
REG_KEY: Incomplete
PLATFORM_SCHEMA: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
@callback
def async_create_preview_binary_sensor(hass: HomeAssistant, name: str, validated_config: dict[str, Any]) -> BinarySensorGroup: ...

class BinarySensorGroup(GroupEntity, BinarySensorEntity):
    _attr_available: bool
    _entity_ids: Incomplete
    _attr_name: Incomplete
    _attr_extra_state_attributes: Incomplete
    _attr_unique_id: Incomplete
    _device_class: Incomplete
    mode: Incomplete
    def __init__(self, unique_id: str | None, name: str, device_class: BinarySensorDeviceClass | None, entity_ids: list[str], mode: bool | None) -> None: ...
    _attr_is_on: Incomplete
    @callback
    def async_update_group_state(self) -> None: ...
    @property
    def device_class(self) -> BinarySensorDeviceClass | None: ...
