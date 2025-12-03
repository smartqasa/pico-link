from .coordinator import PeblarConfigEntry as PeblarConfigEntry, PeblarVersionDataUpdateCoordinator as PeblarVersionDataUpdateCoordinator, PeblarVersionInformation as PeblarVersionInformation
from .entity import PeblarEntity as PeblarEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class PeblarUpdateEntityDescription(UpdateEntityDescription):
    available_fn: Callable[[PeblarVersionInformation], str | None]
    has_fn: Callable[[PeblarVersionInformation], bool] = ...
    installed_fn: Callable[[PeblarVersionInformation], str | None]

DESCRIPTIONS: tuple[PeblarUpdateEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: PeblarConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PeblarUpdateEntity(PeblarEntity[PeblarVersionDataUpdateCoordinator], UpdateEntity):
    entity_description: PeblarUpdateEntityDescription
    @property
    def installed_version(self) -> str | None: ...
    @property
    def latest_version(self) -> str | None: ...
