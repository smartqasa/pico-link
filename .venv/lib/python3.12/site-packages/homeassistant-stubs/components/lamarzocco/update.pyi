from .const import DOMAIN as DOMAIN
from .coordinator import LaMarzoccoConfigEntry as LaMarzoccoConfigEntry
from .entity import LaMarzoccoEntity as LaMarzoccoEntity, LaMarzoccoEntityDescription as LaMarzoccoEntityDescription
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pylamarzocco.const import FirmwareType
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class LaMarzoccoUpdateEntityDescription(LaMarzoccoEntityDescription, UpdateEntityDescription):
    component: FirmwareType

ENTITIES: tuple[LaMarzoccoUpdateEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: LaMarzoccoConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LaMarzoccoUpdateEntity(LaMarzoccoEntity, UpdateEntity):
    entity_description: LaMarzoccoUpdateEntityDescription
    _attr_supported_features: Incomplete
    @property
    def installed_version(self) -> str | None: ...
    @property
    def latest_version(self) -> str: ...
    @property
    def release_url(self) -> str | None: ...
    _attr_in_progress: bool
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...
