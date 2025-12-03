from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, MODELS as MODELS
from .coordinator import LaundrifyUpdateCoordinator as LaundrifyUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from laundrify_aio import LaundrifyDevice as LaundrifyDevice

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LaundrifyPowerPlug(CoordinatorEntity[LaundrifyUpdateCoordinator], BinarySensorEntity):
    _attr_device_class: Incomplete
    _attr_unique_id: str
    _attr_has_entity_name: bool
    _attr_translation_key: str
    _device: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: LaundrifyUpdateCoordinator, device: LaundrifyDevice) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def is_on(self) -> bool: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
