from .entity import ReolinkChannelCoordinatorEntity as ReolinkChannelCoordinatorEntity, ReolinkChannelEntityDescription as ReolinkChannelEntityDescription, ReolinkHostCoordinatorEntity as ReolinkHostCoordinatorEntity, ReolinkHostEntityDescription as ReolinkHostEntityDescription
from .util import ReolinkConfigEntry as ReolinkConfigEntry, ReolinkData as ReolinkData, raise_translated_error as raise_translated_error
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.components.camera import CameraEntityFeature as CameraEntityFeature
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback, async_get_current_platform as async_get_current_platform
from reolink_aio.api import Host as Host
from typing import Any

PARALLEL_UPDATES: int
ATTR_SPEED: str
SUPPORT_PTZ_SPEED: Incomplete
SERVICE_PTZ_MOVE: str

@dataclass(frozen=True, kw_only=True)
class ReolinkButtonEntityDescription(ButtonEntityDescription, ReolinkChannelEntityDescription):
    enabled_default: Callable[[Host, int], bool] | None = ...
    method: Callable[[Host, int], Any]
    ptz_cmd: str | None = ...

@dataclass(frozen=True, kw_only=True)
class ReolinkHostButtonEntityDescription(ButtonEntityDescription, ReolinkHostEntityDescription):
    method: Callable[[Host], Any]

BUTTON_ENTITIES: Incomplete
HOST_BUTTON_ENTITIES: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ReolinkConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ReolinkButtonEntity(ReolinkChannelCoordinatorEntity, ButtonEntity):
    entity_description: ReolinkButtonEntityDescription
    _attr_entity_registry_enabled_default: Incomplete
    _attr_supported_features: Incomplete
    def __init__(self, reolink_data: ReolinkData, channel: int, entity_description: ReolinkButtonEntityDescription) -> None: ...
    @raise_translated_error
    async def async_press(self) -> None: ...
    @raise_translated_error
    async def async_ptz_move(self, **kwargs: Any) -> None: ...

class ReolinkHostButtonEntity(ReolinkHostCoordinatorEntity, ButtonEntity):
    entity_description: ReolinkHostButtonEntityDescription
    def __init__(self, reolink_data: ReolinkData, entity_description: ReolinkHostButtonEntityDescription) -> None: ...
    @raise_translated_error
    async def async_press(self) -> None: ...
