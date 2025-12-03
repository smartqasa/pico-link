from .entity import DeconzDevice as DeconzDevice
from .hub import DeconzHub as DeconzHub
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.number import DOMAIN as NUMBER_DOMAIN, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pydeconz.gateway import DeconzSession as DeconzSession
from pydeconz.interfaces.sensors import SensorResources
from pydeconz.models.event import EventType as EventType
from pydeconz.models.sensor import SensorBase as PydeconzSensorBase
from pydeconz.models.sensor.presence import Presence
from typing import Any

@dataclass(frozen=True, kw_only=True)
class DeconzNumberDescription[_T: (Presence, PydeconzSensorBase)](NumberEntityDescription):
    instance_check: type[_T]
    name_suffix: str
    set_fn: Callable[[DeconzSession, str, int], Coroutine[Any, Any, dict[str, Any]]]
    update_key: str
    value_fn: Callable[[_T], float | None]

ENTITY_DESCRIPTIONS: tuple[DeconzNumberDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DeconzNumber(DeconzDevice[SensorResources], NumberEntity):
    TYPE = NUMBER_DOMAIN
    entity_description: DeconzNumberDescription
    unique_id_suffix: Incomplete
    _name_suffix: Incomplete
    _update_key: Incomplete
    def __init__(self, device: SensorResources, hub: DeconzHub, description: DeconzNumberDescription) -> None: ...
    @property
    def native_value(self) -> float | None: ...
    async def async_set_native_value(self, value: float) -> None: ...
