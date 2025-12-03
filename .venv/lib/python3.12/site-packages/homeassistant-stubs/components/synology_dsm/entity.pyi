from .common import SynoApi as SynoApi
from .const import ATTRIBUTION as ATTRIBUTION, DOMAIN as DOMAIN
from .coordinator import SynologyDSMCentralUpdateCoordinator as SynologyDSMCentralUpdateCoordinator, SynologyDSMUpdateCoordinator as SynologyDSMUpdateCoordinator
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

@dataclass(frozen=True, kw_only=True)
class SynologyDSMEntityDescription(EntityDescription):
    api_key: str

class SynologyDSMBaseEntity[_CoordinatorT: SynologyDSMUpdateCoordinator[Any]](CoordinatorEntity[_CoordinatorT]):
    entity_description: SynologyDSMEntityDescription
    unique_id: str
    _attr_attribution = ATTRIBUTION
    _attr_has_entity_name: bool
    _api: Incomplete
    _attr_unique_id: str
    _attr_device_info: Incomplete
    def __init__(self, api: SynoApi, coordinator: _CoordinatorT, description: SynologyDSMEntityDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...

class SynologyDSMDeviceEntity(SynologyDSMBaseEntity[SynologyDSMCentralUpdateCoordinator]):
    _device_id: Incomplete
    _device_name: str | None
    _device_manufacturer: str | None
    _device_model: str | None
    _device_firmware: str | None
    _device_type: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, api: SynoApi, coordinator: SynologyDSMCentralUpdateCoordinator, description: SynologyDSMEntityDescription, device_id: str | None = None) -> None: ...
