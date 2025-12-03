from .const import DOMAIN as DOMAIN
from .coordinator import ToloSaunaUpdateCoordinator as ToloSaunaUpdateCoordinator
from .entity import ToloSaunaCoordinatorEntity as ToloSaunaCoordinatorEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from tololib import ToloClient as ToloClient, ToloStatus as ToloStatus
from typing import Any

@dataclass(frozen=True, kw_only=True)
class ToloSwitchEntityDescription(SwitchEntityDescription):
    getter: Callable[[ToloStatus], bool]
    setter: Callable[[ToloClient, bool], bool]

SWITCHES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ToloSwitchEntity(ToloSaunaCoordinatorEntity, SwitchEntity):
    entity_description: ToloSwitchEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ToloSaunaUpdateCoordinator, entry: ConfigEntry, entity_description: ToloSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
