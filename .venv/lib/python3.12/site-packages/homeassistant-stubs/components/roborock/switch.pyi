from . import DOMAIN as DOMAIN, RoborockConfigEntry as RoborockConfigEntry
from .coordinator import RoborockDataUpdateCoordinator as RoborockDataUpdateCoordinator
from .entity import RoborockEntityV1 as RoborockEntityV1
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from roborock.command_cache import CacheableAttribute
from roborock.version_1_apis.roborock_client_v1 import AttributeCache as AttributeCache
from typing import Any

_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class RoborockSwitchDescription(SwitchEntityDescription):
    cache_key: CacheableAttribute
    update_value: Callable[[AttributeCache, bool], Coroutine[Any, Any, None]]
    attribute: str

SWITCH_DESCRIPTIONS: list[RoborockSwitchDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: RoborockConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RoborockSwitch(RoborockEntityV1, SwitchEntity):
    entity_description: RoborockSwitchDescription
    def __init__(self, unique_id: str, coordinator: RoborockDataUpdateCoordinator, entity_description: RoborockSwitchDescription) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
