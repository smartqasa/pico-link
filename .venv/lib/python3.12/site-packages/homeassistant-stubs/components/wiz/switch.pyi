from . import WizConfigEntry as WizConfigEntry
from .entity import WizToggleEntity as WizToggleEntity
from .models import WizData as WizData
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: WizConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WizSocketEntity(WizToggleEntity, SwitchEntity):
    _attr_name: Incomplete
    def __init__(self, wiz_data: WizData, name: str) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
