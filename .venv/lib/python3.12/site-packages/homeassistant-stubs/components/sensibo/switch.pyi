from . import SensiboConfigEntry as SensiboConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import SensiboDataUpdateCoordinator as SensiboDataUpdateCoordinator
from .entity import SensiboDeviceBaseEntity as SensiboDeviceBaseEntity, async_handle_api_call as async_handle_api_call
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping
from dataclasses import dataclass
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pysensibo.model import SensiboDevice as SensiboDevice
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class SensiboDeviceSwitchEntityDescription(SwitchEntityDescription):
    value_fn: Callable[[SensiboDevice], bool | None]
    extra_fn: Callable[[SensiboDevice], dict[str, str | bool | None]] | None
    command_on: str
    command_off: str
    data_key: str

DEVICE_SWITCH_TYPES: tuple[SensiboDeviceSwitchEntityDescription, ...]
PURE_SWITCH_TYPES: tuple[SensiboDeviceSwitchEntityDescription, ...]
DESCRIPTION_BY_MODELS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: SensiboConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SensiboDeviceSwitch(SensiboDeviceBaseEntity, SwitchEntity):
    entity_description: SensiboDeviceSwitchEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SensiboDataUpdateCoordinator, device_id: str, entity_description: SensiboDeviceSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any] | None: ...
    @async_handle_api_call
    async def async_turn_on_timer(self, key: str, value: bool) -> bool: ...
    @async_handle_api_call
    async def async_turn_off_timer(self, key: str, value: bool) -> bool: ...
    @async_handle_api_call
    async def async_turn_on_off_pure_boost(self, key: str, value: bool) -> bool: ...
    @async_handle_api_call
    async def async_turn_on_off_smart(self, key: str, value: bool) -> bool: ...
