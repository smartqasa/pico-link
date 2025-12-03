from .const import BASIC_INPUTS_EVENTS_TYPES as BASIC_INPUTS_EVENTS_TYPES, RPC_INPUTS_EVENTS_TYPES as RPC_INPUTS_EVENTS_TYPES, SHIX3_1_INPUTS_EVENTS_TYPES as SHIX3_1_INPUTS_EVENTS_TYPES
from .coordinator import ShellyBlockCoordinator as ShellyBlockCoordinator, ShellyConfigEntry as ShellyConfigEntry, ShellyRpcCoordinator as ShellyRpcCoordinator
from .entity import ShellyBlockEntity as ShellyBlockEntity
from .utils import async_remove_shelly_entity as async_remove_shelly_entity, get_device_entry_gen as get_device_entry_gen, get_rpc_entity_name as get_rpc_entity_name, get_rpc_key_instances as get_rpc_key_instances, is_block_momentary_input as is_block_momentary_input, is_rpc_momentary_input as is_rpc_momentary_input
from _typeshed import Incomplete
from aioshelly.block_device import Block as Block
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.event import EventDeviceClass as EventDeviceClass, EventEntity as EventEntity, EventEntityDescription as EventEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any, Final

@dataclass(frozen=True, kw_only=True)
class ShellyBlockEventDescription(EventEntityDescription):
    removal_condition: Callable[[dict, Block], bool] | None = ...

@dataclass(frozen=True, kw_only=True)
class ShellyRpcEventDescription(EventEntityDescription):
    removal_condition: Callable[[dict, dict, str], bool] | None = ...

BLOCK_EVENT: Final[Incomplete]
RPC_EVENT: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ShellyBlockEvent(ShellyBlockEntity, EventEntity):
    entity_description: ShellyBlockEventDescription
    channel: Incomplete
    _attr_unique_id: Incomplete
    _attr_event_types: Incomplete
    def __init__(self, coordinator: ShellyBlockCoordinator, block: Block, description: ShellyBlockEventDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _async_handle_event(self, event: dict[str, Any]) -> None: ...

class ShellyRpcEvent(CoordinatorEntity[ShellyRpcCoordinator], EventEntity):
    entity_description: ShellyRpcEventDescription
    input_index: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    def __init__(self, coordinator: ShellyRpcCoordinator, key: str, description: ShellyRpcEventDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _async_handle_event(self, event: dict[str, Any]) -> None: ...
