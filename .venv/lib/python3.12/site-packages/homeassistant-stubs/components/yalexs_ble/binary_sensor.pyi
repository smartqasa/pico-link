from . import YALEXSBLEConfigEntry as YALEXSBLEConfigEntry
from .entity import YALEXSBLEEntity as YALEXSBLEEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from yalexs_ble import ConnectionInfo as ConnectionInfo, LockInfo as LockInfo, LockState as LockState

async def async_setup_entry(hass: HomeAssistant, entry: YALEXSBLEConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class YaleXSBLEDoorSensor(YALEXSBLEEntity, BinarySensorEntity):
    _attr_device_class: Incomplete
    _attr_is_on: Incomplete
    @callback
    def _async_update_state(self, new_state: LockState, lock_info: LockInfo, connection_info: ConnectionInfo) -> None: ...
