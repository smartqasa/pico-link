from . import AirGradientConfigEntry as AirGradientConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import AirGradientCoordinator as AirGradientCoordinator
from .entity import AirGradientEntity as AirGradientEntity
from _typeshed import Incomplete
from airgradient import AirGradientClient as AirGradientClient, Config as Config
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class AirGradientNumberEntityDescription(NumberEntityDescription):
    value_fn: Callable[[Config], int]
    set_value_fn: Callable[[AirGradientClient, int], Awaitable[None]]

DISPLAY_BRIGHTNESS: Incomplete
LED_BAR_BRIGHTNESS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: AirGradientConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AirGradientNumber(AirGradientEntity, NumberEntity):
    entity_description: AirGradientNumberEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AirGradientCoordinator, description: AirGradientNumberEntityDescription) -> None: ...
    @property
    def native_value(self) -> int | None: ...
    async def async_set_native_value(self, value: float) -> None: ...
