from . import OverkizDataConfigEntry as OverkizDataConfigEntry
from .const import IGNORED_OVERKIZ_DEVICES as IGNORED_OVERKIZ_DEVICES
from .entity import OverkizDescriptiveEntity as OverkizDescriptiveEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class OverkizSelectDescription(SelectEntityDescription):
    select_option: Callable[[str, Callable[..., Awaitable[None]]], Awaitable[None]]

def _select_option_open_closed_pedestrian(option: str, execute_command: Callable[..., Awaitable[None]]) -> Awaitable[None]: ...
def _select_option_open_closed_partial(option: str, execute_command: Callable[..., Awaitable[None]]) -> Awaitable[None]: ...
def _select_option_memorized_simple_volume(option: str, execute_command: Callable[..., Awaitable[None]]) -> Awaitable[None]: ...
def _select_option_active_zone(option: str, execute_command: Callable[..., Awaitable[None]]) -> Awaitable[None]: ...

SELECT_DESCRIPTIONS: list[OverkizSelectDescription]
SUPPORTED_STATES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: OverkizDataConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OverkizSelect(OverkizDescriptiveEntity, SelectEntity):
    entity_description: OverkizSelectDescription
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...
