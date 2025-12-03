from . import IBeaconConfigEntry as IBeaconConfigEntry
from .const import SIGNAL_IBEACON_DEVICE_NEW as SIGNAL_IBEACON_DEVICE_NEW
from .coordinator import IBeaconCoordinator as IBeaconCoordinator
from .entity import IBeaconEntity as IBeaconEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfLength as UnitOfLength
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from ibeacon_ble import iBeaconAdvertisement as iBeaconAdvertisement

@dataclass(frozen=True, kw_only=True)
class IBeaconSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[iBeaconAdvertisement], str | int | None]

SENSOR_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: IBeaconConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class IBeaconSensorEntity(IBeaconEntity, SensorEntity):
    entity_description: IBeaconSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: IBeaconCoordinator, description: IBeaconSensorEntityDescription, identifier: str, device_unique_id: str, ibeacon_advertisement: iBeaconAdvertisement) -> None: ...
    _attr_available: bool
    _ibeacon_advertisement: Incomplete
    @callback
    def _async_seen(self, ibeacon_advertisement: iBeaconAdvertisement) -> None: ...
    @callback
    def _async_unavailable(self) -> None: ...
    @property
    def native_value(self) -> str | int | None: ...
