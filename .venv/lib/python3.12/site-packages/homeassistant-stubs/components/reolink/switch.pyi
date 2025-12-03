from .const import DOMAIN as DOMAIN
from .entity import ReolinkChannelCoordinatorEntity as ReolinkChannelCoordinatorEntity, ReolinkChannelEntityDescription as ReolinkChannelEntityDescription, ReolinkChimeCoordinatorEntity as ReolinkChimeCoordinatorEntity, ReolinkChimeEntityDescription as ReolinkChimeEntityDescription, ReolinkHostCoordinatorEntity as ReolinkHostCoordinatorEntity, ReolinkHostEntityDescription as ReolinkHostEntityDescription
from .util import ReolinkConfigEntry as ReolinkConfigEntry, ReolinkData as ReolinkData, raise_translated_error as raise_translated_error
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from reolink_aio.api import Chime as Chime, Host as Host
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class ReolinkSwitchEntityDescription(SwitchEntityDescription, ReolinkChannelEntityDescription):
    method: Callable[[Host, int, bool], Any]
    value: Callable[[Host, int], bool | None]

@dataclass(frozen=True, kw_only=True)
class ReolinkNVRSwitchEntityDescription(SwitchEntityDescription, ReolinkHostEntityDescription):
    method: Callable[[Host, bool], Any]
    value: Callable[[Host], bool]

@dataclass(frozen=True, kw_only=True)
class ReolinkChimeSwitchEntityDescription(SwitchEntityDescription, ReolinkChimeEntityDescription):
    method: Callable[[Chime, bool], Any]
    value: Callable[[Chime], bool | None]

SWITCH_ENTITIES: Incomplete
NVR_SWITCH_ENTITIES: Incomplete
CHIME_SWITCH_ENTITIES: Incomplete
DEPRECATED_HDR: Incomplete
DEPRECATED_NVR_SWITCHES: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ReolinkConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ReolinkSwitchEntity(ReolinkChannelCoordinatorEntity, SwitchEntity):
    entity_description: ReolinkSwitchEntityDescription
    def __init__(self, reolink_data: ReolinkData, channel: int, entity_description: ReolinkSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
    @raise_translated_error
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @raise_translated_error
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class ReolinkNVRSwitchEntity(ReolinkHostCoordinatorEntity, SwitchEntity):
    entity_description: ReolinkNVRSwitchEntityDescription
    def __init__(self, reolink_data: ReolinkData, entity_description: ReolinkNVRSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @raise_translated_error
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @raise_translated_error
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class ReolinkChimeSwitchEntity(ReolinkChimeCoordinatorEntity, SwitchEntity):
    entity_description: ReolinkChimeSwitchEntityDescription
    def __init__(self, reolink_data: ReolinkData, chime: Chime, entity_description: ReolinkChimeSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
    @raise_translated_error
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @raise_translated_error
    async def async_turn_off(self, **kwargs: Any) -> None: ...
