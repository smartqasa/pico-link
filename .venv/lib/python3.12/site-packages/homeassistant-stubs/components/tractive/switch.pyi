from . import Trackables as Trackables, TractiveClient as TractiveClient, TractiveConfigEntry as TractiveConfigEntry
from .const import ATTR_BUZZER as ATTR_BUZZER, ATTR_LED as ATTR_LED, ATTR_LIVE_TRACKING as ATTR_LIVE_TRACKING, TRACKER_SWITCH_STATUS_UPDATED as TRACKER_SWITCH_STATUS_UPDATED
from .entity import TractiveEntity as TractiveEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Literal

_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class TractiveSwitchEntityDescription(SwitchEntityDescription):
    method: Literal['async_set_buzzer', 'async_set_led', 'async_set_live_tracking']

SWITCH_TYPES: tuple[TractiveSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: TractiveConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TractiveSwitch(TractiveEntity, SwitchEntity):
    entity_description: TractiveSwitchEntityDescription
    _attr_unique_id: Incomplete
    _tracker: Incomplete
    _method: Incomplete
    def __init__(self, client: TractiveClient, item: Trackables, description: TractiveSwitchEntityDescription) -> None: ...
    _attr_available: bool
    _attr_is_on: Incomplete
    @callback
    def handle_status_update(self, event: dict[str, Any]) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_set_buzzer(self, active: bool) -> dict[str, Any]: ...
    async def async_set_led(self, active: bool) -> dict[str, Any]: ...
    async def async_set_live_tracking(self, active: bool) -> dict[str, Any]: ...
