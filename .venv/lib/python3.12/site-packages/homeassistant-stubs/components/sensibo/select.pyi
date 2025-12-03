from . import SensiboConfigEntry as SensiboConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import SensiboDataUpdateCoordinator as SensiboDataUpdateCoordinator
from .entity import SensiboDeviceBaseEntity as SensiboDeviceBaseEntity, async_handle_api_call as async_handle_api_call
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pysensibo.model import SensiboDevice as SensiboDevice
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class SensiboSelectEntityDescription(SelectEntityDescription):
    data_key: str
    value_fn: Callable[[SensiboDevice], str | None]
    options_fn: Callable[[SensiboDevice], list[str] | None]
    transformation: Callable[[SensiboDevice], dict | None]

DEVICE_SELECT_TYPES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: SensiboConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SensiboSelect(SensiboDeviceBaseEntity, SelectEntity):
    entity_description: SensiboSelectEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SensiboDataUpdateCoordinator, device_id: str, entity_description: SensiboSelectEntityDescription) -> None: ...
    @property
    def current_option(self) -> str | None: ...
    @property
    def options(self) -> list[str]: ...
    async def async_select_option(self, option: str) -> None: ...
    @async_handle_api_call
    async def async_send_api_call(self, key: str, value: Any) -> bool: ...
