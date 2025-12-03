from .const import DOMAIN as DOMAIN, UOM_INDEX as UOM_INDEX, _LOGGER as _LOGGER
from .entity import ISYAuxControlEntity as ISYAuxControlEntity
from .models import IsyData as IsyData
from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, Platform as Platform, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from pyisy.helpers import EventListener as EventListener, NodeProperty as NodeProperty
from pyisy.nodes import Node as Node, NodeChangedEvent as NodeChangedEvent

def time_string(i: int) -> str: ...

RAMP_RATE_OPTIONS: Incomplete
BACKLIGHT_MEMORY_FILTER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ISYRampRateSelectEntity(ISYAuxControlEntity, SelectEntity):
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...

class ISYAuxControlIndexSelectEntity(ISYAuxControlEntity, SelectEntity):
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...

class ISYBacklightSelectEntity(ISYAuxControlEntity, SelectEntity, RestoreEntity):
    _assumed_state: bool
    _memory_change_handler: EventListener | None
    _attr_current_option: Incomplete
    def __init__(self, node: Node, control: str, unique_id: str, description: SelectEntityDescription, device_info: DeviceInfo | None) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def async_on_memory_write(self, event: NodeChangedEvent, key: str) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
