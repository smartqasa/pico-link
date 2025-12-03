from .const import CONF_USB_PATH as CONF_USB_PATH, CONF_USB_SPHERE as CONF_USB_SPHERE, DOMAIN as DOMAIN, PLATFORMS as PLATFORMS, PROJECT_NAME as PROJECT_NAME, SSE_LISTENERS as SSE_LISTENERS, UART_LISTENERS as UART_LISTENERS
from .helpers import get_port as get_port
from .listeners import setup_sse_listeners as setup_sse_listeners, setup_uart_listeners as setup_uart_listeners
from _typeshed import Incomplete
from crownstone_cloud import CrownstoneCloud
from crownstone_sse import CrownstoneSSEAsync
from crownstone_uart import CrownstoneUart
from homeassistant.components import persistent_notification as persistent_notification
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_EMAIL as CONF_EMAIL, CONF_PASSWORD as CONF_PASSWORD, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from typing import Any

_LOGGER: Incomplete

class CrownstoneEntryManager:
    uart: CrownstoneUart | None
    cloud: CrownstoneCloud
    sse: CrownstoneSSEAsync
    hass: Incomplete
    config_entry: Incomplete
    listeners: dict[str, Any]
    usb_sphere_id: str | None
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...
    async def async_setup(self) -> bool: ...
    async def async_process_events(self, sse_client: CrownstoneSSEAsync) -> None: ...
    async def async_setup_usb(self) -> None: ...
    async def async_unload(self) -> bool: ...
    @callback
    def on_shutdown(self, _: Event) -> None: ...

async def _async_update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
