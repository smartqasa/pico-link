from .const import DOMAIN as DOMAIN
from .coordinator import EnphaseConfigEntry as EnphaseConfigEntry, EnphaseUpdateCoordinator as EnphaseUpdateCoordinator
from .entity import EnvoyBaseEntity as EnvoyBaseEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyenphase import Envoy as Envoy, EnvoyDryContactStatus as EnvoyDryContactStatus, EnvoyEnpower as EnvoyEnpower
from pyenphase.models.tariff import EnvoyStorageSettings as EnvoyStorageSettings
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class EnvoyEnpowerSwitchEntityDescription(SwitchEntityDescription):
    value_fn: Callable[[EnvoyEnpower], bool]
    turn_on_fn: Callable[[Envoy], Coroutine[Any, Any, dict[str, Any]]]
    turn_off_fn: Callable[[Envoy], Coroutine[Any, Any, dict[str, Any]]]

@dataclass(frozen=True, kw_only=True)
class EnvoyDryContactSwitchEntityDescription(SwitchEntityDescription):
    value_fn: Callable[[EnvoyDryContactStatus], bool]
    turn_on_fn: Callable[[Envoy, str], Coroutine[Any, Any, dict[str, Any]]]
    turn_off_fn: Callable[[Envoy, str], Coroutine[Any, Any, dict[str, Any]]]

@dataclass(frozen=True, kw_only=True)
class EnvoyStorageSettingsSwitchEntityDescription(SwitchEntityDescription):
    value_fn: Callable[[EnvoyStorageSettings], bool]
    turn_on_fn: Callable[[Envoy], Awaitable[dict[str, Any]]]
    turn_off_fn: Callable[[Envoy], Awaitable[dict[str, Any]]]

ENPOWER_GRID_SWITCH: Incomplete
RELAY_STATE_SWITCH: Incomplete
CHARGE_FROM_GRID_SWITCH: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: EnphaseConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EnvoyEnpowerSwitchEntity(EnvoyBaseEntity, SwitchEntity):
    entity_description: EnvoyEnpowerSwitchEntityDescription
    envoy: Incomplete
    enpower: Incomplete
    _serial_number: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: EnphaseUpdateCoordinator, description: EnvoyEnpowerSwitchEntityDescription, enpower: EnvoyEnpower) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class EnvoyDryContactSwitchEntity(EnvoyBaseEntity, SwitchEntity):
    entity_description: EnvoyDryContactSwitchEntityDescription
    _attr_name: Incomplete
    envoy: Incomplete
    relay_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: EnphaseUpdateCoordinator, description: EnvoyDryContactSwitchEntityDescription, relay_id: str) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class EnvoyStorageSettingsSwitchEntity(EnvoyBaseEntity, SwitchEntity):
    entity_description: EnvoyStorageSettingsSwitchEntityDescription
    envoy: Incomplete
    enpower: Incomplete
    _serial_number: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: EnphaseUpdateCoordinator, description: EnvoyStorageSettingsSwitchEntityDescription, enpower: EnvoyEnpower | None) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
