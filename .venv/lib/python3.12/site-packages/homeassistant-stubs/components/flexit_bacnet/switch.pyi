from . import FlexitCoordinator as FlexitCoordinator
from .const import DOMAIN as DOMAIN
from .entity import FlexitEntity as FlexitEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from flexit_bacnet import FlexitBACnet as FlexitBACnet
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

@dataclass(kw_only=True, frozen=True)
class FlexitSwitchEntityDescription(SwitchEntityDescription):
    is_on_fn: Callable[[FlexitBACnet], bool]
    turn_on_fn: Callable[[FlexitBACnet], Awaitable[None]]
    turn_off_fn: Callable[[FlexitBACnet], Awaitable[None]]

SWITCHES: tuple[FlexitSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FlexitSwitch(FlexitEntity, SwitchEntity):
    _attr_device_class: Incomplete
    entity_description: FlexitSwitchEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FlexitCoordinator, entity_description: FlexitSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
