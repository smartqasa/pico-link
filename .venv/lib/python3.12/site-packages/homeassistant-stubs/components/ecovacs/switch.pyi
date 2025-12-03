from . import EcovacsConfigEntry as EcovacsConfigEntry
from .entity import EcovacsCapabilityEntityDescription as EcovacsCapabilityEntityDescription, EcovacsDescriptionEntity as EcovacsDescriptionEntity, EcovacsEntity as EcovacsEntity
from .util import get_supported_entitites as get_supported_entitites
from dataclasses import dataclass
from deebot_client.capabilities import CapabilitySetEnable
from deebot_client.events import EnableEvent as EnableEvent
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

@dataclass(kw_only=True, frozen=True)
class EcovacsSwitchEntityDescription(SwitchEntityDescription, EcovacsCapabilityEntityDescription[CapabilitySetEnable]): ...

ENTITY_DESCRIPTIONS: tuple[EcovacsSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: EcovacsConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EcovacsSwitchEntity(EcovacsDescriptionEntity[CapabilitySetEnable], SwitchEntity):
    entity_description: EcovacsSwitchEntityDescription
    _attr_is_on: bool
    async def async_added_to_hass(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
