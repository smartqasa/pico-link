from .const import DOMAIN as DOMAIN
from .coordinator import RidwellDataUpdateCoordinator as RidwellDataUpdateCoordinator
from .entity import RidwellEntity as RidwellEntity
from _typeshed import Incomplete
from aioridwell.model import RidwellAccount as RidwellAccount
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

SWITCH_DESCRIPTION: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RidwellSwitch(RidwellEntity, SwitchEntity):
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: RidwellDataUpdateCoordinator, account: RidwellAccount, description: SwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
