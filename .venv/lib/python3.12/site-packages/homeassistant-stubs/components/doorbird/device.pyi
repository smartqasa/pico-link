from .const import API_URL as API_URL, DEFAULT_EVENT_TYPES as DEFAULT_EVENT_TYPES, HTTP_EVENT_TYPE as HTTP_EVENT_TYPE, MAX_WEEKDAY as MAX_WEEKDAY, MIN_WEEKDAY as MIN_WEEKDAY
from _typeshed import Incomplete
from collections import defaultdict
from dataclasses import dataclass
from doorbirdpy import DoorBird as DoorBird, DoorBirdScheduleEntry as DoorBirdScheduleEntry
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.network import get_url as get_url
from homeassistant.util import slugify as slugify
from propcache import cached_property
from typing import Any

_LOGGER: Incomplete

@dataclass(slots=True)
class DoorbirdEvent:
    event: str
    event_type: str

@dataclass(slots=True)
class DoorbirdEventConfig:
    events: list[DoorbirdEvent]
    schedule: list[DoorBirdScheduleEntry]
    unconfigured_favorites: defaultdict[str, list[str]]

class ConfiguredDoorBird:
    _hass: Incomplete
    _name: Incomplete
    _device: Incomplete
    _custom_url: Incomplete
    _token: Incomplete
    _event_entity_ids: Incomplete
    events: list[str]
    door_station_events: list[str]
    event_descriptions: list[DoorbirdEvent]
    def __init__(self, hass: HomeAssistant, device: DoorBird, name: str | None, custom_url: str | None, token: str, event_entity_ids: dict[str, str]) -> None: ...
    def update_events(self, events: list[str]) -> None: ...
    @cached_property
    def name(self) -> str | None: ...
    @cached_property
    def device(self) -> DoorBird: ...
    @cached_property
    def custom_url(self) -> str | None: ...
    @cached_property
    def token(self) -> str: ...
    async def async_register_events(self) -> None: ...
    async def _configure_unconfigured_favorites(self, event_config: DoorbirdEventConfig) -> None: ...
    async def _async_register_events(self) -> dict[str, Any]: ...
    async def _async_get_event_config(self, http_fav: dict[str, dict[str, Any]]) -> DoorbirdEventConfig: ...
    @cached_property
    def slug(self) -> str: ...
    def _get_event_name(self, event: str) -> str: ...
    async def _async_get_http_favorites(self) -> dict[str, dict[str, Any]]: ...
    async def _async_register_event(self, hass_url: str, event: str, http_fav: dict[str, dict[str, Any]]) -> bool: ...
    def get_event_data(self, event: str) -> dict[str, str | None]: ...

async def async_reset_device_favorites(door_station: ConfiguredDoorBird) -> None: ...
