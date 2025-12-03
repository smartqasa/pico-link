from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping
from datetime import datetime
from enum import StrEnum
from homeassistant.components import websocket_api as websocket_api
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers import singleton as singleton
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util.signal_type import SignalType as SignalType
from homeassistant.util.uuid import random_uuid_hex as random_uuid_hex
from typing import Any, Final, TypedDict

DOMAIN: str
ATTR_CREATED_AT: Final[str]
ATTR_MESSAGE: Final[str]
ATTR_NOTIFICATION_ID: Final[str]
ATTR_TITLE: Final[str]
ATTR_STATUS: Final[str]

class Notification(TypedDict):
    created_at: datetime
    message: str
    notification_id: str
    title: str | None

class UpdateType(StrEnum):
    CURRENT = 'current'
    ADDED = 'added'
    REMOVED = 'removed'
    UPDATED = 'updated'

SIGNAL_PERSISTENT_NOTIFICATIONS_UPDATED: Incomplete
SCHEMA_SERVICE_NOTIFICATION: Incomplete
_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete

@callback
def async_register_callback(hass: HomeAssistant, _callback: Callable[[UpdateType, dict[str, Notification]], None]) -> CALLBACK_TYPE: ...
@bind_hass
def create(hass: HomeAssistant, message: str, title: str | None = None, notification_id: str | None = None) -> None: ...
@bind_hass
def dismiss(hass: HomeAssistant, notification_id: str) -> None: ...
@callback
@bind_hass
def async_create(hass: HomeAssistant, message: str, title: str | None = None, notification_id: str | None = None) -> None: ...
@callback
def _async_get_or_create_notifications(hass: HomeAssistant) -> dict[str, Notification]: ...
@callback
@bind_hass
def async_dismiss(hass: HomeAssistant, notification_id: str) -> None: ...
@callback
def async_dismiss_all(hass: HomeAssistant) -> None: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
@callback
def websocket_get_notifications(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: Mapping[str, Any]) -> None: ...
@callback
def _async_send_notification_update(connection: websocket_api.ActiveConnection, msg_id: int, update_type: UpdateType, notifications: dict[str, Notification]) -> None: ...
@callback
def websocket_subscribe_notifications(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: Mapping[str, Any]) -> None: ...
