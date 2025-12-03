from .const import DOMAIN as DOMAIN
from .coordinator import LaMetricDataUpdateCoordinator as LaMetricDataUpdateCoordinator
from .entity import LaMetricEntity as LaMetricEntity
from .helpers import lametric_exception_handler as lametric_exception_handler
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from demetriek import Device as Device, LaMetricDevice as LaMetricDevice
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

@dataclass(frozen=True, kw_only=True)
class LaMetricSwitchEntityDescription(SwitchEntityDescription):
    available_fn: Callable[[Device], bool] = ...
    has_fn: Callable[[Device], bool] = ...
    is_on_fn: Callable[[Device], bool]
    set_fn: Callable[[LaMetricDevice, bool], Awaitable[Any]]

SWITCHES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LaMetricSwitchEntity(LaMetricEntity, SwitchEntity):
    entity_description: LaMetricSwitchEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LaMetricDataUpdateCoordinator, description: LaMetricSwitchEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def is_on(self) -> bool: ...
    @lametric_exception_handler
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @lametric_exception_handler
    async def async_turn_off(self, **kwargs: Any) -> None: ...
