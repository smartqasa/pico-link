from .entity import BasePrivateDeviceEntity as BasePrivateDeviceEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components import bluetooth as bluetooth
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfLength as UnitOfLength, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class PrivateDeviceSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[HomeAssistant, bluetooth.BluetoothServiceInfoBleak], str | int | float | None]

SENSOR_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PrivateBLEDeviceSensor(BasePrivateDeviceEntity, SensorEntity):
    entity_description: PrivateDeviceSensorEntityDescription
    _attr_available: bool
    def __init__(self, config_entry: ConfigEntry, entity_description: PrivateDeviceSensorEntityDescription) -> None: ...
    _last_info: Incomplete
    @callback
    def _async_track_service_info(self, service_info: bluetooth.BluetoothServiceInfoBleak, change: bluetooth.BluetoothChange) -> None: ...
    @callback
    def _async_track_unavailable(self, service_info: bluetooth.BluetoothServiceInfoBleak) -> None: ...
    @property
    def native_value(self) -> str | int | float | None: ...
