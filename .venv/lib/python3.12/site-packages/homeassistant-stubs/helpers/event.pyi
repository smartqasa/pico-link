import asyncio
import time
from . import frame as frame
from .device_registry import EVENT_DEVICE_REGISTRY_UPDATED as EVENT_DEVICE_REGISTRY_UPDATED, EventDeviceRegistryUpdatedData as EventDeviceRegistryUpdatedData
from .entity_registry import EVENT_ENTITY_REGISTRY_UPDATED as EVENT_ENTITY_REGISTRY_UPDATED, EventEntityRegistryUpdatedData as EventEntityRegistryUpdatedData
from .ratelimit import KeyedRateLimit as KeyedRateLimit
from .sun import get_astral_event_next as get_astral_event_next
from .template import RenderInfo as RenderInfo, Template as Template, result_as_boolean as result_as_boolean
from .typing import TemplateVarsType as TemplateVarsType
from _typeshed import Incomplete
from collections import defaultdict
from collections.abc import Callable, Coroutine, Iterable, Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime, timedelta
from homeassistant.const import EVENT_CORE_CONFIG_UPDATE as EVENT_CORE_CONFIG_UPDATE, EVENT_STATE_CHANGED as EVENT_STATE_CHANGED, EVENT_STATE_REPORTED as EVENT_STATE_REPORTED, MATCH_ALL as MATCH_ALL, SUN_EVENT_SUNRISE as SUN_EVENT_SUNRISE, SUN_EVENT_SUNSET as SUN_EVENT_SUNSET
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, EventStateChangedData as EventStateChangedData, EventStateEventData as EventStateEventData, EventStateReportedData as EventStateReportedData, HassJob as HassJob, HassJobType as HassJobType, HomeAssistant as HomeAssistant, State as State, callback as callback, split_entity_id as split_entity_id
from homeassistant.exceptions import TemplateError as TemplateError
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util.async_ import run_callback_threadsafe as run_callback_threadsafe
from homeassistant.util.event_type import EventType as EventType
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Any, Concatenate, Generic, TypeVar

_TRACK_STATE_CHANGE_DATA: HassKey[_KeyedEventData[EventStateChangedData]]
_TRACK_STATE_REPORT_DATA: HassKey[_KeyedEventData[EventStateReportedData]]
_TRACK_STATE_ADDED_DOMAIN_DATA: HassKey[_KeyedEventData[EventStateChangedData]]
_TRACK_STATE_REMOVED_DOMAIN_DATA: HassKey[_KeyedEventData[EventStateChangedData]]
_TRACK_ENTITY_REGISTRY_UPDATED_DATA: HassKey[_KeyedEventData[EventEntityRegistryUpdatedData]]
_TRACK_DEVICE_REGISTRY_UPDATED_DATA: HassKey[_KeyedEventData[EventDeviceRegistryUpdatedData]]
_ALL_LISTENER: str
_DOMAINS_LISTENER: str
_ENTITIES_LISTENER: str
_LOGGER: Incomplete
RANDOM_MICROSECOND_MIN: int
RANDOM_MICROSECOND_MAX: int
_TypedDictT = TypeVar('_TypedDictT', bound=Mapping[str, Any])

@dataclass(slots=True, frozen=True)
class _KeyedEventTracker(Generic[_TypedDictT]):
    key: HassKey[_KeyedEventData[_TypedDictT]]
    event_type: EventType[_TypedDictT] | str
    dispatcher_callable: Callable[[HomeAssistant, dict[str, list[HassJob[[Event[_TypedDictT]], Any]]], Event[_TypedDictT]], None]
    filter_callable: Callable[[HomeAssistant, dict[str, list[HassJob[[Event[_TypedDictT]], Any]]], _TypedDictT], bool]

@dataclass(slots=True, frozen=True)
class _KeyedEventData(Generic[_TypedDictT]):
    listener: CALLBACK_TYPE
    callbacks: defaultdict[str, list[HassJob[[Event[_TypedDictT]], Any]]]

@dataclass(slots=True)
class TrackStates:
    all_states: bool
    entities: set[str]
    domains: set[str]

@dataclass(slots=True)
class TrackTemplate:
    template: Template
    variables: TemplateVarsType
    rate_limit: float | None = ...

