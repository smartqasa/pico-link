from .const import NEATO_LOGIN as NEATO_LOGIN, NEATO_ROBOTS as NEATO_ROBOTS, SCAN_INTERVAL_MINUTES as SCAN_INTERVAL_MINUTES
from .entity import NeatoEntity as NeatoEntity
from .hub import NeatoHub as NeatoHub
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pybotvac.robot import Robot as Robot
from typing import Any

_LOGGER: Incomplete
SCAN_INTERVAL: Incomplete
SWITCH_TYPE_SCHEDULE: str
SWITCH_TYPES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NeatoConnectedSwitch(NeatoEntity, SwitchEntity):
    _attr_translation_key: str
    _attr_available: bool
    _attr_entity_category: Incomplete
    type: Incomplete
    _state: dict[str, Any] | None
    _schedule_state: str | None
    _clean_state: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, neato: NeatoHub, robot: Robot, switch_type: str) -> None: ...
    def update(self) -> None: ...
    @property
    def is_on(self) -> bool: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
