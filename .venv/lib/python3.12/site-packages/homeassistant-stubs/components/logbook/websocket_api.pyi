import asyncio
from .const import DOMAIN as DOMAIN
from .helpers import async_determine_event_types as async_determine_event_types, async_filter_entities as async_filter_entities, async_subscribe_events as async_subscribe_events
from .models import LogbookConfig as LogbookConfig, async_event_to_row as async_event_to_row
from .processor import EventProcessor as EventProcessor
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime as dt
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.recorder import get_instance as get_instance
from homeassistant.components.websocket_api import ActiveConnection as ActiveConnection, messages as messages
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.event import async_track_point_in_utc_time as async_track_point_in_utc_time
from homeassistant.helpers.json import json_bytes as json_bytes
from homeassistant.util.async_ import create_eager_task as create_eager_task
from typing import Any

MAX_PENDING_LOGBOOK_EVENTS: int
EVENT_COALESCE_TIME: float
BIG_QUERY_HOURS: int
BIG_QUERY_RECENT_HOURS: int
_LOGGER: Incomplete

@dataclass(slots=True)
class LogbookLiveStream:
    stream_queue: asyncio.Queue[Event]
    subscriptions: list[CALLBACK_TYPE]
    end_time_unsub: CALLBACK_TYPE | None = ...
    task: asyncio.Task | None = ...
    wait_sync_task: asyncio.Task | None = ...

@callback
def async_setup(hass: HomeAssistant) -> None: ...
@callback
def _async_send_empty_response(connection: ActiveConnection, msg_id: int, start_time: dt, end_time: dt | None) -> None: ...
async def _async_send_historical_events(hass: HomeAssistant, connection: ActiveConnection, msg_id: int, start_time: dt, end_time: dt, event_processor: EventProcessor, partial: bool, force_send: bool = False) -> dt | None: ...
async def _async_get_ws_stream_events(hass: HomeAssistant, msg_id: int, start_time: dt, end_time: dt, event_processor: EventProcessor, partial: bool) -> tuple[bytes, dt | None]: ...
def _generate_stream_message(events: list[dict[str, Any]], start_day: dt, end_day: dt) -> dict[str, Any]: ...
def _ws_stream_get_events(msg_id: int, start_day: dt, end_day: dt, event_processor: EventProcessor, partial: bool) -> tuple[bytes, dt | None]: ...
async def _async_events_consumer(subscriptions_setup_complete_time: dt, connection: ActiveConnection, msg_id: int, stream_queue: asyncio.Queue[Event], event_processor: EventProcessor) -> None: ...
@websocket_api.async_response
async def ws_event_stream(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
def _ws_formatted_get_events(msg_id: int, start_time: dt, end_time: dt, event_processor: EventProcessor) -> bytes: ...
@websocket_api.async_response
async def ws_get_events(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
