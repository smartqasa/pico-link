from . import SmConfigEntry as SmConfigEntry
from .coordinator import SmDataUpdateCoordinator as SmDataUpdateCoordinator
from .entity import SmEntity as SmEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pysmlight import Sensors as Sensors, SettingsEvent as SettingsEvent
from pysmlight.const import Settings
from typing import Any

_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class SmSwitchEntityDescription(SwitchEntityDescription):
    setting: Settings
    state_fn: Callable[[Sensors], bool | None]

SWITCHES: list[SmSwitchEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: SmConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SmSwitch(SmEntity, SwitchEntity):
    coordinator: SmDataUpdateCoordinator
    entity_description: SmSwitchEntityDescription
    _attr_device_class: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SmDataUpdateCoordinator, description: SmSwitchEntityDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def set_smlight(self, state: bool) -> None: ...
    @callback
    def event_callback(self, event: SettingsEvent) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
