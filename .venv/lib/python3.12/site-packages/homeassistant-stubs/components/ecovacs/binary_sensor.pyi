from . import EcovacsConfigEntry as EcovacsConfigEntry
from .entity import EcovacsCapabilityEntityDescription as EcovacsCapabilityEntityDescription, EcovacsDescriptionEntity as EcovacsDescriptionEntity, EventT as EventT
from .util import get_supported_entitites as get_supported_entitites
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from deebot_client.capabilities import CapabilityEvent
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Generic

@dataclass(kw_only=True, frozen=True)
class EcovacsBinarySensorEntityDescription(BinarySensorEntityDescription, EcovacsCapabilityEntityDescription, Generic[EventT]):
    value_fn: Callable[[EventT], bool | None]

ENTITY_DESCRIPTIONS: tuple[EcovacsBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: EcovacsConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EcovacsBinarySensor(EcovacsDescriptionEntity[CapabilityEvent[EventT]], BinarySensorEntity):
    entity_description: EcovacsBinarySensorEntityDescription
    _attr_is_on: Incomplete
    async def async_added_to_hass(self) -> None: ...
