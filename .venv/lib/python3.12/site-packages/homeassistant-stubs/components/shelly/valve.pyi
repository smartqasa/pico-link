from .coordinator import ShellyBlockCoordinator as ShellyBlockCoordinator, ShellyConfigEntry as ShellyConfigEntry
from .entity import BlockEntityDescription as BlockEntityDescription, ShellyBlockAttributeEntity as ShellyBlockAttributeEntity, async_setup_block_attribute_entities as async_setup_block_attribute_entities
from .utils import async_remove_shelly_entity as async_remove_shelly_entity, get_device_entry_gen as get_device_entry_gen
from _typeshed import Incomplete
from aioshelly.block_device import Block as Block
from dataclasses import dataclass
from homeassistant.components.valve import ValveDeviceClass as ValveDeviceClass, ValveEntity as ValveEntity, ValveEntityDescription as ValveEntityDescription, ValveEntityFeature as ValveEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

@dataclass(kw_only=True, frozen=True)
class BlockValveDescription(BlockEntityDescription, ValveEntityDescription): ...

GAS_VALVE: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
@callback
def async_setup_block_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BlockShellyValve(ShellyBlockAttributeEntity, ValveEntity):
    entity_description: BlockValveDescription
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    control_result: dict[str, Any] | None
    _attr_is_closed: Incomplete
    def __init__(self, coordinator: ShellyBlockCoordinator, block: Block, attribute: str, description: BlockValveDescription) -> None: ...
    @property
    def is_closing(self) -> bool: ...
    @property
    def is_opening(self) -> bool: ...
    async def async_open_valve(self, **kwargs: Any) -> None: ...
    async def async_close_valve(self, **kwargs: Any) -> None: ...
    @callback
    def _update_callback(self) -> None: ...
