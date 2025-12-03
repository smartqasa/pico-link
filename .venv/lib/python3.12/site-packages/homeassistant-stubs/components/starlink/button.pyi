from .const import DOMAIN as DOMAIN
from .coordinator import StarlinkUpdateCoordinator as StarlinkUpdateCoordinator
from .entity import StarlinkEntity as StarlinkEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

@dataclass(frozen=True, kw_only=True)
class StarlinkButtonEntityDescription(ButtonEntityDescription):
    press_fn: Callable[[StarlinkUpdateCoordinator], Awaitable[None]]

class StarlinkButtonEntity(StarlinkEntity, ButtonEntity):
    entity_description: StarlinkButtonEntityDescription
    async def async_press(self) -> None: ...

BUTTONS: Incomplete
