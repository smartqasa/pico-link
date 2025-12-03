import asyncio
import logging
from . import block_async_io as block_async_io, config_entries as config_entries, core as core, loader as loader, requirements as requirements
from .components import http as http
from .const import BASE_PLATFORMS as BASE_PLATFORMS, FORMAT_DATETIME as FORMAT_DATETIME, REQUIRED_NEXT_PYTHON_HA_RELEASE as REQUIRED_NEXT_PYTHON_HA_RELEASE, REQUIRED_NEXT_PYTHON_VER as REQUIRED_NEXT_PYTHON_VER, SIGNAL_BOOTSTRAP_INTEGRATIONS as SIGNAL_BOOTSTRAP_INTEGRATIONS
from .core_config import async_process_ha_core_config as async_process_ha_core_config
from .exceptions import HomeAssistantError as HomeAssistantError
from .helpers import area_registry as area_registry, category_registry as category_registry, device_registry as device_registry, entity as entity, entity_registry as entity_registry, floor_registry as floor_registry, issue_registry as issue_registry, label_registry as label_registry, recorder as recorder, restore_state as restore_state, template as template, translation as translation
from .helpers.dispatcher import async_dispatcher_send_internal as async_dispatcher_send_internal
from .helpers.storage import get_internal_store_manager as get_internal_store_manager
from .helpers.system_info import async_get_system_info as async_get_system_info
from .helpers.typing import ConfigType as ConfigType
from .runner import RuntimeConfig as RuntimeConfig
from .setup import _setup_started as _setup_started, async_get_setup_timings as async_get_setup_timings, async_notify_setup_error as async_notify_setup_error, async_set_domains_to_be_loaded as async_set_domains_to_be_loaded, async_setup_component as async_setup_component
from .util.async_ import create_eager_task as create_eager_task
from .util.hass_dict import HassKey as HassKey
from .util.logging import async_activate_log_queue_handler as async_activate_log_queue_handler
from .util.package import async_get_user_site as async_get_user_site, is_docker_env as is_docker_env, is_virtual_env as is_virtual_env
from .util.system_info import is_official_image as is_official_image
from _typeshed import Incomplete
from anyio._backends import _asyncio as _asyncio
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
from typing import Any

_LOGGER: Incomplete
SETUP_ORDER_SORT_KEY: Incomplete
ERROR_LOG_FILENAME: str
DATA_REGISTRIES_LOADED: HassKey[None]
LOG_SLOW_STARTUP_INTERVAL: int
SLOW_STARTUP_CHECK_INTERVAL: int
STAGE_1_TIMEOUT: int
STAGE_2_TIMEOUT: int
WRAP_UP_TIMEOUT: int
COOLDOWN_TIME: int
DEBUGGER_INTEGRATIONS: Incomplete
CORE_INTEGRATIONS: Incomplete
LOGGING_AND_HTTP_DEPS_INTEGRATIONS: Incomplete
FRONTEND_INTEGRATIONS: Incomplete
RECORDER_INTEGRATIONS: Incomplete
DISCOVERY_INTEGRATIONS: Incomplete
STAGE_1_INTEGRATIONS: Incomplete
DEFAULT_INTEGRATIONS: Incomplete
DEFAULT_INTEGRATIONS_RECOVERY_MODE: Incomplete
DEFAULT_INTEGRATIONS_SUPERVISOR: Incomplete
CRITICAL_INTEGRATIONS: Incomplete
SETUP_ORDER: Incomplete
PRELOAD_STORAGE: Incomplete

async def async_setup_hass(runtime_config: RuntimeConfig) -> core.HomeAssistant | None: ...
def open_hass_ui(hass: core.HomeAssistant) -> None: ...
def _init_blocking_io_modules_in_executor() -> None: ...
async def async_load_base_functionality(hass: core.HomeAssistant) -> None: ...
async def async_from_config_dict(config: ConfigType, hass: core.HomeAssistant) -> core.HomeAssistant | None: ...
async def async_enable_logging(hass: core.HomeAssistant, verbose: bool = False, log_rotate_days: int | None = None, log_file: str | None = None, log_no_color: bool = False) -> None: ...
def _create_log_file(err_log_path: str, log_rotate_days: int | None) -> RotatingFileHandler | TimedRotatingFileHandler: ...

class _RotatingFileHandlerWithoutShouldRollOver(RotatingFileHandler):
    def shouldRollover(self, record: logging.LogRecord) -> bool: ...

async def async_mount_local_lib_path(config_dir: str) -> str: ...
@core.callback
def _get_domains(hass: core.HomeAssistant, config: dict[str, Any]) -> set[str]: ...

class _WatchPendingSetups:
    _hass: Incomplete
    _setup_started: Incomplete
    _duration_count: int
    _handle: asyncio.TimerHandle | None
    _previous_was_empty: bool
    _loop: Incomplete
    def __init__(self, hass: core.HomeAssistant, setup_started: dict[tuple[str, str | None], float]) -> None: ...
    def _async_watch(self) -> None: ...
    def _async_dispatch(self, remaining_with_setup_started: dict[str, float]) -> None: ...
    def _async_schedule_next(self) -> None: ...
    def async_start(self) -> None: ...
    def async_stop(self) -> None: ...

async def async_setup_multi_components(hass: core.HomeAssistant, domains: set[str], config: dict[str, Any]) -> None: ...
async def _async_resolve_domains_to_setup(hass: core.HomeAssistant, config: dict[str, Any]) -> tuple[set[str], dict[str, loader.Integration]]: ...
async def _async_set_up_integrations(hass: core.HomeAssistant, config: dict[str, Any]) -> None: ...
