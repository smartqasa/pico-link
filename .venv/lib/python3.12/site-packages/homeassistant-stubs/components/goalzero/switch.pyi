from .coordinator import GoalZeroConfigEntry as GoalZeroConfigEntry
from .entity import GoalZeroEntity as GoalZeroEntity
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

SWITCH_TYPES: tuple[SwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: GoalZeroConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class GoalZeroSwitch(GoalZeroEntity, SwitchEntity):
    @property
    def is_on(self) -> bool: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
