from .const import DOMAIN as DOMAIN
from .coordinator import SmDataUpdateCoordinator as SmDataUpdateCoordinator
from .entity import SmEntity as SmEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pysmlight.web import CmdWrapper as CmdWrapper

_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class SmButtonDescription(ButtonEntityDescription):
    press_fn: Callable[[CmdWrapper], Awaitable[None]]

BUTTONS: list[SmButtonDescription]
ROUTER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SmButton(SmEntity, ButtonEntity):
    coordinator: SmDataUpdateCoordinator
    entity_description: SmButtonDescription
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SmDataUpdateCoordinator, description: SmButtonDescription) -> None: ...
    async def async_press(self) -> None: ...
