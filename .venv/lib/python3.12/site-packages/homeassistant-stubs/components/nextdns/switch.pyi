from . import NextDnsConfigEntry as NextDnsConfigEntry
from .coordinator import NextDnsUpdateCoordinator as NextDnsUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from nextdns import Settings
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class NextDnsSwitchEntityDescription(SwitchEntityDescription):
    state: Callable[[Settings], bool]

SWITCHES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: NextDnsConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NextDnsSwitch(CoordinatorEntity[NextDnsUpdateCoordinator[Settings]], SwitchEntity):
    _attr_has_entity_name: bool
    entity_description: NextDnsSwitchEntityDescription
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    _attr_is_on: Incomplete
    def __init__(self, coordinator: NextDnsUpdateCoordinator[Settings], description: NextDnsSwitchEntityDescription) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_set_setting(self, new_state: bool) -> None: ...
