import asyncio
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.const import EVENT_COMPONENT_LOADED as EVENT_COMPONENT_LOADED
from homeassistant.core import Event as Event, HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.loader import Integration as Integration, async_get_integrations as async_get_integrations, async_get_loaded_integration as async_get_loaded_integration, async_register_preload_platform as async_register_preload_platform, bind_hass as bind_hass
from homeassistant.setup import ATTR_COMPONENT as ATTR_COMPONENT, EventComponentLoaded as EventComponentLoaded
from homeassistant.util.hass_dict import HassKey as HassKey
from homeassistant.util.logging import catch_log_exception as catch_log_exception
from types import ModuleType
from typing import Any

_LOGGER: Incomplete
DATA_INTEGRATION_PLATFORMS: HassKey[list[IntegrationPlatform]]

@dataclass(slots=True, frozen=True)
class IntegrationPlatform:
    platform_name: str
    process_job: HassJob[[HomeAssistant, str, Any], Awaitable[None] | None]
    seen_components: set[str]

@callback
def _async_integration_platform_component_loaded(hass: HomeAssistant, integration_platforms: list[IntegrationPlatform], event: Event[EventComponentLoaded]) -> None: ...
async def _async_process_integration_platforms_for_component(hass: HomeAssistant, integration: Integration, platforms_that_exist: list[str], integration_platforms_by_name: dict[str, IntegrationPlatform]) -> None: ...
@callback
def _process_integration_platforms(hass: HomeAssistant, integration: Integration, platforms: dict[str, ModuleType], integration_platforms_by_name: dict[str, IntegrationPlatform]) -> list[asyncio.Future[Awaitable[None] | None]]: ...
def _format_err(name: str, platform_name: str, *args: Any) -> str: ...
@bind_hass
async def async_process_integration_platforms(hass: HomeAssistant, platform_name: str, process_platform: Callable[[HomeAssistant, str, Any], Awaitable[None] | None], wait_for_platforms: bool = False) -> None: ...
async def _async_process_integration_platforms(hass: HomeAssistant, platform_name: str, top_level_components: set[str], process_job: HassJob) -> None: ...
