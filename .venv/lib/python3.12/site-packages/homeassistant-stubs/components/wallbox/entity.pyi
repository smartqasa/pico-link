from .const import CHARGER_CURRENT_VERSION_KEY as CHARGER_CURRENT_VERSION_KEY, CHARGER_DATA_KEY as CHARGER_DATA_KEY, CHARGER_NAME_KEY as CHARGER_NAME_KEY, CHARGER_PART_NUMBER_KEY as CHARGER_PART_NUMBER_KEY, CHARGER_SERIAL_NUMBER_KEY as CHARGER_SERIAL_NUMBER_KEY, CHARGER_SOFTWARE_KEY as CHARGER_SOFTWARE_KEY, DOMAIN as DOMAIN
from .coordinator import WallboxCoordinator as WallboxCoordinator
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class WallboxEntity(CoordinatorEntity[WallboxCoordinator]):
    _attr_has_entity_name: bool
    @property
    def device_info(self) -> DeviceInfo: ...
