from . import FullyKioskConfigEntry as FullyKioskConfigEntry
from .coordinator import FullyKioskDataUpdateCoordinator as FullyKioskDataUpdateCoordinator
from .entity import FullyKioskEntity as FullyKioskEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.notify import NotifyEntity as NotifyEntity, NotifyEntityDescription as NotifyEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class FullyNotifyEntityDescription(NotifyEntityDescription):
    cmd: str

NOTIFIERS: tuple[FullyNotifyEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: FullyKioskConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FullyNotifyEntity(FullyKioskEntity, NotifyEntity):
    entity_description: FullyNotifyEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FullyKioskDataUpdateCoordinator, description: FullyNotifyEntityDescription) -> None: ...
    async def async_send_message(self, message: str, title: str | None = None) -> None: ...
