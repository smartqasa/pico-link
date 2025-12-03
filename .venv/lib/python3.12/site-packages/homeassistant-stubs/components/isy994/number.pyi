from .const import CONF_VAR_SENSOR_STRING as CONF_VAR_SENSOR_STRING, DEFAULT_VAR_SENSOR_STRING as DEFAULT_VAR_SENSOR_STRING, DOMAIN as DOMAIN, UOM_8_BIT_RANGE as UOM_8_BIT_RANGE
from .entity import ISYAuxControlEntity as ISYAuxControlEntity
from .helpers import convert_isy_value_to_hass as convert_isy_value_to_hass
from .models import IsyData as IsyData
from _typeshed import Incomplete
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription, NumberMode as NumberMode, RestoreNumber as RestoreNumber
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_VARIABLES as CONF_VARIABLES, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, Platform as Platform, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.percentage import percentage_to_ranged_value as percentage_to_ranged_value, ranged_value_to_percentage as ranged_value_to_percentage
from pyisy.helpers import EventListener as EventListener, NodeProperty as NodeProperty
from pyisy.nodes import Node as Node, NodeChangedEvent as NodeChangedEvent
from pyisy.variables import Variable as Variable
from typing import Any

ISY_MAX_SIZE: Incomplete
ON_RANGE: Incomplete
CONTROL_DESC: Incomplete
BACKLIGHT_MEMORY_FILTER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ISYAuxControlNumberEntity(ISYAuxControlEntity, NumberEntity):
    _attr_mode: Incomplete
    @property
    def native_value(self) -> float | int | None: ...
    async def async_set_native_value(self, value: float) -> None: ...

class ISYVariableNumberEntity(NumberEntity):
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _init_entity: bool
    _node: Variable
    entity_description: NumberEntityDescription
    _change_handler: EventListener | None
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, node: Variable, unique_id: str, description: NumberEntityDescription, device_info: DeviceInfo, init_entity: bool = False) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def async_on_update(self, event: NodeProperty) -> None: ...
    @property
    def native_value(self) -> float | int | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    async def async_set_native_value(self, value: float) -> None: ...

class ISYBacklightNumberEntity(ISYAuxControlEntity, RestoreNumber):
    _assumed_state: bool
    _memory_change_handler: EventListener | None
    _attr_native_value: int
    def __init__(self, node: Node, control: str, unique_id: str, description: NumberEntityDescription, device_info: DeviceInfo | None) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def async_on_memory_write(self, event: NodeChangedEvent, key: str) -> None: ...
    async def async_set_native_value(self, value: float) -> None: ...
