import abc
from .const import DOMAIN as DOMAIN
from .coordinator import SurePetcareDataCoordinator as SurePetcareDataCoordinator
from .entity import SurePetcareEntity as SurePetcareEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from surepy.entities import SurepyEntity as SurepyEntity

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SurePetcareBinarySensor(SurePetcareEntity, BinarySensorEntity, metaclass=abc.ABCMeta):
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, surepetcare_id: int, coordinator: SurePetcareDataCoordinator) -> None: ...

class Hub(SurePetcareBinarySensor):
    _attr_device_class: Incomplete
    _attr_entity_category: Incomplete
    @property
    def available(self) -> bool: ...
    _attr_is_on: Incomplete
    _attr_extra_state_attributes: Incomplete
    @callback
    def _update_attr(self, surepy_entity: SurepyEntity) -> None: ...

class Pet(SurePetcareBinarySensor):
    _attr_device_class: Incomplete
    _attr_is_on: Incomplete
    _attr_extra_state_attributes: Incomplete
    @callback
    def _update_attr(self, surepy_entity: SurepyEntity) -> None: ...

class DeviceConnectivity(SurePetcareBinarySensor):
    _attr_device_class: Incomplete
    _attr_entity_category: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, surepetcare_id: int, coordinator: SurePetcareDataCoordinator) -> None: ...
    _attr_is_on: Incomplete
    _attr_extra_state_attributes: Incomplete
    @callback
    def _update_attr(self, surepy_entity: SurepyEntity) -> None: ...
