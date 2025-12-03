from . import AirGradientConfigEntry as AirGradientConfigEntry
from .const import DOMAIN as DOMAIN, PM_STANDARD as PM_STANDARD, PM_STANDARD_REVERSE as PM_STANDARD_REVERSE
from .coordinator import AirGradientCoordinator as AirGradientCoordinator
from .entity import AirGradientEntity as AirGradientEntity
from _typeshed import Incomplete
from airgradient import AirGradientClient as AirGradientClient, Config as Config
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class AirGradientSelectEntityDescription(SelectEntityDescription):
    value_fn: Callable[[Config], str | None]
    set_value_fn: Callable[[AirGradientClient, str], Awaitable[None]]

CONFIG_CONTROL_ENTITY: Incomplete
DISPLAY_SELECT_TYPES: tuple[AirGradientSelectEntityDescription, ...]
LED_BAR_ENTITIES: tuple[AirGradientSelectEntityDescription, ...]
LEARNING_TIME_OFFSET_OPTIONS: Incomplete
ABC_DAYS: Incomplete

def _get_value(value: int, values: list[str]) -> str | None: ...

CONTROL_ENTITIES: tuple[AirGradientSelectEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: AirGradientConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AirGradientSelect(AirGradientEntity, SelectEntity):
    entity_description: AirGradientSelectEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AirGradientCoordinator, description: AirGradientSelectEntityDescription) -> None: ...
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...
