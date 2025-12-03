from .client import CloudClient as CloudClient
from .const import DATA_CLOUD as DATA_CLOUD, DISPATCHER_REMOTE_UPDATE as DISPATCHER_REMOTE_UPDATE
from _typeshed import Incomplete
from hass_nabucasa import Cloud as Cloud
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

WAIT_UNTIL_CHANGE: int

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class CloudRemoteBinary(BinarySensorEntity):
    _attr_name: str
    _attr_device_class: Incomplete
    _attr_should_poll: bool
    _attr_unique_id: str
    _attr_entity_category: Incomplete
    cloud: Incomplete
    def __init__(self, cloud: Cloud[CloudClient]) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def available(self) -> bool: ...
    async def async_added_to_hass(self) -> None: ...
