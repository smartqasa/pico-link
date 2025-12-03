import dataclasses
import logging
from .const import DOMAIN as DOMAIN
from .models import BluetoothChange as BluetoothChange, BluetoothServiceInfoBleak as BluetoothServiceInfoBleak
from .update_coordinator import BasePassiveBluetoothCoordinator as BasePassiveBluetoothCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from habluetooth import BluetoothScanningMode as BluetoothScanningMode
from homeassistant import config_entries as config_entries
from homeassistant.const import ATTR_CONNECTIONS as ATTR_CONNECTIONS, ATTR_IDENTIFIERS as ATTR_IDENTIFIERS, ATTR_NAME as ATTR_NAME, CONF_ENTITY_CATEGORY as CONF_ENTITY_CATEGORY, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, EntityCategory as EntityCategory
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import CONNECTION_BLUETOOTH as CONNECTION_BLUETOOTH, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback, async_get_current_platform as async_get_current_platform
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.typing import UNDEFINED as UNDEFINED
from homeassistant.util.enum import try_parse_enum as try_parse_enum
from typing import Any, Self, TypedDict

STORAGE_KEY: str
STORAGE_VERSION: int
STORAGE_SAVE_INTERVAL: Incomplete
PASSIVE_UPDATE_PROCESSOR: str

@dataclasses.dataclass(slots=True, frozen=True)
class PassiveBluetoothEntityKey:
    key: str
    device_id: str | None
    def to_string(self) -> str: ...
    @classmethod
    def from_string(cls, key: str) -> PassiveBluetoothEntityKey: ...

@dataclasses.dataclass(slots=True, frozen=False)
class PassiveBluetoothProcessorData:
    coordinators: set[PassiveBluetoothProcessorCoordinator[Any]]
    all_restore_data: dict[str, dict[str, RestoredPassiveBluetoothDataUpdate]]

class RestoredPassiveBluetoothDataUpdate(TypedDict):
    devices: dict[str, DeviceInfo]
    entity_descriptions: dict[str, dict[str, Any]]
    entity_names: dict[str, str | None]
    entity_data: dict[str, Any]

cached_fields: Incomplete

def deserialize_entity_description(descriptions_class: type[EntityDescription], data: dict[str, Any]) -> EntityDescription: ...
def serialize_entity_description(description: EntityDescription) -> dict[str, Any]: ...

@dataclasses.dataclass(slots=True, frozen=False)
class PassiveBluetoothDataUpdate[_T]:
    devices: dict[str | None, DeviceInfo] = dataclasses.field(default_factory=dict)
    entity_descriptions: dict[PassiveBluetoothEntityKey, EntityDescription] = dataclasses.field(default_factory=dict)
    entity_names: dict[PassiveBluetoothEntityKey, str | None] = dataclasses.field(default_factory=dict)
    entity_data: dict[PassiveBluetoothEntityKey, _T] = dataclasses.field(default_factory=dict)
    def update(self, new_data: PassiveBluetoothDataUpdate[_T]) -> set[PassiveBluetoothEntityKey] | None: ...
    def async_get_restore_data(self) -> RestoredPassiveBluetoothDataUpdate: ...
    @callback
    def async_set_restore_data(self, restore_data: RestoredPassiveBluetoothDataUpdate, entity_description_class: type[EntityDescription]) -> None: ...

def async_register_coordinator_for_restore(hass: HomeAssistant, coordinator: PassiveBluetoothProcessorCoordinator[Any]) -> CALLBACK_TYPE: ...
async def async_setup(hass: HomeAssistant) -> None: ...

class PassiveBluetoothProcessorCoordinator[_DataT](BasePassiveBluetoothCoordinator):
    _processors: list[PassiveBluetoothDataProcessor[Any, _DataT]]
    _update_method: Incomplete
    last_update_success: bool
    restore_data: dict[str, RestoredPassiveBluetoothDataUpdate]
    restore_key: Incomplete
    def __init__(self, hass: HomeAssistant, logger: logging.Logger, address: str, mode: BluetoothScanningMode, update_method: Callable[[BluetoothServiceInfoBleak], _DataT], connectable: bool = False) -> None: ...
    @property
    def available(self) -> bool: ...
    @callback
    def async_get_restore_data(self) -> dict[str, RestoredPassiveBluetoothDataUpdate]: ...
    @callback
    def async_register_processor(self, processor: PassiveBluetoothDataProcessor[Any, _DataT], entity_description_class: type[EntityDescription] | None = None) -> Callable[[], None]: ...
    @callback
    def _async_handle_unavailable(self, service_info: BluetoothServiceInfoBleak) -> None: ...
    _available: bool
    @callback
    def _async_handle_bluetooth_event(self, service_info: BluetoothServiceInfoBleak, change: BluetoothChange) -> None: ...

class PassiveBluetoothDataProcessor[_T, _DataT]:
    coordinator: PassiveBluetoothProcessorCoordinator[_DataT]
    data: PassiveBluetoothDataUpdate[_T]
    entity_names: dict[PassiveBluetoothEntityKey, str | None]
    entity_data: dict[PassiveBluetoothEntityKey, _T]
    entity_descriptions: dict[PassiveBluetoothEntityKey, EntityDescription]
    devices: dict[str | None, DeviceInfo]
    restore_key: str | None
    _listeners: list[Callable[[PassiveBluetoothDataUpdate[_T] | None], None]]
    _entity_key_listeners: dict[PassiveBluetoothEntityKey, list[Callable[[PassiveBluetoothDataUpdate[_T] | None], None]]]
    update_method: Incomplete
    last_update_success: bool
    def __init__(self, update_method: Callable[[_DataT], PassiveBluetoothDataUpdate[_T]], restore_key: str | None = None) -> None: ...
    @callback
    def async_register_coordinator(self, coordinator: PassiveBluetoothProcessorCoordinator[_DataT], entity_description_class: type[EntityDescription] | None) -> None: ...
    @property
    def available(self) -> bool: ...
    @callback
    def async_handle_unavailable(self) -> None: ...
    @callback
    def async_add_entities_listener(self, entity_class: type[PassiveBluetoothProcessorEntity[Self]], async_add_entities: AddEntitiesCallback) -> Callable[[], None]: ...
    @callback
    def async_add_listener(self, update_callback: Callable[[PassiveBluetoothDataUpdate[_T] | None], None]) -> Callable[[], None]: ...
    @callback
    def async_add_entity_key_listener(self, update_callback: Callable[[PassiveBluetoothDataUpdate[_T] | None], None], entity_key: PassiveBluetoothEntityKey) -> Callable[[], None]: ...
    @callback
    def async_update_listeners(self, data: PassiveBluetoothDataUpdate[_T] | None, was_available: bool | None = None, changed_entity_keys: set[PassiveBluetoothEntityKey] | None = None) -> None: ...
    @callback
    def async_handle_update(self, update: _DataT, was_available: bool | None = None) -> None: ...

class PassiveBluetoothProcessorEntity[_PassiveBluetoothDataProcessorT: PassiveBluetoothDataProcessor[Any, Any]](Entity):
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    entity_description: Incomplete
    entity_key: Incomplete
    processor: Incomplete
    processor_context: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    def __init__(self, processor: _PassiveBluetoothDataProcessorT, entity_key: PassiveBluetoothEntityKey, description: EntityDescription, context: Any = None) -> None: ...
    @property
    def available(self) -> bool: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _handle_processor_update(self, new_data: PassiveBluetoothDataUpdate[_PassiveBluetoothDataProcessorT] | None) -> None: ...
