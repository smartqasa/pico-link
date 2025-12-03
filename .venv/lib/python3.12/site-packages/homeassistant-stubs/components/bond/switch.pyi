from . import BondConfigEntry as BondConfigEntry
from .const import ATTR_POWER_STATE as ATTR_POWER_STATE, SERVICE_SET_POWER_TRACKED_STATE as SERVICE_SET_POWER_TRACKED_STATE
from .entity import BondEntity as BondEntity
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: BondConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BondSwitch(BondEntity, SwitchEntity):
    _attr_is_on: Incomplete
    def _apply_state(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_set_power_belief(self, power_state: bool) -> None: ...
