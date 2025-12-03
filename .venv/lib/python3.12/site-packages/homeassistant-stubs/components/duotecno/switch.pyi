from .const import DOMAIN as DOMAIN
from .entity import DuotecnoEntity as DuotecnoEntity, api_call as api_call
from duotecno.controller import PyDuotecno as PyDuotecno
from duotecno.unit import SwitchUnit as SwitchUnit
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DuotecnoSwitch(DuotecnoEntity, SwitchEntity):
    _unit: SwitchUnit
    @property
    def is_on(self) -> bool: ...
    @api_call
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @api_call
    async def async_turn_off(self, **kwargs: Any) -> None: ...
