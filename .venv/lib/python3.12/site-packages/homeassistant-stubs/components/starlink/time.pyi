from .const import DOMAIN as DOMAIN
from .coordinator import StarlinkData as StarlinkData, StarlinkUpdateCoordinator as StarlinkUpdateCoordinator
from .entity import StarlinkEntity as StarlinkEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from datetime import time, tzinfo
from homeassistant.components.time import TimeEntity as TimeEntity, TimeEntityDescription as TimeEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

@dataclass(frozen=True, kw_only=True)
class StarlinkTimeEntityDescription(TimeEntityDescription):
    value_fn: Callable[[StarlinkData, tzinfo], time | None]
    update_fn: Callable[[StarlinkUpdateCoordinator, time], Awaitable[None]]
    available_fn: Callable[[StarlinkData], bool]

class StarlinkTimeEntity(StarlinkEntity, TimeEntity):
    entity_description: StarlinkTimeEntityDescription
    @property
    def native_value(self) -> time | None: ...
    @property
    def available(self) -> bool: ...
    async def async_set_value(self, value: time) -> None: ...

def _utc_minutes_to_time(utc_minutes: int, timezone: tzinfo) -> time: ...
def _time_to_utc_minutes(t: time, timezone: tzinfo) -> int: ...

TIMES: Incomplete
