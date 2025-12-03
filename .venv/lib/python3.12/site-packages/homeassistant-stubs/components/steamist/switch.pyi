from .const import DOMAIN as DOMAIN
from .coordinator import SteamistDataUpdateCoordinator as SteamistDataUpdateCoordinator
from .entity import SteamistEntity as SteamistEntity
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

ACTIVE_SWITCH: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SteamistSwitchEntity(SteamistEntity, SwitchEntity):
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
