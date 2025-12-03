from .const import DOMAIN as DOMAIN
from .coordinator import SynologyDSMCentralUpdateCoordinator as SynologyDSMCentralUpdateCoordinator
from .entity import SynologyDSMBaseEntity as SynologyDSMBaseEntity, SynologyDSMEntityDescription as SynologyDSMEntityDescription
from .models import SynologyDSMData as SynologyDSMData
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.update import UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Final

@dataclass(frozen=True, kw_only=True)
class SynologyDSMUpdateEntityEntityDescription(UpdateEntityDescription, SynologyDSMEntityDescription): ...

UPDATE_ENTITIES: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SynoDSMUpdateEntity(SynologyDSMBaseEntity[SynologyDSMCentralUpdateCoordinator], UpdateEntity):
    entity_description: SynologyDSMUpdateEntityEntityDescription
    _attr_title: str
    @property
    def available(self) -> bool: ...
    @property
    def installed_version(self) -> str | None: ...
    @property
    def latest_version(self) -> str | None: ...
    @property
    def release_url(self) -> str | None: ...
