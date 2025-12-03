from .const import DEFAULT_TITLE as DEFAULT_TITLE, DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import WithingsActivityDataUpdateCoordinator as WithingsActivityDataUpdateCoordinator, WithingsBedPresenceDataUpdateCoordinator as WithingsBedPresenceDataUpdateCoordinator, WithingsDataUpdateCoordinator as WithingsDataUpdateCoordinator, WithingsDeviceDataUpdateCoordinator as WithingsDeviceDataUpdateCoordinator, WithingsGoalsDataUpdateCoordinator as WithingsGoalsDataUpdateCoordinator, WithingsMeasurementDataUpdateCoordinator as WithingsMeasurementDataUpdateCoordinator, WithingsSleepDataUpdateCoordinator as WithingsSleepDataUpdateCoordinator, WithingsWorkoutDataUpdateCoordinator as WithingsWorkoutDataUpdateCoordinator
from _typeshed import Incomplete
from aiohttp.web import Request as Request, Response as Response
from aiowithings import WithingsClient
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass, field
from homeassistant.components import cloud as cloud
from homeassistant.components.http import HomeAssistantView as HomeAssistantView
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_TOKEN as CONF_TOKEN, CONF_WEBHOOK_ID as CONF_WEBHOOK_ID, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.config_entry_oauth2_flow import OAuth2Session as OAuth2Session, async_get_config_entry_implementation as async_get_config_entry_implementation
from homeassistant.helpers.event import async_call_later as async_call_later
from typing import Any

PLATFORMS: Incomplete
SUBSCRIBE_DELAY: Incomplete
UNSUBSCRIBE_DELAY: Incomplete
CONF_CLOUDHOOK_URL: str
type WithingsConfigEntry = ConfigEntry[WithingsData]

@dataclass(slots=True)
class WithingsData:
    client: WithingsClient
    measurement_coordinator: WithingsMeasurementDataUpdateCoordinator
    sleep_coordinator: WithingsSleepDataUpdateCoordinator
    bed_presence_coordinator: WithingsBedPresenceDataUpdateCoordinator
    goals_coordinator: WithingsGoalsDataUpdateCoordinator
    activity_coordinator: WithingsActivityDataUpdateCoordinator
    workout_coordinator: WithingsWorkoutDataUpdateCoordinator
    device_coordinator: WithingsDeviceDataUpdateCoordinator
    coordinators: set[WithingsDataUpdateCoordinator] = field(default_factory=set)
    def __post_init__(self) -> None: ...

async def async_setup_entry(hass: HomeAssistant, entry: WithingsConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: WithingsConfigEntry) -> bool: ...
async def async_subscribe_webhooks(client: WithingsClient, webhook_url: str) -> None: ...

class WithingsWebhookManager:
    _webhooks_registered: bool
    _register_lock: Incomplete
    hass: Incomplete
    entry: Incomplete
    def __init__(self, hass: HomeAssistant, entry: WithingsConfigEntry) -> None: ...
    @property
    def withings_data(self) -> WithingsData: ...
    async def unregister_webhook(self, _: Any) -> None: ...
    async def register_webhook(self, _: Any) -> None: ...

async def async_unsubscribe_webhooks(client: WithingsClient) -> None: ...
async def _async_cloudhook_generate_url(hass: HomeAssistant, entry: WithingsConfigEntry) -> str: ...
async def async_remove_entry(hass: HomeAssistant, entry: WithingsConfigEntry) -> None: ...
def json_message_response(message: str, message_code: int) -> Response: ...
def get_webhook_handler(withings_data: WithingsData) -> Callable[[HomeAssistant, str, Request], Awaitable[Response | None]]: ...
