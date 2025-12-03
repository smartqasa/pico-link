from .const import CONF_LOCAL_ACCESS_TOKEN as CONF_LOCAL_ACCESS_TOKEN, DOMAIN as DOMAIN
from _typeshed import Incomplete
from aiotedee import TedeeLock
from aiotedee.bridge import TedeeBridge as TedeeBridge
from collections.abc import Awaitable, Callable as Callable
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

SCAN_INTERVAL: Incomplete
GET_LOCKS_INTERVAL_SECONDS: int
_LOGGER: Incomplete
type TedeeConfigEntry = ConfigEntry[TedeeApiCoordinator]

class TedeeApiCoordinator(DataUpdateCoordinator[dict[int, TedeeLock]]):
    config_entry: TedeeConfigEntry
    bridge: TedeeBridge
    tedee_client: Incomplete
    _next_get_locks: Incomplete
    _locks_last_update: set[int]
    new_lock_callbacks: list[Callable[[int], None]]
    tedee_webhook_id: int | None
    def __init__(self, hass: HomeAssistant, entry: TedeeConfigEntry) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> dict[int, TedeeLock]: ...
    async def _async_update(self, update_fn: Callable[[], Awaitable[None]]) -> None: ...
    def webhook_received(self, message: dict[str, Any]) -> None: ...
    async def async_register_webhook(self, webhook_url: str) -> None: ...
    async def async_unregister_webhook(self) -> None: ...
    def _async_add_remove_locks(self) -> None: ...
