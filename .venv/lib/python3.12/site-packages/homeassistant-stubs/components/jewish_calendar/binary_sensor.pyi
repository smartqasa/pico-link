from .entity import JewishCalendarConfigEntry as JewishCalendarConfigEntry, JewishCalendarEntity as JewishCalendarEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from hdate.zmanim import Zmanim as Zmanim
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import event as event
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(frozen=True)
class JewishCalendarBinarySensorMixIns(BinarySensorEntityDescription):
    is_on: Callable[[Zmanim], bool] = ...

@dataclass(frozen=True)
class JewishCalendarBinarySensorEntityDescription(JewishCalendarBinarySensorMixIns, BinarySensorEntityDescription): ...

BINARY_SENSORS: tuple[JewishCalendarBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: JewishCalendarConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class JewishCalendarBinarySensor(JewishCalendarEntity, BinarySensorEntity):
    _attr_should_poll: bool
    _attr_entity_category: Incomplete
    _update_unsub: CALLBACK_TYPE | None
    entity_description: JewishCalendarBinarySensorEntityDescription
    @property
    def is_on(self) -> bool: ...
    def _get_zmanim(self) -> Zmanim: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    @callback
    def _update(self, now: datetime | None = None) -> None: ...
    def _schedule_update(self) -> None: ...
