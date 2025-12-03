from .const import DEFAULT_WATERING_TIME as DEFAULT_WATERING_TIME, DOMAIN as DOMAIN
from .coordinator import HydrawiseUpdateCoordinators as HydrawiseUpdateCoordinators
from .entity import HydrawiseEntity as HydrawiseEntity
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pydrawise import Hydrawise as Hydrawise, Zone as Zone
from typing import Any

@dataclass(frozen=True, kw_only=True)
class HydrawiseSwitchEntityDescription(SwitchEntityDescription):
    turn_on_fn: Callable[[Hydrawise, Zone], Coroutine[Any, Any, None]]
    turn_off_fn: Callable[[Hydrawise, Zone], Coroutine[Any, Any, None]]
    value_fn: Callable[[Zone], bool]

SWITCH_TYPES: tuple[HydrawiseSwitchEntityDescription, ...]
SWITCH_KEYS: list[str]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HydrawiseSwitch(HydrawiseEntity, SwitchEntity):
    entity_description: HydrawiseSwitchEntityDescription
    zone: Zone
    _attr_is_on: bool
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def _update_attrs(self) -> None: ...
