from . import FullyKioskConfigEntry as FullyKioskConfigEntry
from .coordinator import FullyKioskDataUpdateCoordinator as FullyKioskDataUpdateCoordinator
from .entity import FullyKioskEntity as FullyKioskEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from fullykiosk import FullyKiosk as FullyKiosk
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

@dataclass(frozen=True, kw_only=True)
class FullySwitchEntityDescription(SwitchEntityDescription):
    on_action: Callable[[FullyKiosk], Any]
    off_action: Callable[[FullyKiosk], Any]
    is_on_fn: Callable[[dict[str, Any]], Any]
    mqtt_on_event: str | None
    mqtt_off_event: str | None

SWITCHES: tuple[FullySwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: FullyKioskConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FullySwitchEntity(FullyKioskEntity, SwitchEntity):
    entity_description: FullySwitchEntityDescription
    _attr_unique_id: Incomplete
    _turned_on_subscription: CALLBACK_TYPE | None
    _turned_off_subscription: CALLBACK_TYPE | None
    def __init__(self, coordinator: FullyKioskDataUpdateCoordinator, description: FullySwitchEntityDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_is_on: bool
    def _turn_off(self, **kwargs: Any) -> None: ...
    def _turn_on(self, **kwargs: Any) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