@dataclass(slots=True)
class TrackTemplateResult:
    template: Template
    last_result: Any
    result: Any

def threaded_listener_factory[**_P](async_factory: Callable[Concatenate[HomeAssistant, _P], Any]) -> Callable[Concatenate[HomeAssistant, _P], CALLBACK_TYPE]: ...
@callback
@bind_hass
def async_track_state_change(hass: HomeAssistant, entity_ids: str | Iterable[str], action: Callable[[str, State | None, State | None], Coroutine[Any, Any, None] | None], from_state: str | Iterable[str] | None = None, to_state: str | Iterable[str] | None = None) -> CALLBACK_TYPE: ...

track_state_change: Incomplete

@bind_hass
def async_track_state_change_event(hass: HomeAssistant, entity_ids: str | Iterable[str], action: Callable[[Event[EventStateChangedData]], Any], job_type: HassJobType | None = None) -> CALLBACK_TYPE: ...
@callback
def _async_dispatch_entity_id_event_soon[_StateEventDataT: EventStateEventData](hass: HomeAssistant, callbacks: dict[str, list[HassJob[[Event[_StateEventDataT]], Any]]], event: Event[_StateEventDataT]) -> None: ...
@callback
def _async_dispatch_entity_id_event[_StateEventDataT: EventStateEventData](hass: HomeAssistant, callbacks: dict[str, list[HassJob[[Event[_StateEventDataT]], Any]]], event: Event[_StateEventDataT]) -> None: ...
@callback
def _async_state_filter[_StateEventDataT: EventStateEventData](hass: HomeAssistant, callbacks: dict[str, list[HassJob[[Event[_StateEventDataT]], Any]]], event_data: _StateEventDataT) -> bool: ...

_KEYED_TRACK_STATE_CHANGE: Incomplete

@bind_hass
def _async_track_state_change_event(hass: HomeAssistant, entity_ids: str | Iterable[str], action: Callable[[Event[EventStateChangedData]], Any], job_type: HassJobType | None) -> CALLBACK_TYPE: ...

_KEYED_TRACK_STATE_REPORT: Incomplete

def async_track_state_report_event(hass: HomeAssistant, entity_ids: str | Iterable[str], action: Callable[[Event[EventStateReportedData]], Any], job_type: HassJobType | None = None) -> CALLBACK_TYPE: ...
@callback
def _remove_empty_listener() -> None: ...
@callback
def _remove_listener(hass: HomeAssistant, tracker: _KeyedEventTracker[_TypedDictT], keys: Iterable[str], job: HassJob[[Event[_TypedDictT]], Any], callbacks: dict[str, list[HassJob[[Event[_TypedDictT]], Any]]]) -> None: ...
def _async_track_event(tracker: _KeyedEventTracker[_TypedDictT], hass: HomeAssistant, keys: str | Iterable[str], action: Callable[[Event[_TypedDictT]], None], job_type: HassJobType | None) -> CALLBACK_TYPE: ...
@callback
def _async_dispatch_old_entity_id_or_entity_id_event(hass: HomeAssistant, callbacks: dict[str, list[HassJob[[Event[EventEntityRegistryUpdatedData]], Any]]], event: Event[EventEntityRegistryUpdatedData]) -> None: ...
@callback
def _async_entity_registry_updated_filter(hass: HomeAssistant, callbacks: dict[str, list[HassJob[[Event[EventEntityRegistryUpdatedData]], Any]]], event_data: EventEntityRegistryUpdatedData) -> bool: ...

_KEYED_TRACK_ENTITY_REGISTRY_UPDATED: Incomplete

@bind_hass
@callback
def async_track_entity_registry_updated_event(hass: HomeAssistant, entity_ids: str | Iterable[str], action: Callable[[Event[EventEntityRegistryUpdatedData]], Any], job_type: HassJobType | None = None) -> CALLBACK_TYPE: ...
@callback
def _async_device_registry_updated_filter(hass: HomeAssistant, callbacks: dict[str, list[HassJob[[Event[EventDeviceRegistryUpdatedData]], Any]]], event_data: EventDeviceRegistryUpdatedData) -> bool: ...
@callback
def _async_dispatch_device_id_event(hass: HomeAssistant, callbacks: dict[str, list[HassJob[[Event[EventDeviceRegistryUpdatedData]], Any]]], event: Event[EventDeviceRegistryUpdatedData]) -> None: ...

