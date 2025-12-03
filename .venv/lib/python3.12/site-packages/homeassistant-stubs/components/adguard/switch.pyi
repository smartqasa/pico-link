from . import AdGuardConfigEntry as AdGuardConfigEntry, AdGuardData as AdGuardData
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from .entity import AdGuardHomeEntity as AdGuardHomeEntity
from _typeshed import Incomplete
from adguardhome import AdGuardHome as AdGuardHome
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

SCAN_INTERVAL: Incomplete
PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class AdGuardHomeSwitchEntityDescription(SwitchEntityDescription):
    is_on_fn: Callable[[AdGuardHome], Callable[[], Coroutine[Any, Any, bool]]]
    turn_on_fn: Callable[[AdGuardHome], Callable[[], Coroutine[Any, Any, None]]]
    turn_off_fn: Callable[[AdGuardHome], Callable[[], Coroutine[Any, Any, None]]]

SWITCHES: tuple[AdGuardHomeSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: AdGuardConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AdGuardHomeSwitch(AdGuardHomeEntity, SwitchEntity):
    entity_description: AdGuardHomeSwitchEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, data: AdGuardData, entry: AdGuardConfigEntry, description: AdGuardHomeSwitchEntityDescription) -> None: ...
    _attr_available: bool
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    async def _adguard_update(self) -> None: ...
