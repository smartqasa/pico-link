import asyncio
from .const import CONF_USE_HTTPS as CONF_USE_HTTPS, DOMAIN as DOMAIN
from .exceptions import PasswordIncompatible as PasswordIncompatible, ReolinkSetupException as ReolinkSetupException, ReolinkWebhookException as ReolinkWebhookException, UserNotAdmin as UserNotAdmin
from _typeshed import Incomplete
from aiohttp.web import Request as Request
from collections import defaultdict
from collections.abc import Mapping
from homeassistant.components import webhook as webhook
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_PROTOCOL as CONF_PROTOCOL, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.helpers.network import NoURLAvailableError as NoURLAvailableError, get_url as get_url
from homeassistant.util.ssl import SSLCipherList as SSLCipherList
from reolink_aio.api import Host
from reolink_aio.enums import SubType
from typing import Any, Literal

DEFAULT_TIMEOUT: int
FIRST_TCP_PUSH_TIMEOUT: int
FIRST_ONVIF_TIMEOUT: int
FIRST_ONVIF_LONG_POLL_TIMEOUT: int
SUBSCRIPTION_RENEW_THRESHOLD: int
POLL_INTERVAL_NO_PUSH: int
LONG_POLL_COOLDOWN: float
LONG_POLL_ERROR_COOLDOWN: int
BATTERY_WAKE_UPDATE_INTERVAL: int
_LOGGER: Incomplete

class ReolinkHost:
    _hass: HomeAssistant
    _unique_id: str
    _api: Incomplete
    last_wake: float
    update_cmd: defaultdict[str, defaultdict[int | None, int]]
    firmware_ch_list: list[int | None]
    starting: bool
    credential_errors: int
    webhook_id: str | None
    _onvif_push_supported: bool
    _onvif_long_poll_supported: bool
    _base_url: str
    _webhook_url: str
    _webhook_reachable: bool
    _long_poll_received: bool
    _long_poll_error: bool
    _cancel_poll: CALLBACK_TYPE | None
    _cancel_tcp_push_check: CALLBACK_TYPE | None
    _cancel_onvif_check: CALLBACK_TYPE | None
    _cancel_long_poll_check: CALLBACK_TYPE | None
    _poll_job: Incomplete
    _fast_poll_error: bool
    _long_poll_task: asyncio.Task | None
    _lost_subscription: bool
    def __init__(self, hass: HomeAssistant, config: Mapping[str, Any], options: Mapping[str, Any]) -> None: ...
    @callback
    def async_register_update_cmd(self, cmd: str, channel: int | None = None) -> None: ...
    @callback
    def async_unregister_update_cmd(self, cmd: str, channel: int | None = None) -> None: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def api(self) -> Host: ...
    async def async_init(self) -> None: ...
    async def _async_check_tcp_push(self, *_: Any) -> None: ...
    async def _async_check_onvif(self, *_: Any) -> None: ...
    async def _async_check_onvif_long_poll(self, *_: Any) -> None: ...
    async def update_states(self) -> None: ...
    async def disconnect(self) -> None: ...
    async def _async_start_long_polling(self, initial: bool = False) -> None: ...
    async def _async_stop_long_polling(self) -> None: ...
    async def stop(self, *_: Any) -> None: ...
    async def subscribe(self) -> None: ...
    async def renew(self) -> None: ...
    async def _renew(self, sub_type: Literal[SubType.push, SubType.long_poll]) -> None: ...
    def register_webhook(self) -> None: ...
    def unregister_webhook(self) -> None: ...
    async def _async_long_polling(self, *_: Any) -> None: ...
    async def _async_poll_all_motion(self, *_: Any) -> None: ...
    async def handle_webhook(self, hass: HomeAssistant, webhook_id: str, request: Request) -> None: ...
    async def _process_webhook_data(self, hass: HomeAssistant, webhook_id: str, data: bytes | None) -> None: ...
    def _signal_write_ha_state(self, channels: list[int] | None = None) -> None: ...
    @property
    def event_connection(self) -> str: ...
