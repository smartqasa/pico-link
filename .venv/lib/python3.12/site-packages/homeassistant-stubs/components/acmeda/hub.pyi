import aiopulse
import asyncio
from .const import ACMEDA_ENTITY_REMOVE as ACMEDA_ENTITY_REMOVE, ACMEDA_HUB_UPDATE as ACMEDA_HUB_UPDATE, LOGGER as LOGGER
from .helpers import update_devices as update_devices
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send

class PulseHub:
    api: aiopulse.Hub
    config_entry: Incomplete
    hass: Incomplete
    tasks: list[asyncio.Task[None]]
    current_rollers: dict[int, aiopulse.Roller]
    cleanup_callbacks: list[Callable[[], None]]
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...
    @property
    def title(self) -> str: ...
    @property
    def host(self) -> str: ...
    async def async_setup(self, tries: int = 0) -> bool: ...
    async def async_reset(self) -> bool: ...
    async def async_notify_update(self, update_type: aiopulse.UpdateType) -> None: ...
