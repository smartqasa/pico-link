from . import SimpliSafe as SimpliSafe
from .const import ATTR_LAST_EVENT_INFO as ATTR_LAST_EVENT_INFO, ATTR_LAST_EVENT_SENSOR_NAME as ATTR_LAST_EVENT_SENSOR_NAME, ATTR_LAST_EVENT_SENSOR_TYPE as ATTR_LAST_EVENT_SENSOR_TYPE, ATTR_LAST_EVENT_TIMESTAMP as ATTR_LAST_EVENT_TIMESTAMP, ATTR_SYSTEM_ID as ATTR_SYSTEM_ID, DISPATCHER_TOPIC_WEBSOCKET_EVENT as DISPATCHER_TOPIC_WEBSOCKET_EVENT, DOMAIN as DOMAIN, LOGGER as LOGGER
from .typing import SystemType as SystemType
from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from simplipy.device import Device as Device
from simplipy.websocket import WebsocketEvent as WebsocketEvent

DEFAULT_CONFIG_URL: str
DEFAULT_ENTITY_MODEL: str
DEFAULT_ERROR_THRESHOLD: int
WEBSOCKET_EVENTS_REQUIRING_SERIAL: Incomplete

class SimpliSafeEntity(CoordinatorEntity[DataUpdateCoordinator[None]]):
    _attr_has_entity_name: bool
    _error_count: int
    _attr_extra_state_attributes: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    _device: Incomplete
    _online: bool
    _simplisafe: Incomplete
    _system: Incomplete
    _websocket_events_to_listen_for: Incomplete
    def __init__(self, simplisafe: SimpliSafe, system: SystemType, *, device: Device | None = None, additional_websocket_events: Iterable[str] | None = None) -> None: ...
    @property
    def available(self) -> bool: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    @callback
    def _handle_websocket_update(self, event: WebsocketEvent) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def async_increment_error_count(self) -> None: ...
    @callback
    def async_reset_error_count(self) -> None: ...
    @callback
    def async_update_from_rest_api(self) -> None: ...
    @callback
    def async_update_from_websocket_event(self, event: WebsocketEvent) -> None: ...
