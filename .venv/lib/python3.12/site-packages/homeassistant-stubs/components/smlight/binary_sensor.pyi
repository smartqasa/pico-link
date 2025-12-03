from .const import SCAN_INTERNET_INTERVAL as SCAN_INTERNET_INTERVAL
from .coordinator import SmDataUpdateCoordinator as SmDataUpdateCoordinator
from .entity import SmEntity as SmEntity
from _collections_abc import Callable as Callable
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pysmlight import Sensors as Sensors
from pysmlight.sse import MessageEvent as MessageEvent

SCAN_INTERVAL = SCAN_INTERNET_INTERVAL

@dataclass(frozen=True, kw_only=True)
class SmBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[Sensors], bool]

SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SmBinarySensorEntity(SmEntity, BinarySensorEntity):
    entity_description: SmBinarySensorEntityDescription
    _attr_device_class: Incomplete
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SmDataUpdateCoordinator, description: SmBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...

class SmInternetSensorEntity(SmEntity, BinarySensorEntity):
    _attr_translation_key: str
    _attr_device_class: Incomplete
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SmDataUpdateCoordinator) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_is_on: Incomplete
    @callback
    def internet_callback(self, event: MessageEvent) -> None: ...
    @property
    def should_poll(self) -> bool: ...
    async def async_update(self) -> None: ...
