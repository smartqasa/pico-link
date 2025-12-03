from . import DevoloHomeNetworkConfigEntry as DevoloHomeNetworkConfigEntry
from .const import DOMAIN as DOMAIN, SWITCH_GUEST_WIFI as SWITCH_GUEST_WIFI, SWITCH_LEDS as SWITCH_LEDS
from .coordinator import DevoloDataUpdateCoordinator as DevoloDataUpdateCoordinator
from .entity import DevoloCoordinatorEntity as DevoloCoordinatorEntity
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from devolo_plc_api.device import Device as Device
from devolo_plc_api.device_api import WifiGuestAccessGet
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int
type _DataType = WifiGuestAccessGet | bool

@dataclass(frozen=True, kw_only=True)
class DevoloSwitchEntityDescription[_DataT: _DataType](SwitchEntityDescription):
    is_on_func: Callable[[_DataT], bool]
    turn_on_func: Callable[[Device], Awaitable[bool]]
    turn_off_func: Callable[[Device], Awaitable[bool]]

SWITCH_TYPES: dict[str, DevoloSwitchEntityDescription[Any]]

async def async_setup_entry(hass: HomeAssistant, entry: DevoloHomeNetworkConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DevoloSwitchEntity[_DataT: _DataType](DevoloCoordinatorEntity[_DataT], SwitchEntity):
    entity_description: DevoloSwitchEntityDescription[_DataT]
    def __init__(self, entry: DevoloHomeNetworkConfigEntry, coordinator: DevoloDataUpdateCoordinator[_DataT], description: DevoloSwitchEntityDescription[_DataT]) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
