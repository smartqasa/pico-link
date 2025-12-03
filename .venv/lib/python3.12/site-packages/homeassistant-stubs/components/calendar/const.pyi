from . import CalendarEntity as CalendarEntity
from _typeshed import Incomplete
from enum import IntFlag
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.util.hass_dict import HassKey as HassKey

DOMAIN: str
DATA_COMPONENT: HassKey[EntityComponent[CalendarEntity]]
CONF_EVENT: str

class CalendarEntityFeature(IntFlag):
    CREATE_EVENT = 1
    DELETE_EVENT = 2
    UPDATE_EVENT = 4

EVENT_UID: str
EVENT_START: str
EVENT_END: str
EVENT_SUMMARY: str
EVENT_DESCRIPTION: str
EVENT_LOCATION: str
EVENT_RECURRENCE_ID: str
EVENT_RECURRENCE_RANGE: str
EVENT_RRULE: str
EVENT_START_DATE: str
EVENT_END_DATE: str
EVENT_START_DATETIME: str
EVENT_END_DATETIME: str
EVENT_IN: str
EVENT_IN_DAYS: str
EVENT_IN_WEEKS: str
EVENT_TIME_FIELDS: Incomplete
EVENT_TYPES: str
EVENT_DURATION: str
LIST_EVENT_FIELDS: Incomplete
