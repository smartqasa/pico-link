from . import RingConfigEntry as RingConfigEntry
from .coordinator import RingDataCoordinator as RingDataCoordinator
from .entity import RingDeviceT as RingDeviceT, RingEntity as RingEntity, refresh_after as refresh_after
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription, NumberMode as NumberMode
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from ring_doorbell import RingGeneric as RingGeneric
from typing import Any, Generic

async def async_setup_entry(hass: HomeAssistant, entry: RingConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

@dataclass(frozen=True, kw_only=True)
class RingNumberEntityDescription(NumberEntityDescription, Generic[RingDeviceT]):
    value_fn: Callable[[RingDeviceT], StateType]
    setter_fn: Callable[[RingDeviceT, float], Awaitable[None]]
    exists_fn: Callable[[RingGeneric], bool]

NUMBER_TYPES: tuple[RingNumberEntityDescription[Any], ...]

class RingNumber(RingEntity[RingDeviceT], NumberEntity):
    entity_description: RingNumberEntityDescription[RingDeviceT]
    _attr_unique_id: Incomplete
    def __init__(self, device: RingDeviceT, coordinator: RingDataCoordinator, description: RingNumberEntityDescription[RingDeviceT]) -> None: ...
    _attr_native_value: Incomplete
    def _update_native_value(self) -> None: ...
    _device: Incomplete
    @callback
    def _handle_coordinator_update(self) -> None: ...
    @refresh_after
    async def async_set_native_value(self, value: float) -> None: ...
