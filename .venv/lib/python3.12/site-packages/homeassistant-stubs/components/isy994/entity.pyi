from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.const import STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from pyisy.helpers import EventListener as EventListener, NodeProperty as NodeProperty
from pyisy.nodes import Group as Group, Node as Node, NodeChangedEvent as NodeChangedEvent
from pyisy.programs import Program as Program
from pyisy.variables import Variable as Variable
from typing import Any

class ISYEntity(Entity):
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _node: Node | Program | Variable
    _attr_name: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    _attrs: dict[str, Any]
    _change_handler: EventListener | None
    _control_handler: EventListener | None
    def __init__(self, node: Node | Group | Variable | Program, device_info: DeviceInfo | None = None) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def async_on_update(self, event: NodeProperty) -> None: ...
    @callback
    def async_on_control(self, event: NodeProperty) -> None: ...

class ISYNodeEntity(ISYEntity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    def __init__(self, node: Node | Group | Variable | Program, device_info: DeviceInfo | None = None) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> dict: ...
    async def async_send_node_command(self, command: str) -> None: ...
    async def async_send_raw_node_command(self, command: str, value: Any | None = None, unit_of_measurement: str | None = None, parameters: Any | None = None) -> None: ...
    async def async_get_zwave_parameter(self, parameter: Any) -> None: ...
    async def async_set_zwave_parameter(self, parameter: Any, value: Any | None, size: int | None) -> None: ...
    async def async_rename_node(self, name: str) -> None: ...

class ISYProgramEntity(ISYEntity):
    _actions: Program
    _status: Program
    _attr_name: Incomplete
    def __init__(self, name: str, status: Program, actions: Program = None) -> None: ...
    @property
    def extra_state_attributes(self) -> dict: ...

class ISYAuxControlEntity(Entity):
    _attr_should_poll: bool
    _node: Incomplete
    _control: Incomplete
    _attr_name: Incomplete
    entity_description: Incomplete
    _attr_has_entity_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _change_handler: EventListener
    _availability_handler: EventListener
    def __init__(self, node: Node, control: str, unique_id: str, description: EntityDescription, device_info: DeviceInfo | None) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def async_on_update(self, event: NodeProperty | NodeChangedEvent, key: str) -> None: ...
    @property
    def available(self) -> bool: ...
