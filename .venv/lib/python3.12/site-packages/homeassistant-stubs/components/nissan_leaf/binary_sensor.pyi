from . import LeafDataStore as LeafDataStore
from .const import DATA_CHARGING as DATA_CHARGING, DATA_LEAF as DATA_LEAF, DATA_PLUGGED_IN as DATA_PLUGGED_IN
from .entity import LeafEntity as LeafEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType

_LOGGER: Incomplete

def setup_platform(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class LeafPluggedInSensor(LeafEntity, BinarySensorEntity):
    _attr_device_class: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, car: LeafDataStore) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def available(self) -> bool: ...
    @property
    def is_on(self) -> bool: ...

class LeafChargingSensor(LeafEntity, BinarySensorEntity):
    _attr_device_class: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, car: LeafDataStore) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def available(self) -> bool: ...
    @property
    def is_on(self) -> bool: ...
