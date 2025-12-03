import asyncio
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from async_upnp_client.aiohttp import AiohttpNotifyServer
from async_upnp_client.client import UpnpRequester as UpnpRequester
from async_upnp_client.client_factory import UpnpFactory
from async_upnp_client.event_handler import UpnpEventHandler as UpnpEventHandler
from collections import defaultdict
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HomeAssistant as HomeAssistant
from homeassistant.helpers import aiohttp_client as aiohttp_client
from typing import NamedTuple

class EventListenAddr(NamedTuple):
    host: str | None
    port: int
    callback_url: str | None

class DlnaDmrData:
    lock: asyncio.Lock
    requester: UpnpRequester
    upnp_factory: UpnpFactory
    event_notifiers: dict[EventListenAddr, AiohttpNotifyServer]
    event_notifier_refs: defaultdict[EventListenAddr, int]
    stop_listener_remove: CALLBACK_TYPE | None
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_cleanup_event_notifiers(self, event: Event) -> None: ...
    async def async_get_event_notifier(self, listen_addr: EventListenAddr, hass: HomeAssistant) -> UpnpEventHandler: ...
    async def async_release_event_notifier(self, listen_addr: EventListenAddr) -> None: ...

def get_domain_data(hass: HomeAssistant) -> DlnaDmrData: ...
