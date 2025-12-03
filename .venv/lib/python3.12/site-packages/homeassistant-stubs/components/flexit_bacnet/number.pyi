from . import FlexitCoordinator as FlexitCoordinator
from .const import DOMAIN as DOMAIN
from .entity import FlexitEntity as FlexitEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from flexit_bacnet import FlexitBACnet as FlexitBACnet
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription, NumberMode as NumberMode
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_MAX_FAN_SETPOINT: int
_MIN_FAN_SETPOINT: int

@dataclass(kw_only=True, frozen=True)
class FlexitNumberEntityDescription(NumberEntityDescription):
    native_value_fn: Callable[[FlexitBACnet], float]
    native_max_value_fn: Callable[[FlexitBACnet], int]
    native_min_value_fn: Callable[[FlexitBACnet], int]
    set_native_value_fn: Callable[[FlexitBACnet], Callable[[int], Awaitable[None]]]

NUMBERS: tuple[FlexitNumberEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FlexitNumber(FlexitEntity, NumberEntity):
    entity_description: FlexitNumberEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FlexitCoordinator, entity_description: FlexitNumberEntityDescription) -> None: ...
    @property
    def native_value(self) -> float: ...
    @property
    def native_max_value(self) -> float: ...
    @property
    def native_min_value(self) -> float: ...
    async def async_set_native_value(self, value: float) -> None: ...
