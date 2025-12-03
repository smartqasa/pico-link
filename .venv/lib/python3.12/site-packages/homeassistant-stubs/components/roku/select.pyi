from . import RokuConfigEntry as RokuConfigEntry
from .entity import RokuEntity as RokuEntity
from .helpers import format_channel_name as format_channel_name, roku_exception_handler as roku_exception_handler
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from rokuecp import Roku as Roku
from rokuecp.models import Device as RokuDevice

PARALLEL_UPDATES: int

def _get_application_name(device: RokuDevice) -> str | None: ...
def _get_applications(device: RokuDevice) -> list[str]: ...
def _get_channel_name(device: RokuDevice) -> str | None: ...
def _get_channels(device: RokuDevice) -> list[str]: ...
async def _launch_application(device: RokuDevice, roku: Roku, value: str) -> None: ...
async def _tune_channel(device: RokuDevice, roku: Roku, value: str) -> None: ...

@dataclass(frozen=True, kw_only=True)
class RokuSelectEntityDescription(SelectEntityDescription):
    options_fn: Callable[[RokuDevice], list[str]]
    value_fn: Callable[[RokuDevice], str | None]
    set_fn: Callable[[RokuDevice, Roku, str], Awaitable[None]]

ENTITIES: tuple[RokuSelectEntityDescription, ...]
CHANNEL_ENTITY: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: RokuConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RokuSelectEntity(RokuEntity, SelectEntity):
    entity_description: RokuSelectEntityDescription
    @property
    def current_option(self) -> str | None: ...
    @property
    def options(self) -> list[str]: ...
    async def async_select_option(self, option: str) -> None: ...
