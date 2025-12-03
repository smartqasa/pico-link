import asyncio
import contextlib
import contextvars
from . import core as core, loader as loader, requirements as requirements
from .const import BASE_PLATFORMS as BASE_PLATFORMS, EVENT_COMPONENT_LOADED as EVENT_COMPONENT_LOADED, EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START, PLATFORM_FORMAT as PLATFORM_FORMAT
from .core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HomeAssistant as HomeAssistant, callback as callback
from .exceptions import DependencyError as DependencyError, HomeAssistantError as HomeAssistantError
from .helpers import singleton as singleton, translation as translation
from .helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from .helpers.typing import ConfigType as ConfigType
from .util.async_ import create_eager_task as create_eager_task
from .util.hass_dict import HassKey as HassKey
from _typeshed import Incomplete
from collections import defaultdict
from collections.abc import Awaitable, Callable as Callable, Generator, Mapping
from enum import StrEnum
from types import ModuleType
from typing import Final, TypedDict

current_setup_group: contextvars.ContextVar[tuple[str, str | None] | None]
_LOGGER: Incomplete
ATTR_COMPONENT: Final[str]
DATA_SETUP: HassKey[dict[str, asyncio.Future[bool]]]
DATA_SETUP_DONE: HassKey[dict[str, asyncio.Future[bool]]]
DATA_SETUP_STARTED: HassKey[dict[tuple[str, str | None], float]]
DATA_SETUP_TIME: HassKey[defaultdict[str, defaultdict[str | None, defaultdict[SetupPhases, float]]]]
DATA_DEPS_REQS: HassKey[set[str]]
DATA_PERSISTENT_ERRORS: HassKey[dict[str, str | None]]
NOTIFY_FOR_TRANSLATION_KEYS: Incomplete
SLOW_SETUP_WARNING: int
SLOW_SETUP_MAX_WAIT: int

class EventComponentLoaded(TypedDict):
    component: str

@callback
def async_notify_setup_error(hass: HomeAssistant, component: str, display_link: str | None = None) -> None: ...
@core.callback
def async_set_domains_to_be_loaded(hass: core.HomeAssistant, domains: set[str]) -> None: ...
def setup_component(hass: core.HomeAssistant, domain: str, config: ConfigType) -> bool: ...
async def async_setup_component(hass: core.HomeAssistant, domain: str, config: ConfigType) -> bool: ...
async def _async_process_dependencies(hass: core.HomeAssistant, config: ConfigType, integration: loader.Integration) -> list[str]: ...
def _log_error_setup_error(hass: HomeAssistant, domain: str, integration: loader.Integration | None, msg: str, exc_info: Exception | None = None) -> None: ...
async def _async_setup_component(hass: core.HomeAssistant, domain: str, config: ConfigType) -> bool: ...
async def async_prepare_setup_platform(hass: core.HomeAssistant, hass_config: ConfigType, domain: str, platform_name: str) -> ModuleType | None: ...
async def async_process_deps_reqs(hass: core.HomeAssistant, config: ConfigType, integration: loader.Integration) -> None: ...
@core.callback
def async_when_setup(hass: core.HomeAssistant, component: str, when_setup_cb: Callable[[core.HomeAssistant, str], Awaitable[None]]) -> None: ...
@core.callback
def async_when_setup_or_start(hass: core.HomeAssistant, component: str, when_setup_cb: Callable[[core.HomeAssistant, str], Awaitable[None]]) -> None: ...
@core.callback
def _async_when_setup(hass: core.HomeAssistant, component: str, when_setup_cb: Callable[[core.HomeAssistant, str], Awaitable[None]], start_event: bool) -> None: ...
@core.callback
def async_get_loaded_integrations(hass: core.HomeAssistant) -> set[str]: ...

class SetupPhases(StrEnum):
    SETUP = 'setup'
    CONFIG_ENTRY_SETUP = 'config_entry_setup'
    PLATFORM_SETUP = 'platform_setup'
    CONFIG_ENTRY_PLATFORM_SETUP = 'config_entry_platform_setup'
    WAIT_BASE_PLATFORM_SETUP = 'wait_base_component'
    WAIT_IMPORT_PLATFORMS = 'wait_import_platforms'
    WAIT_IMPORT_PACKAGES = 'wait_import_packages'

def _setup_started(hass: core.HomeAssistant) -> dict[tuple[str, str | None], float]: ...
@contextlib.contextmanager
def async_pause_setup(hass: core.HomeAssistant, phase: SetupPhases) -> Generator[None]: ...
def _setup_times(hass: core.HomeAssistant) -> defaultdict[str, defaultdict[str | None, defaultdict[SetupPhases, float]]]: ...
@contextlib.contextmanager
def async_start_setup(hass: core.HomeAssistant, integration: str, phase: SetupPhases, group: str | None = None) -> Generator[None]: ...
@callback
def async_get_setup_timings(hass: core.HomeAssistant) -> dict[str, float]: ...
@callback
def async_get_domain_setup_times(hass: core.HomeAssistant, domain: str) -> Mapping[str | None, dict[SetupPhases, float]]: ...
