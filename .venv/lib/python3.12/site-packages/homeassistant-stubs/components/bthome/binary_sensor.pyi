from .coordinator import BTHomePassiveBluetoothDataProcessor as BTHomePassiveBluetoothDataProcessor
from .device import device_key_to_bluetooth_entity_key as device_key_to_bluetooth_entity_key
from .types import BTHomeConfigEntry as BTHomeConfigEntry
from _typeshed import Incomplete
from bthome_ble import SensorUpdate as SensorUpdate
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.components.bluetooth.passive_update_processor import PassiveBluetoothDataUpdate as PassiveBluetoothDataUpdate, PassiveBluetoothProcessorEntity as PassiveBluetoothProcessorEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.sensor import sensor_device_info_to_hass_device_info as sensor_device_info_to_hass_device_info

BINARY_SENSOR_DESCRIPTIONS: Incomplete

def sensor_update_to_bluetooth_data_update(sensor_update: SensorUpdate) -> PassiveBluetoothDataUpdate[bool | None]: ...
async def async_setup_entry(hass: HomeAssistant, entry: BTHomeConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BTHomeBluetoothBinarySensorEntity(PassiveBluetoothProcessorEntity[BTHomePassiveBluetoothDataProcessor[bool | None]], BinarySensorEntity):
    @property
    def is_on(self) -> bool | None: ...
    @property
    def available(self) -> bool: ...
