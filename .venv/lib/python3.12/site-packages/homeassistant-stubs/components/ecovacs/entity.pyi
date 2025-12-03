from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from deebot_client.capabilities import Capabilities as Capabilities
from deebot_client.device import Device as Device
from deebot_client.events.base import Event
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from sucks import EventListener as EventListener, VacBot as VacBot
from typing import Any, Generic, TypeVar

CapabilityEntity = TypeVar('CapabilityEntity')
EventT = TypeVar('EventT', bound=Event)

class EcovacsEntity(Entity, Generic[CapabilityEntity]):
    _attr_should_poll: bool
    _attr_has_entity_name: bool
    _always_available: bool
    _attr_unique_id: Incomplete
    _device: Incomplete
    _capability: Incomplete
    _subscribed_events: set[type[Event]]
    def __init__(self, device: Device, capability: CapabilityEntity, **kwargs: Any) -> None: ...
    @property
    def device_info(self) -> DeviceInfo | None: ...
    _attr_available: Incomplete
    async def async_added_to_hass(self) -> None: ...
    def _subscribe(self, event_type: type[EventT], callback: Callable[[EventT], Coroutine[Any, Any, None]]) -> None: ...
    async def async_update(self) -> None: ...

class EcovacsDescriptionEntity(EcovacsEntity[CapabilityEntity]):
    entity_description: Incomplete
    def __init__(self, device: Device, capability: CapabilityEntity, entity_description: EntityDescription, **kwargs: Any) -> None: ...

@dataclass(kw_only=True, frozen=True)
class EcovacsCapabilityEntityDescription(EntityDescription, Generic[CapabilityEntity]):
    capability_fn: Callable[[Capabilities], CapabilityEntity | None]

class EcovacsLegacyEntity(Entity):
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    device: Incomplete
    error: str | None
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _event_listeners: list[EventListener]
    def __init__(self, device: VacBot) -> None: ...
    @property
    def available(self) -> bool: ...
    async def async_will_remove_from_hass(self) -> None: ...
