from .const import DOMAIN as DOMAIN
from .coordinator import TailwindConfigEntry as TailwindConfigEntry
from .entity import TailwindEntity as TailwindEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from gotailwind import Tailwind as Tailwind, TailwindDeviceStatus as TailwindDeviceStatus
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

@dataclass(frozen=True, kw_only=True)
class TailwindNumberEntityDescription(NumberEntityDescription):
    value_fn: Callable[[TailwindDeviceStatus], int]
    set_value_fn: Callable[[Tailwind, float], Awaitable[Any]]

DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: TailwindConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TailwindNumberEntity(TailwindEntity, NumberEntity):
    entity_description: TailwindNumberEntityDescription
    @property
    def native_value(self) -> int | None: ...
    async def async_set_native_value(self, value: float) -> None: ...
