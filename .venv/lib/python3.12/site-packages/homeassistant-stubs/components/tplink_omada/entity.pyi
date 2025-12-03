from .const import DOMAIN as DOMAIN
from .coordinator import OmadaCoordinator as OmadaCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from tplink_omada_client.devices import OmadaDevice as OmadaDevice
from typing import Any

class OmadaDeviceEntity[_T: OmadaCoordinator[Any]](CoordinatorEntity[_T]):
    _attr_has_entity_name: bool
    device: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: _T, device: OmadaDevice) -> None: ...
