from .const import READ_MODE_BOOL as READ_MODE_BOOL, READ_MODE_INT as READ_MODE_INT
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.typing import StateType as StateType
from pyownet import protocol
from typing import Any

@dataclass(frozen=True)
class OneWireEntityDescription(EntityDescription):
    read_mode: str | None = ...

_LOGGER: Incomplete

class OneWireEntity(Entity):
    entity_description: OneWireEntityDescription
    _attr_has_entity_name: bool
    _last_update_success: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _device_file: Incomplete
    _state: StateType
    _value_raw: float | None
    _owproxy: Incomplete
    def __init__(self, description: OneWireEntityDescription, device_id: str, device_info: DeviceInfo, device_file: str, owproxy: protocol._Proxy) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...
    def _read_value(self) -> str: ...
    def _write_value(self, value: bytes) -> None: ...
    def update(self) -> None: ...
