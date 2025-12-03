from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from hdate import Location as Location
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription

type JewishCalendarConfigEntry = ConfigEntry[JewishCalendarData]
@dataclass
class JewishCalendarData:
    language: str
    diaspora: bool
    location: Location
    candle_lighting_offset: int
    havdalah_offset: int

class JewishCalendarEntity(Entity):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _location: Incomplete
    _hebrew: Incomplete
    _language: Incomplete
    _candle_lighting_offset: Incomplete
    _havdalah_offset: Incomplete
    _diaspora: Incomplete
    def __init__(self, config_entry: JewishCalendarConfigEntry, description: EntityDescription) -> None: ...
