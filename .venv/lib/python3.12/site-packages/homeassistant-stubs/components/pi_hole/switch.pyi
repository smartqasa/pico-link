from . import PiHoleConfigEntry as PiHoleConfigEntry
from .const import SERVICE_DISABLE as SERVICE_DISABLE, SERVICE_DISABLE_ATTR_DURATION as SERVICE_DISABLE_ATTR_DURATION
from .entity import PiHoleEntity as PiHoleEntity
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: PiHoleConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PiHoleSwitch(PiHoleEntity, SwitchEntity):
    _attr_icon: str
    @property
    def name(self) -> str: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_disable(self, duration: Any = None) -> None: ...
