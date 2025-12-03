from .const import DOMAIN as DOMAIN
from .coordinator import FritzboxConfigEntry as FritzboxConfigEntry
from .entity import FritzBoxDeviceEntity as FritzBoxDeviceEntity
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: FritzboxConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FritzboxSwitch(FritzBoxDeviceEntity, SwitchEntity):
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def check_lock_state(self) -> None: ...
