from . import IBeaconConfigEntry as IBeaconConfigEntry
from .const import SIGNAL_IBEACON_DEVICE_NEW as SIGNAL_IBEACON_DEVICE_NEW
from .coordinator import IBeaconCoordinator as IBeaconCoordinator
from .entity import IBeaconEntity as IBeaconEntity
from _typeshed import Incomplete
from homeassistant.components.device_tracker import SourceType as SourceType
from homeassistant.components.device_tracker.config_entry import BaseTrackerEntity as BaseTrackerEntity
from homeassistant.const import STATE_HOME as STATE_HOME, STATE_NOT_HOME as STATE_NOT_HOME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from ibeacon_ble import iBeaconAdvertisement as iBeaconAdvertisement

async def async_setup_entry(hass: HomeAssistant, entry: IBeaconConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class IBeaconTrackerEntity(IBeaconEntity, BaseTrackerEntity):
    _attr_name: Incomplete
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    _active: bool
    def __init__(self, coordinator: IBeaconCoordinator, identifier: str, device_unique_id: str, ibeacon_advertisement: iBeaconAdvertisement) -> None: ...
    @property
    def state(self) -> str: ...
    @property
    def source_type(self) -> SourceType: ...
    _ibeacon_advertisement: Incomplete
    @callback
    def _async_seen(self, ibeacon_advertisement: iBeaconAdvertisement) -> None: ...
    @callback
    def _async_unavailable(self) -> None: ...
