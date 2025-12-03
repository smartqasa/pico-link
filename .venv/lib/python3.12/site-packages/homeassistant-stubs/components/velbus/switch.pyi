from . import VelbusConfigEntry as VelbusConfigEntry
from .entity import VelbusEntity as VelbusEntity, api_call as api_call
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any
from velbusaio.channels import Relay as VelbusRelay

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: VelbusConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class VelbusSwitch(VelbusEntity, SwitchEntity):
    _channel: VelbusRelay
    @property
    def is_on(self) -> bool: ...
    @api_call
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @api_call
    async def async_turn_off(self, **kwargs: Any) -> None: ...
