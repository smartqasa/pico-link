from . import OverkizDataConfigEntry as OverkizDataConfigEntry
from .entity import OverkizDescriptiveEntity as OverkizDescriptiveEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyoverkiz.types import StateType as OverkizStateType
from typing import Any

@dataclass(frozen=True, kw_only=True)
class OverkizSwitchDescription(SwitchEntityDescription):
    turn_on: str
    turn_off: str
    is_on: Callable[[Callable[[str], OverkizStateType]], bool] | None = ...
    turn_on_args: OverkizStateType | list[OverkizStateType] | None = ...
    turn_off_args: OverkizStateType | list[OverkizStateType] | None = ...

SWITCH_DESCRIPTIONS: list[OverkizSwitchDescription]
SUPPORTED_DEVICES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: OverkizDataConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OverkizSwitch(OverkizDescriptiveEntity, SwitchEntity):
    entity_description: OverkizSwitchDescription
    @property
    def is_on(self) -> bool | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
