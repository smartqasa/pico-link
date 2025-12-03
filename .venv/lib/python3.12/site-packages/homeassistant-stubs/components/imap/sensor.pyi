from . import ImapConfigEntry as ImapConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import ImapDataUpdateCoordinator as ImapDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONF_USERNAME as CONF_USERNAME, EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

PARALLEL_UPDATES: int
IMAP_MAIL_COUNT_DESCRIPTION: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ImapConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ImapSensor(CoordinatorEntity[ImapDataUpdateCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: ImapDataUpdateCoordinator, description: SensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> int | None: ...
