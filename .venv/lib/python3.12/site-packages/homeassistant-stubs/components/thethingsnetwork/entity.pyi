from .const import DOMAIN as DOMAIN
from .coordinator import TTNCoordinator as TTNCoordinator
from _typeshed import Incomplete
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from ttn_client import TTNBaseValue as TTNBaseValue

_LOGGER: Incomplete

class TTNEntity(CoordinatorEntity[TTNCoordinator]):
    _attr_has_entity_name: bool
    _ttn_value: TTNBaseValue
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: TTNCoordinator, app_id: str, ttn_value: TTNBaseValue) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    @property
    def device_id(self) -> str: ...
    @property
    def field_id(self) -> str: ...
