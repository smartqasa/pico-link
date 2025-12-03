from .coordinator import AndroidIPCamConfigEntry as AndroidIPCamConfigEntry, AndroidIPCamDataUpdateCoordinator as AndroidIPCamDataUpdateCoordinator
from .entity import AndroidIPCamBaseEntity as AndroidIPCamBaseEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pydroid_ipcam import PyDroidIPCam as PyDroidIPCam
from typing import Any

@dataclass(frozen=True, kw_only=True)
class AndroidIPWebcamSwitchEntityDescription(SwitchEntityDescription):
    on_func: Callable[[PyDroidIPCam], Coroutine[Any, Any, bool]]
    off_func: Callable[[PyDroidIPCam], Coroutine[Any, Any, bool]]

SWITCH_TYPES: tuple[AndroidIPWebcamSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: AndroidIPCamConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class IPWebcamSettingSwitch(AndroidIPCamBaseEntity, SwitchEntity):
    entity_description: AndroidIPWebcamSwitchEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AndroidIPCamDataUpdateCoordinator, description: AndroidIPWebcamSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
