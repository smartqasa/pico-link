from . import WLEDConfigEntry as WLEDConfigEntry, WLED_KEY as WLED_KEY
from .coordinator import WLEDDataUpdateCoordinator as WLEDDataUpdateCoordinator, WLEDReleasesDataUpdateCoordinator as WLEDReleasesDataUpdateCoordinator
from .entity import WLEDEntity as WLEDEntity
from .helpers import wled_exception_handler as wled_exception_handler
from _typeshed import Incomplete
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: WLEDConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WLEDUpdateEntity(WLEDEntity, UpdateEntity):
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    _attr_title: str
    releases_coordinator: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: WLEDDataUpdateCoordinator, releases_coordinator: WLEDReleasesDataUpdateCoordinator) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def installed_version(self) -> str | None: ...
    @property
    def latest_version(self) -> str | None: ...
    @property
    def release_url(self) -> str | None: ...
    @wled_exception_handler
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...
