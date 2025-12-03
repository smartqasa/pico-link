from . import LektricoConfigEntry as LektricoConfigEntry, LektricoDeviceDataUpdateCoordinator as LektricoDeviceDataUpdateCoordinator
from .entity import LektricoEntity as LektricoEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import ATTR_SERIAL_NUMBER as ATTR_SERIAL_NUMBER, CONF_TYPE as CONF_TYPE, EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from lektricowifi import Device
from typing import Any

@dataclass(frozen=True, kw_only=True)
class LektricoSwitchEntityDescription(SwitchEntityDescription):
    value_fn: Callable[[dict[str, Any]], bool]
    set_value_fn: Callable[[Device, dict[Any, Any], bool], Coroutine[Any, Any, Any]]

SWITCHS_FOR_ALL_CHARGERS: tuple[LektricoSwitchEntityDescription, ...]
SWITCHS_FOR_3_PHASE_CHARGERS: tuple[LektricoSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: LektricoConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LektricoSwitch(LektricoEntity, SwitchEntity):
    entity_description: LektricoSwitchEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, description: LektricoSwitchEntityDescription, coordinator: LektricoDeviceDataUpdateCoordinator, device_name: str) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
