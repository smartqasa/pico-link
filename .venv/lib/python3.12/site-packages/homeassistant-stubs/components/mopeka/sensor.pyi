from . import MopekaConfigEntry as MopekaConfigEntry
from .device import device_key_to_bluetooth_entity_key as device_key_to_bluetooth_entity_key
from _typeshed import Incomplete
from homeassistant.components.bluetooth.passive_update_processor import PassiveBluetoothDataProcessor as PassiveBluetoothDataProcessor, PassiveBluetoothDataUpdate as PassiveBluetoothDataUpdate, PassiveBluetoothProcessorEntity as PassiveBluetoothProcessorEntity
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfLength as UnitOfLength, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.sensor import sensor_device_info_to_hass_device_info as sensor_device_info_to_hass_device_info
from mopeka_iot_ble import SensorUpdate

SENSOR_DESCRIPTIONS: Incomplete

def sensor_update_to_bluetooth_data_update(sensor_update: SensorUpdate) -> PassiveBluetoothDataUpdate: ...
async def async_setup_entry(hass: HomeAssistant, entry: MopekaConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MopekaBluetoothSensorEntity(PassiveBluetoothProcessorEntity[PassiveBluetoothDataProcessor[float | int | None, SensorUpdate]], SensorEntity):
    @property
    def native_value(self) -> int | float | None: ...
