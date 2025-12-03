from . import DevoloHomeNetworkConfigEntry as DevoloHomeNetworkConfigEntry
from .const import DOMAIN as DOMAIN, REGULAR_FIRMWARE as REGULAR_FIRMWARE
from .coordinator import DevoloDataUpdateCoordinator as DevoloDataUpdateCoordinator
from .entity import DevoloCoordinatorEntity as DevoloCoordinatorEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from devolo_plc_api.device import Device as Device
from devolo_plc_api.device_api import UpdateFirmwareCheck as UpdateFirmwareCheck
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class DevoloUpdateEntityDescription(UpdateEntityDescription):
    latest_version: Callable[[UpdateFirmwareCheck], str]
    update_func: Callable[[Device], Awaitable[bool]]

UPDATE_TYPES: dict[str, DevoloUpdateEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: DevoloHomeNetworkConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DevoloUpdateEntity(DevoloCoordinatorEntity, UpdateEntity):
    _attr_supported_features: Incomplete
    entity_description: DevoloUpdateEntityDescription
    _in_progress_old_version: str | None
    def __init__(self, entry: DevoloHomeNetworkConfigEntry, coordinator: DevoloDataUpdateCoordinator, description: DevoloUpdateEntityDescription) -> None: ...
    @property
    def installed_version(self) -> str: ...
    @property
    def latest_version(self) -> str: ...
    @property
    def in_progress(self) -> bool: ...
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...
