from .coordinator import ShellyConfigEntry as ShellyConfigEntry, ShellyRpcCoordinator as ShellyRpcCoordinator
from .entity import RpcEntityDescription as RpcEntityDescription, ShellyRpcAttributeEntity as ShellyRpcAttributeEntity, async_setup_entry_rpc as async_setup_entry_rpc
from .utils import async_remove_orphaned_entities as async_remove_orphaned_entities, get_device_entry_gen as get_device_entry_gen, get_virtual_component_ids as get_virtual_component_ids
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Final

@dataclass(frozen=True, kw_only=True)
class RpcSelectDescription(RpcEntityDescription, SelectEntityDescription): ...

RPC_SELECT_ENTITIES: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RpcSelect(ShellyRpcAttributeEntity, SelectEntity):
    entity_description: RpcSelectDescription
    _attr_options: Incomplete
    def __init__(self, coordinator: ShellyRpcCoordinator, key: str, attribute: str, description: RpcSelectDescription) -> None: ...
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...
