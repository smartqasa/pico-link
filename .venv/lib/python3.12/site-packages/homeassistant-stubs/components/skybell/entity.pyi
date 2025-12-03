from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from .coordinator import SkybellDataUpdateCoordinator as SkybellDataUpdateCoordinator
from _typeshed import Incomplete
from aioskybell import SkybellDevice as SkybellDevice
from homeassistant.const import ATTR_CONNECTIONS as ATTR_CONNECTIONS
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class SkybellEntity(CoordinatorEntity[SkybellDataUpdateCoordinator]):
    _attr_attribution: str
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: SkybellDataUpdateCoordinator, description: EntityDescription) -> None: ...
    @property
    def _device(self) -> SkybellDevice: ...
    async def async_added_to_hass(self) -> None: ...
