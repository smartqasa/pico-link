import aiotractive
import asyncio
from .const import ATTR_ACTIVITY_LABEL as ATTR_ACTIVITY_LABEL, ATTR_CALORIES as ATTR_CALORIES, ATTR_DAILY_GOAL as ATTR_DAILY_GOAL, ATTR_MINUTES_ACTIVE as ATTR_MINUTES_ACTIVE, ATTR_MINUTES_DAY_SLEEP as ATTR_MINUTES_DAY_SLEEP, ATTR_MINUTES_NIGHT_SLEEP as ATTR_MINUTES_NIGHT_SLEEP, ATTR_MINUTES_REST as ATTR_MINUTES_REST, ATTR_SLEEP_LABEL as ATTR_SLEEP_LABEL, ATTR_TRACKER_STATE as ATTR_TRACKER_STATE, CLIENT_ID as CLIENT_ID, RECONNECT_INTERVAL as RECONNECT_INTERVAL, SERVER_UNAVAILABLE as SERVER_UNAVAILABLE, SWITCH_KEY_MAP as SWITCH_KEY_MAP, TRACKER_HARDWARE_STATUS_UPDATED as TRACKER_HARDWARE_STATUS_UPDATED, TRACKER_POSITION_UPDATED as TRACKER_POSITION_UPDATED, TRACKER_SWITCH_STATUS_UPDATED as TRACKER_SWITCH_STATUS_UPDATED, TRACKER_WELLNESS_STATUS_UPDATED as TRACKER_WELLNESS_STATUS_UPDATED
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_BATTERY_CHARGING as ATTR_BATTERY_CHARGING, ATTR_BATTERY_LEVEL as ATTR_BATTERY_LEVEL, CONF_EMAIL as CONF_EMAIL, CONF_PASSWORD as CONF_PASSWORD, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from typing import Any

PLATFORMS: Incomplete
_LOGGER: Incomplete

@dataclass
class Trackables:
    tracker: aiotractive.tracker.Tracker
    trackable: dict
    tracker_details: dict
    hw_info: dict
    pos_report: dict

@dataclass(slots=True)
class TractiveData:
    client: TractiveClient
    trackables: list[Trackables]
type TractiveConfigEntry = ConfigEntry[TractiveData]

async def async_setup_entry(hass: HomeAssistant, entry: TractiveConfigEntry) -> bool: ...
async def _generate_trackables(client: aiotractive.Tractive, trackable: aiotractive.trackable_object.TrackableObject) -> Trackables | None: ...
async def async_unload_entry(hass: HomeAssistant, entry: TractiveConfigEntry) -> bool: ...

class TractiveClient:
    _hass: Incomplete
    _client: Incomplete
    _user_id: Incomplete
    _last_hw_time: int
    _last_pos_time: int
    _listen_task: asyncio.Task | None
    _config_entry: Incomplete
    def __init__(self, hass: HomeAssistant, client: aiotractive.Tractive, user_id: str, config_entry: ConfigEntry) -> None: ...
    @property
    def user_id(self) -> str: ...
    @property
    def subscribed(self) -> bool: ...
    async def trackable_objects(self) -> list[aiotractive.trackable_object.TrackableObject]: ...
    def tracker(self, tracker_id: str) -> aiotractive.tracker.Tracker: ...
    def subscribe(self) -> None: ...
    async def unsubscribe(self) -> None: ...
    async def _listen(self) -> None: ...
    def _send_hardware_update(self, event: dict[str, Any]) -> None: ...
    def _send_switch_update(self, event: dict[str, Any]) -> None: ...
    def _send_wellness_update(self, event: dict[str, Any]) -> None: ...
    def _send_position_update(self, event: dict[str, Any]) -> None: ...
    def _dispatch_tracker_event(self, event_name: str, tracker_id: str, payload: dict[str, Any]) -> None: ...
