from . import BAFConfigEntry as BAFConfigEntry
from .entity import BAFDescriptionEntity as BAFDescriptionEntity
from _typeshed import Incomplete
from aiobafi6 import Device as Device
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

@dataclass(frozen=True, kw_only=True)
class BAFSwitchDescription(SwitchEntityDescription):
    value_fn: Callable[[Device], bool | None]

BASE_SWITCHES: Incomplete
AUTO_COMFORT_SWITCHES: Incomplete
FAN_SWITCHES: Incomplete
LIGHT_SWITCHES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: BAFConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BAFSwitch(BAFDescriptionEntity, SwitchEntity):
    entity_description: BAFSwitchDescription
    _attr_is_on: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
