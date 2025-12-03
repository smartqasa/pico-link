from . import EcovacsConfigEntry as EcovacsConfigEntry
from .const import SUPPORTED_LIFESPANS as SUPPORTED_LIFESPANS, SUPPORTED_STATION_ACTIONS as SUPPORTED_STATION_ACTIONS
from .entity import EcovacsCapabilityEntityDescription as EcovacsCapabilityEntityDescription, EcovacsDescriptionEntity as EcovacsDescriptionEntity, EcovacsEntity as EcovacsEntity
from .util import get_supported_entitites as get_supported_entitites
from _typeshed import Incomplete
from dataclasses import dataclass
from deebot_client.capabilities import CapabilityExecute, CapabilityExecuteTypes, CapabilityLifeSpan
from deebot_client.commands import StationAction
from deebot_client.events import LifeSpan as LifeSpan
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(kw_only=True, frozen=True)
class EcovacsButtonEntityDescription(ButtonEntityDescription, EcovacsCapabilityEntityDescription): ...

@dataclass(kw_only=True, frozen=True)
class EcovacsLifespanButtonEntityDescription(ButtonEntityDescription):
    component: LifeSpan

@dataclass(kw_only=True, frozen=True)
class EcovacsStationActionButtonEntityDescription(ButtonEntityDescription):
    action: StationAction

ENTITY_DESCRIPTIONS: tuple[EcovacsButtonEntityDescription, ...]
STATION_ENTITY_DESCRIPTIONS: Incomplete
LIFESPAN_ENTITY_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: EcovacsConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EcovacsButtonEntity(EcovacsDescriptionEntity[CapabilityExecute], ButtonEntity):
    entity_description: EcovacsLifespanButtonEntityDescription
    async def async_press(self) -> None: ...

class EcovacsResetLifespanButtonEntity(EcovacsDescriptionEntity[CapabilityLifeSpan], ButtonEntity):
    entity_description: EcovacsLifespanButtonEntityDescription
    async def async_press(self) -> None: ...

class EcovacsStationActionButtonEntity(EcovacsDescriptionEntity[CapabilityExecuteTypes[StationAction]], ButtonEntity):
    entity_description: EcovacsStationActionButtonEntityDescription
    async def async_press(self) -> None: ...
