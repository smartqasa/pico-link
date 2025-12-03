from . import SwitchbotCloudData as SwitchbotCloudData
from .const import DOMAIN as DOMAIN
from .entity import SwitchBotCloudEntity as SwitchBotCloudEntity
from _typeshed import Incomplete
from homeassistant.components.lock import LockEntity as LockEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SwitchBotCloudLock(SwitchBotCloudEntity, LockEntity):
    _attr_name: Incomplete
    _attr_is_locked: Incomplete
    @callback
    def _handle_coordinator_update(self) -> None: ...
    async def async_lock(self, **kwargs: Any) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...
