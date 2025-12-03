from . import RingConfigEntry as RingConfigEntry
from .coordinator import RingDataCoordinator as RingDataCoordinator
from .entity import DeprecatedInfo as DeprecatedInfo, RingDeviceT as RingDeviceT, RingEntity as RingEntity, RingEntityDescription as RingEntityDescription, async_check_create_deprecated as async_check_create_deprecated, refresh_after as refresh_after
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine, Sequence
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Generic, Self

_LOGGER: Incomplete
IN_HOME_CHIME_IS_PRESENT: Incomplete

@dataclass(frozen=True, kw_only=True)
class RingSwitchEntityDescription(SwitchEntityDescription, RingEntityDescription, Generic[RingDeviceT]):
    exists_fn: Callable[[RingDeviceT], bool]
    unique_id_fn: Callable[[Self, RingDeviceT], str] = ...
    is_on_fn: Callable[[RingDeviceT], bool]
    turn_on_fn: Callable[[RingDeviceT], Coroutine[Any, Any, None]]
    turn_off_fn: Callable[[RingDeviceT], Coroutine[Any, Any, None]]

SWITCHES: Sequence[RingSwitchEntityDescription[Any]]

async def async_setup_entry(hass: HomeAssistant, entry: RingConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RingSwitch(RingEntity[RingDeviceT], SwitchEntity):
    entity_description: RingSwitchEntityDescription[RingDeviceT]
    _no_updates_until: Incomplete
    _attr_unique_id: Incomplete
    _attr_is_on: Incomplete
    def __init__(self, device: RingDeviceT, coordinator: RingDataCoordinator, description: RingSwitchEntityDescription[RingDeviceT]) -> None: ...
    _device: Incomplete
    @callback
    def _handle_coordinator_update(self) -> None: ...
    @refresh_after
    async def _async_set_switch(self, switch_on: bool) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
