import abc
from . import AirzoneCloudConfigEntry as AirzoneCloudConfigEntry
from .coordinator import AirzoneUpdateCoordinator as AirzoneUpdateCoordinator
from .entity import AirzoneEntity as AirzoneEntity, AirzoneZoneEntity as AirzoneZoneEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Final

@dataclass(frozen=True, kw_only=True)
class AirzoneSelectDescription(SelectEntityDescription):
    api_param: str
    options_dict: dict[str, Any]
    options_fn: Callable[[dict[str, Any], dict[str, Any]], list[str]] = ...

AIR_QUALITY_MAP: Final[dict[str, str]]
MODE_MAP: Final[dict[str, int]]

def main_zone_options(zone_data: dict[str, Any], options: dict[str, int]) -> list[str]: ...

MAIN_ZONE_SELECT_TYPES: Final[tuple[AirzoneSelectDescription, ...]]
ZONE_SELECT_TYPES: Final[tuple[AirzoneSelectDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: AirzoneCloudConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AirzoneBaseSelect(AirzoneEntity, SelectEntity, metaclass=abc.ABCMeta):
    entity_description: AirzoneSelectDescription
    values_dict: dict[str, str]
    @callback
    def _handle_coordinator_update(self) -> None: ...
    def _get_current_option(self) -> str | None: ...
    _attr_current_option: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...

class AirzoneZoneSelect(AirzoneZoneEntity, AirzoneBaseSelect):
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    _attr_options: Incomplete
    values_dict: Incomplete
    def __init__(self, coordinator: AirzoneUpdateCoordinator, description: AirzoneSelectDescription, zone_id: str, zone_data: dict[str, Any]) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
