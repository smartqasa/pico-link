from . import PlugwiseConfigEntry as PlugwiseConfigEntry
from .const import GATEWAY_ID as GATEWAY_ID, REBOOT as REBOOT
from .coordinator import PlugwiseDataUpdateCoordinator as PlugwiseDataUpdateCoordinator
from .entity import PlugwiseEntity as PlugwiseEntity
from .util import plugwise_command as plugwise_command
from _typeshed import Incomplete
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: PlugwiseConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PlugwiseButtonEntity(PlugwiseEntity, ButtonEntity):
    _attr_device_class: Incomplete
    _attr_entity_category: Incomplete
    _attr_translation_key: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PlugwiseDataUpdateCoordinator, device_id: str) -> None: ...
    @plugwise_command
    async def async_press(self) -> None: ...
