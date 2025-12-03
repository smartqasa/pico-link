from . import DevoloHomeControlConfigEntry as DevoloHomeControlConfigEntry
from .entity import DevoloDeviceEntity as DevoloDeviceEntity
from _typeshed import Incomplete
from devolo_home_control_api.devices.zwave import Zwave as Zwave
from devolo_home_control_api.homecontrol import HomeControl as HomeControl
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

DEVICE_CLASS_MAPPING: Incomplete
STATE_CLASS_MAPPING: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: DevoloHomeControlConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DevoloMultiLevelDeviceEntity(DevoloDeviceEntity, SensorEntity):
    @property
    def native_value(self) -> float: ...

class DevoloGenericMultiLevelDeviceEntity(DevoloMultiLevelDeviceEntity):
    _multi_level_sensor_property: Incomplete
    _attr_device_class: Incomplete
    _attr_state_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _value: Incomplete
    _attr_translation_key: str
    _attr_entity_registry_enabled_default: bool
    def __init__(self, homecontrol: HomeControl, device_instance: Zwave, element_uid: str) -> None: ...

class DevoloBatteryEntity(DevoloMultiLevelDeviceEntity):
    _attr_entity_category: Incomplete
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_device_class: Incomplete
    _attr_state_class: Incomplete
    _value: Incomplete
    def __init__(self, homecontrol: HomeControl, device_instance: Zwave, element_uid: str) -> None: ...

class DevoloConsumptionEntity(DevoloMultiLevelDeviceEntity):
    _sensor_type: Incomplete
    _attr_device_class: Incomplete
    _attr_state_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _value: Incomplete
    def __init__(self, homecontrol: HomeControl, device_instance: Zwave, element_uid: str, consumption: str) -> None: ...
    @property
    def unique_id(self) -> str: ...
    def _sync(self, message: tuple) -> None: ...
