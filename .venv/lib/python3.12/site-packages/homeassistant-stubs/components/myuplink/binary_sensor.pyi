from . import MyUplinkConfigEntry as MyUplinkConfigEntry, MyUplinkDataCoordinator as MyUplinkDataCoordinator
from .const import F_SERIES as F_SERIES
from .entity import MyUplinkEntity as MyUplinkEntity, MyUplinkSystemEntity as MyUplinkSystemEntity
from .helpers import find_matching_platform as find_matching_platform, transform_model_series as transform_model_series
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from myuplink import DevicePoint as DevicePoint

CATEGORY_BASED_DESCRIPTIONS: dict[str, dict[str, BinarySensorEntityDescription]]
CONNECTED_BINARY_SENSOR_DESCRIPTION: Incomplete
ALARM_BINARY_SENSOR_DESCRIPTION: Incomplete

def get_description(device_point: DevicePoint) -> BinarySensorEntityDescription | None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: MyUplinkConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MyUplinkDevicePointBinarySensor(MyUplinkEntity, BinarySensorEntity):
    point_id: Incomplete
    _attr_name: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: MyUplinkDataCoordinator, device_id: str, device_point: DevicePoint, entity_description: BinarySensorEntityDescription | None, unique_id_suffix: str) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def available(self) -> bool: ...

class MyUplinkDeviceBinarySensor(MyUplinkEntity, BinarySensorEntity):
    entity_description: Incomplete
    def __init__(self, coordinator: MyUplinkDataCoordinator, device_id: str, entity_description: BinarySensorEntityDescription, unique_id_suffix: str) -> None: ...
    @property
    def is_on(self) -> bool: ...

class MyUplinkSystemBinarySensor(MyUplinkSystemEntity, BinarySensorEntity):
    entity_description: Incomplete
    def __init__(self, coordinator: MyUplinkDataCoordinator, system_id: str, device_id: str, entity_description: BinarySensorEntityDescription, unique_id_suffix: str) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
