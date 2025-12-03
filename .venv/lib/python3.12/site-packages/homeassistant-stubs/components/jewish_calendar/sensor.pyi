from .entity import JewishCalendarConfigEntry as JewishCalendarConfigEntry, JewishCalendarEntity as JewishCalendarEntity
from _typeshed import Incomplete
from datetime import date as Date
from hdate import HDate
from hdate.zmanim import Zmanim
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, SUN_EVENT_SUNSET as SUN_EVENT_SUNSET
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.sun import get_astral_event_date as get_astral_event_date
from typing import Any

_LOGGER: Incomplete
INFO_SENSORS: tuple[SensorEntityDescription, ...]
TIME_SENSORS: tuple[SensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: JewishCalendarConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class JewishCalendarSensor(JewishCalendarEntity, SensorEntity):
    _attr_entity_category: Incomplete
    _attrs: dict[str, str]
    def __init__(self, config_entry: JewishCalendarConfigEntry, description: SensorEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    async def async_update(self) -> None: ...
    def make_zmanim(self, date: Date) -> Zmanim: ...
    @property
    def extra_state_attributes(self) -> dict[str, str]: ...
    _attr_options: Incomplete
    def get_state(self, daytime_date: HDate, after_shkia_date: HDate, after_tzais_date: HDate) -> Any | None: ...

class JewishCalendarTimeSensor(JewishCalendarSensor):
    _attr_device_class: Incomplete
    def get_state(self, daytime_date: HDate, after_shkia_date: HDate, after_tzais_date: HDate) -> Any | None: ...