_KEYED_TRACK_DEVICE_REGISTRY_UPDATED: Incomplete

@callback
def async_track_device_registry_updated_event(hass: HomeAssistant, device_ids: str | Iterable[str], action: Callable[[Event[EventDeviceRegistryUpdatedData]], Any], job_type: HassJobType | None = None) -> CALLBACK_TYPE: ...
@callback
def _async_dispatch_domain_event(hass: HomeAssistant, callbacks: dict[str, list[HassJob[[Event[EventStateChangedData]], Any]]], event: Event[EventStateChangedData]) -> None: ...
@callback
def _async_domain_added_filter(hass: HomeAssistant, callbacks: dict[str, list[HassJob[[Event[EventStateChangedData]], Any]]], event_data: EventStateChangedData) -> bool: ...
@bind_hass
def async_track_state_added_domain(hass: HomeAssistant, domains: str | Iterable[str], action: Callable[[Event[EventStateChangedData]], Any], job_type: HassJobType | None = None) -> CALLBACK_TYPE: ...

_KEYED_TRACK_STATE_ADDED_DOMAIN: Incomplete

@bind_hass
def _async_track_state_added_domain(hass: HomeAssistant, domains: str | Iterable[str], action: Callable[[Event[EventStateChangedData]], Any], job_type: HassJobType | None) -> CALLBACK_TYPE: ...
@callback
def _async_domain_removed_filter(hass: HomeAssistant, callbacks: dict[str, list[HassJob[[Event[EventStateChangedData]], Any]]], event_data: EventStateChangedData) -> bool: ...

_KEYED_TRACK_STATE_REMOVED_DOMAIN: Incomplete

@bind_hass
def async_track_state_removed_domain(hass: HomeAssistant, domains: str | Iterable[str], action: Callable[[Event[EventStateChangedData]], Any], job_type: HassJobType | None = None) -> CALLBACK_TYPE: ...
@callback
def _async_string_to_lower_list(instr: str | Iterable[str]) -> list[str]: ...

class _TrackStateChangeFiltered:
    hass: Incomplete
    _action: Incomplete
    _action_as_hassjob: Incomplete
    _listeners: dict[str, Callable[[], None]]
    _last_track_states: TrackStates
    def __init__(self, hass: HomeAssistant, track_states: TrackStates, action: Callable[[Event[EventStateChangedData]], Any]) -> None: ...
    @callback
    def async_setup(self) -> None: ...
    @property
    def listeners(self) -> dict[str, bool | set[str]]: ...
    @callback
    def async_update_listeners(self, new_track_states: TrackStates) -> None: ...
    @callback
    def async_remove(self) -> None: ...
    @callback
    def _cancel_listener(self, listener_name: str) -> None: ...
    @callback
    def _setup_entities_listener(self, domains: set[str], entities: set[str]) -> None: ...
    @callback
    def _state_added(self, event: Event[EventStateChangedData]) -> None: ...
    @callback
    def _setup_domains_listener(self, domains: set[str]) -> None: ...
    @callback
    def _setup_all_listener(self) -> None: ...

@callback
@bind_hass
def async_track_state_change_filtered(hass: HomeAssistant, track_states: TrackStates, action: Callable[[Event[EventStateChangedData]], Any]) -> _TrackStateChangeFiltered: ...
@callback
@bind_hass
def async_track_template(hass: HomeAssistant, template: Template, action: Callable[[str, State | None, State | None], Coroutine[Any, Any, None] | None], variables: TemplateVarsType | None = None) -> CALLBACK_TYPE: ...

track_template: Incomplete

