from .coordinator import GoveeBLEPassiveBluetoothDataProcessor as GoveeBLEPassiveBluetoothDataProcessor
from .device import device_key_to_bluetooth_entity_key as device_key_to_bluetooth_entity_key
from _typeshed import Incomplete
from govee_ble import SensorUpdate
from homeassistant import config_entries as config_entries
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.components.bluetooth.passive_update_processor import PassiveBluetoothDataProcessor as PassiveBluetoothDataProcessor, PassiveBluetoothDataUpdate as PassiveBluetoothDataUpdate, PassiveBluetoothProcessorEntity as PassiveBluetoothProcessorEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.sensor import sensor_device_info_to_hass_device_info as sensor_device_info_to_hass_device_info

BINARY_SENSOR_DESCRIPTIONS: Incomplete

def sensor_update_to_bluetooth_data_update(sensor_update: SensorUpdate) -> PassiveBluetoothDataUpdate[bool | None]: ...
async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class GoveeBluetoothBinarySensorEntity(PassiveBluetoothProcessorEntity[PassiveBluetoothDataProcessor[bool | None, SensorUpdate]], BinarySensorEntity):
    processor: GoveeBLEPassiveBluetoothDataProcessor[bool | None]
    @property
    def available(self) -> bool: ...
    @property
    def is_on(self) -> bool | None: ...
