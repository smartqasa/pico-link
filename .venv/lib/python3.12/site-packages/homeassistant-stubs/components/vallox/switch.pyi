from .const import DOMAIN as DOMAIN
from .coordinator import ValloxDataUpdateCoordinator as ValloxDataUpdateCoordinator
from .entity import ValloxEntity as ValloxEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any
from vallox_websocket_api import Vallox as Vallox

class ValloxSwitchEntity(ValloxEntity, SwitchEntity):
    entity_description: ValloxSwitchEntityDescription
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    _client: Incomplete
    def __init__(self, name: str, coordinator: ValloxDataUpdateCoordinator, description: ValloxSwitchEntityDescription, client: Vallox) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def _set_value(self, value: bool) -> None: ...

@dataclass(frozen=True, kw_only=True)
class ValloxSwitchEntityDescription(SwitchEntityDescription):
    metric_key: str

SWITCH_ENTITIES: tuple[ValloxSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