class TrackTemplateResultInfo:
    hass: Incomplete
    _job: Incomplete
    _track_templates: Incomplete
    _has_super_template: Incomplete
    _last_result: dict[Template, bool | str | TemplateError]
    _rate_limit: Incomplete
    _info: dict[Template, RenderInfo]
    _track_state_changes: _TrackStateChangeFiltered | None
    _time_listeners: dict[Template, Callable[[], None]]
    def __init__(self, hass: HomeAssistant, track_templates: Sequence[TrackTemplate], action: TrackTemplateResultListener, has_super_template: bool = False) -> None: ...
    def __repr__(self) -> str: ...
    def async_setup(self, strict: bool = False, log_fn: Callable[[int, str], None] | None = None) -> None: ...
    @property
    def listeners(self) -> dict[str, bool | set[str]]: ...
    @callback
    def _setup_time_listener(self, template: Template, has_time: bool) -> None: ...
    @callback
    def _update_time_listeners(self) -> None: ...
    @callback
    def async_remove(self) -> None: ...
    @callback
    def async_refresh(self) -> None: ...
    def _render_template_if_ready(self, track_template_: TrackTemplate, now: float, event: Event[EventStateChangedData] | None) -> bool | TrackTemplateResult: ...
    @staticmethod
    def _super_template_as_boolean(result: bool | str | TemplateError) -> bool: ...
    @callback
    def _apply_update(self, updates: list[TrackTemplateResult], update: bool | TrackTemplateResult, template: Template) -> bool: ...
    @callback
    def _refresh(self, event: Event[EventStateChangedData] | None, track_templates: Iterable[TrackTemplate] | None = None, replayed: bool | None = False) -> None: ...
type TrackTemplateResultListener = Callable[[Event[EventStateChangedData] | None, list[TrackTemplateResult]], Coroutine[Any, Any, None] | None]

@callback
@bind_hass
def async_track_template_result(hass: HomeAssistant, track_templates: Sequence[TrackTemplate], action: TrackTemplateResultListener, strict: bool = False, log_fn: Callable[[int, str], None] | None = None, has_super_template: bool = False) -> TrackTemplateResultInfo: ...
@callback
@bind_hass
def async_track_same_state(hass: HomeAssistant, period: timedelta, action: Callable[[], Coroutine[Any, Any, None] | None], async_check_same_func: Callable[[str, State | None, State | None], bool], entity_ids: str | Iterable[str] = ...) -> CALLBACK_TYPE: ...

track_same_state: Incomplete

@callback
@bind_hass
def async_track_point_in_time(hass: HomeAssistant, action: HassJob[[datetime], Coroutine[Any, Any, None] | None] | Callable[[datetime], Coroutine[Any, Any, None] | None], point_in_time: datetime) -> CALLBACK_TYPE: ...

track_point_in_time: Incomplete

@dataclass(slots=True)
class _TrackPointUTCTime:
    hass: HomeAssistant
    job: HassJob[[datetime], Coroutine[Any, Any, None] | None]
    utc_point_in_time: datetime
    expected_fire_timestamp: float
    _cancel_callback: asyncio.TimerHandle | None = ...
    def async_attach(self) -> None: ...
    @callback
    def __call__(self) -> None: ...
    @callback
    def async_cancel(self) -> None: ...

@callback
@bind_hass
def async_track_point_in_utc_time(hass: HomeAssistant, action: HassJob[[datetime], Coroutine[Any, Any, None] | None] | Callable[[datetime], Coroutine[Any, Any, None] | None], point_in_time: datetime) -> CALLBACK_TYPE: ...

track_point_in_utc_time: Incomplete

def _run_async_call_action(hass: HomeAssistant, job: HassJob[[datetime], Coroutine[Any, Any, None] | None]) -> None: ...
@callback
@bind_hass
def async_call_at(hass: HomeAssistant, action: HassJob[[datetime], Coroutine[Any, Any, None] | None] | Callable[[datetime], Coroutine[Any, Any, None] | None], loop_time: float) -> CALLBACK_TYPE: ...
@callback
@bind_hass
def async_call_later(hass: HomeAssistant, delay: float | timedelta, action: HassJob[[datetime], Coroutine[Any, Any, None] | None] | Callable[[datetime], Coroutine[Any, Any, None] | None]) -> CALLBACK_TYPE: ...

call_later: Incomplete

