import asyncio
from .const import HA_MANAGED_API_PORT as HA_MANAGED_API_PORT, HA_MANAGED_URL as HA_MANAGED_URL
from _typeshed import Incomplete
from collections import deque
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

_LOGGER: Incomplete
_TERMINATE_TIMEOUT: int
_SETUP_TIMEOUT: int
_SUCCESSFUL_BOOT_MESSAGE: str
_LOCALHOST_IP: str
_LOG_BUFFER_SIZE: int
_RESPAWN_COOLDOWN: int
_GO2RTC_CONFIG_FORMAT: str
_LOG_LEVEL_MAP: Incomplete

class Go2RTCServerStartError(HomeAssistantError):
    _message: str

class Go2RTCWatchdogError(HomeAssistantError): ...

def _create_temp_file(api_ip: str) -> str: ...

class Server:
    _hass: Incomplete
    _binary: Incomplete
    _log_buffer: deque[str]
    _process: asyncio.subprocess.Process | None
    _startup_complete: Incomplete
    _api_ip: Incomplete
    _watchdog_task: asyncio.Task | None
    _watchdog_tasks: list[asyncio.Task]
    def __init__(self, hass: HomeAssistant, binary: str, *, enable_ui: bool = False) -> None: ...
    async def start(self) -> None: ...
    async def _start(self) -> None: ...
    async def _log_output(self, process: asyncio.subprocess.Process) -> None: ...
    def _log_server_output(self, loglevel: int) -> None: ...
    async def _watchdog(self) -> None: ...
    async def _monitor_process(self) -> None: ...
    async def _monitor_api(self) -> None: ...
    async def _stop_watchdog(self) -> None: ...
    async def stop(self) -> None: ...
    async def _stop(self) -> None: ...
