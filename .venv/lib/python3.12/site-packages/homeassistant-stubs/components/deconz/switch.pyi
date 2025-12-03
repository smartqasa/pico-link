from .const import POWER_PLUGS as POWER_PLUGS
from .entity import DeconzDevice as DeconzDevice
from .hub import DeconzHub as DeconzHub
from homeassistant.components.switch import DOMAIN as SWITCH_DOMAIN, SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pydeconz.models.event import EventType as EventType
from pydeconz.models.light.light import Light
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DeconzPowerPlug(DeconzDevice[Light], SwitchEntity):
    TYPE = SWITCH_DOMAIN
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
