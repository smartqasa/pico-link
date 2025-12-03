from . import RingConfigEntry as RingConfigEntry
from .coordinator import RingDataCoordinator as RingDataCoordinator
from .entity import RingDeviceT as RingDeviceT, RingEntity as RingEntity, RingEntityDescription as RingEntityDescription, async_check_create_deprecated as async_check_create_deprecated, refresh_after as refresh_after
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.siren import ATTR_TONE as ATTR_TONE, SirenEntity as SirenEntity, SirenEntityDescription as SirenEntityDescription, SirenEntityFeature as SirenEntityFeature, SirenTurnOnServiceParameters as SirenTurnOnServiceParameters
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from ring_doorbell import RingGeneric as RingGeneric
from typing import Any, Generic

_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class RingSirenEntityDescription(SirenEntityDescription, RingEntityDescription, Generic[RingDeviceT]):
    exists_fn: Callable[[RingGeneric], bool]
    unique_id_fn: Callable[[RingDeviceT], str] = ...
    is_on_fn: Callable[[RingDeviceT], bool] | None = ...
    turn_on_fn: Callable[[RingDeviceT, SirenTurnOnServiceParameters], Coroutine[Any, Any, Any]] | None = ...
    turn_off_fn: Callable[[RingDeviceT], Coroutine[Any, Any, None]] | None = ...

SIRENS: tuple[RingSirenEntityDescription[Any], ...]

async def async_setup_entry(hass: HomeAssistant, entry: RingConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RingSiren(RingEntity[RingDeviceT], SirenEntity):
    entity_description: RingSirenEntityDescription[RingDeviceT]
    _attr_unique_id: Incomplete
    _attr_is_on: Incomplete
    _attr_supported_features: Incomplete
    def __init__(self, device: RingDeviceT, coordinator: RingDataCoordinator, description: RingSirenEntityDescription[RingDeviceT]) -> None: ...
    async def _async_set_siren(self, siren_on: bool, **kwargs: Any) -> None: ...
    @refresh_after
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @refresh_after
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _device: Incomplete
    @callback
    def _handle_coordinator_update(self) -> None: ...
