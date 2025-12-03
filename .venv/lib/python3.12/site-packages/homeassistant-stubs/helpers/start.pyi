from .typing import NoEventData as NoEventData
from collections.abc import Callable as Callable, Coroutine
from homeassistant.const import EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START, EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, CoreState as CoreState, Event as Event, HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.util.event_type import EventType as EventType
from typing import Any

@callback
def _async_at_core_state(hass: HomeAssistant, at_start_cb: Callable[[HomeAssistant], Coroutine[Any, Any, None] | None], event_type: EventType[NoEventData], check_state: Callable[[HomeAssistant], bool]) -> CALLBACK_TYPE: ...
@callback
def async_at_start(hass: HomeAssistant, at_start_cb: Callable[[HomeAssistant], Coroutine[Any, Any, None] | None]) -> CALLBACK_TYPE: ...
@callback
def async_at_started(hass: HomeAssistant, at_start_cb: Callable[[HomeAssistant], Coroutine[Any, Any, None] | None]) -> CALLBACK_TYPE: ...
