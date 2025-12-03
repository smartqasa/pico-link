import datetime
from . import DOMAIN as DOMAIN, RoborockConfigEntry as RoborockConfigEntry
from .coordinator import RoborockDataUpdateCoordinator as RoborockDataUpdateCoordinator
from .entity import RoborockEntityV1 as RoborockEntityV1
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from datetime import time
from homeassistant.components.time import TimeEntity as TimeEntity, TimeEntityDescription as TimeEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from roborock.command_cache import CacheableAttribute
from roborock.version_1_apis.roborock_client_v1 import AttributeCache as AttributeCache
from typing import Any

_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class RoborockTimeDescription(TimeEntityDescription):
    cache_key: CacheableAttribute
    update_value: Callable[[AttributeCache, datetime.time], Coroutine[Any, Any, None]]
    get_value: Callable[[AttributeCache], datetime.time]

TIME_DESCRIPTIONS: list[RoborockTimeDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: RoborockConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RoborockTimeEntity(RoborockEntityV1, TimeEntity):
    entity_description: RoborockTimeDescription
    def __init__(self, unique_id: str, coordinator: RoborockDataUpdateCoordinator, entity_description: RoborockTimeDescription) -> None: ...
    @property
    def native_value(self) -> time | None: ...
    async def async_set_value(self, value: time) -> None: ...