@dataclass(slots=True)
class _TrackTimeInterval:
    hass: HomeAssistant
    seconds: float
    job_name: str
    action: Callable[[datetime], Coroutine[Any, Any, None] | None]
    cancel_on_shutdown: bool | None
    _track_job: HassJob[[datetime], Coroutine[Any, Any, None] | None] | None = ...
    _run_job: HassJob[[datetime], Coroutine[Any, Any, None] | None] | None = ...
    _timer_handle: asyncio.TimerHandle | None = ...
    def async_attach(self) -> None: ...
    def _schedule_timer(self) -> None: ...
    @callback
    def _interval_listener(self, _: Any) -> None: ...
    @callback
    def async_cancel(self) -> None: ...

@callback
@bind_hass
def async_track_time_interval(hass: HomeAssistant, action: Callable[[datetime], Coroutine[Any, Any, None] | None], interval: timedelta, *, name: str | None = None, cancel_on_shutdown: bool | None = None) -> CALLBACK_TYPE: ...

track_time_interval: Incomplete

@dataclass(slots=True)
class SunListener:
    hass: HomeAssistant
    job: HassJob[[], Coroutine[Any, Any, None] | None]
    event: str
    offset: timedelta | None
    _unsub_sun: CALLBACK_TYPE | None = ...
    _unsub_config: CALLBACK_TYPE | None = ...
    @callback
    def async_attach(self) -> None: ...
    @callback
    def async_detach(self) -> None: ...
    @callback
    def _listen_next_sun_event(self) -> None: ...
    @callback
    def _handle_sun_event(self, _now: Any) -> None: ...
    @callback
    def _handle_config_event(self, _event: Any) -> None: ...

@callback
@bind_hass
def async_track_sunrise(hass: HomeAssistant, action: Callable[[], None], offset: timedelta | None = None) -> CALLBACK_TYPE: ...

track_sunrise: Incomplete

@callback
@bind_hass
def async_track_sunset(hass: HomeAssistant, action: Callable[[], None], offset: timedelta | None = None) -> CALLBACK_TYPE: ...

track_sunset: Incomplete
time_tracker_utcnow: Incomplete
time_tracker_timestamp = time.time

@dataclass(slots=True)
class _TrackUTCTimeChange:
    hass: HomeAssistant
    time_match_expression: tuple[list[int], list[int], list[int]]
    microsecond: int
    local: bool
    job: HassJob[[datetime], Coroutine[Any, Any, None] | None]
    listener_job_name: str
    _pattern_time_change_listener_job: HassJob[[datetime], None] | None = ...
    _cancel_callback: CALLBACK_TYPE | None = ...
    def async_attach(self) -> None: ...
    def _calculate_next(self, utc_now: datetime) -> datetime: ...
    @callback
    def _pattern_time_change_listener(self, _: datetime) -> None: ...
    @callback
    def async_cancel(self) -> None: ...

@callback
@bind_hass
def async_track_utc_time_change(hass: HomeAssistant, action: Callable[[datetime], Coroutine[Any, Any, None] | None], hour: Any | None = None, minute: Any | None = None, second: Any | None = None, local: bool = False) -> CALLBACK_TYPE: ...

track_utc_time_change: Incomplete

@callback
@bind_hass
def async_track_time_change(hass: HomeAssistant, action: Callable[[datetime], Coroutine[Any, Any, None] | None], hour: Any | None = None, minute: Any | None = None, second: Any | None = None) -> CALLBACK_TYPE: ...

track_time_change: Incomplete

def process_state_match(parameter: str | Iterable[str] | None, invert: bool = False) -> Callable[[str | None], bool]: ...
@callback
def _entities_domains_from_render_infos(render_infos: Iterable[RenderInfo]) -> tuple[set[str], set[str]]: ...
@callback
def _render_infos_needs_all_listener(render_infos: Iterable[RenderInfo]) -> bool: ...
@callback
def _render_infos_to_track_states(render_infos: Iterable[RenderInfo]) -> TrackStates: ...
@callback
def _event_triggers_rerender(event: Event[EventStateChangedData], info: RenderInfo) -> bool: ...
@callback
def _rate_limit_for_event(event: Event[EventStateChangedData], info: RenderInfo, track_template_: TrackTemplate) -> float | None: ...
def _suppress_domain_all_in_render_info(render_info: RenderInfo) -> RenderInfo: ...
