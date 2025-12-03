from . import DevoloHomeControlConfigEntry as DevoloHomeControlConfigEntry
from .entity import DevoloDeviceEntity as DevoloDeviceEntity
from _typeshed import Incomplete
from devolo_home_control_api.devices.zwave import Zwave as Zwave
from devolo_home_control_api.homecontrol import HomeControl as HomeControl
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

DEVICE_CLASS_MAPPING: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: DevoloHomeControlConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DevoloBinaryDeviceEntity(DevoloDeviceEntity, BinarySensorEntity):
    _binary_sensor_property: Incomplete
    _attr_device_class: Incomplete
    _attr_translation_key: str
    _value: Incomplete
    _attr_entity_category: Incomplete
    _attr_entity_registry_enabled_default: bool
    def __init__(self, homecontrol: HomeControl, device_instance: Zwave, element_uid: str) -> None: ...
    @property
    def is_on(self) -> bool: ...

class DevoloRemoteControl(DevoloDeviceEntity, BinarySensorEntity):
    _remote_control_property: Incomplete
    _key: Incomplete
    _attr_is_on: bool
    _attr_translation_key: str
    _attr_translation_placeholders: Incomplete
    def __init__(self, homecontrol: HomeControl, device_instance: Zwave, element_uid: str, key: int) -> None: ...
    def _sync(self, message: tuple) -> None: ...
