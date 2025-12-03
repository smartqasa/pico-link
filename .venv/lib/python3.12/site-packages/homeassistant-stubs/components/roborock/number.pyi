from . import DOMAIN as DOMAIN, RoborockConfigEntry as RoborockConfigEntry
from .coordinator import RoborockDataUpdateCoordinator as RoborockDataUpdateCoordinator
from .entity import RoborockEntityV1 as RoborockEntityV1
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from roborock.command_cache import CacheableAttribute
from roborock.version_1_apis.roborock_client_v1 import AttributeCache as AttributeCache
from typing import Any

_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class RoborockNumberDescription(NumberEntityDescription):
    cache_key: CacheableAttribute
    update_value: Callable[[AttributeCache, float], Coroutine[Any, Any, None]]

NUMBER_DESCRIPTIONS: list[RoborockNumberDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: RoborockConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RoborockNumberEntity(RoborockEntityV1, NumberEntity):
    entity_description: RoborockNumberDescription
    def __init__(self, unique_id: str, coordinator: RoborockDataUpdateCoordinator, entity_description: RoborockNumberDescription) -> None: ...
    @property
    def native_value(self) -> float | None: ...
    async def async_set_native_value(self, value: float) -> None: ...
