from . import LektricoConfigEntry as LektricoConfigEntry, LektricoDeviceDataUpdateCoordinator as LektricoDeviceDataUpdateCoordinator
from .entity import LektricoEntity as LektricoEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import ATTR_SERIAL_NUMBER as ATTR_SERIAL_NUMBER, CONF_TYPE as CONF_TYPE, EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from lektricowifi import Device as Device
from typing import Any

@dataclass(frozen=True, kw_only=True)
class LektricoSelectEntityDescription(SelectEntityDescription):
    value_fn: Callable[[dict[str, Any]], str]
    set_value_fn: Callable[[Device, int], Coroutine[Any, Any, dict[Any, Any]]]

LB_MODE_OPTIONS: Incomplete
SELECTS: tuple[LektricoSelectEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: LektricoConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LektricoSelect(LektricoEntity, SelectEntity):
    entity_description: LektricoSelectEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, description: LektricoSelectEntityDescription, coordinator: LektricoDeviceDataUpdateCoordinator, device_name: str) -> None: ...
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...
