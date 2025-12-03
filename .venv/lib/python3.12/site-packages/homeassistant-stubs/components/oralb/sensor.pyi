from . import OralBConfigEntry as OralBConfigEntry
from .device import device_key_to_bluetooth_entity_key as device_key_to_bluetooth_entity_key
from homeassistant.components.bluetooth.passive_update_processor import PassiveBluetoothDataProcessor as PassiveBluetoothDataProcessor, PassiveBluetoothDataUpdate as PassiveBluetoothDataUpdate, PassiveBluetoothProcessorEntity as PassiveBluetoothProcessorEntity
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.sensor import sensor_device_info_to_hass_device_info as sensor_device_info_to_hass_device_info
from oralb_ble import SensorUpdate

SENSOR_DESCRIPTIONS: dict[str, SensorEntityDescription]

def sensor_update_to_bluetooth_data_update(sensor_update: SensorUpdate) -> PassiveBluetoothDataUpdate: ...
async def async_setup_entry(hass: HomeAssistant, entry: OralBConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OralBBluetoothSensorEntity(PassiveBluetoothProcessorEntity[PassiveBluetoothDataProcessor[str | int | None, SensorUpdate]], SensorEntity):
    @property
    def native_value(self) -> str | int | None: ...
    @property
    def available(self) -> bool: ...
    @property
    def assumed_state(self) -> bool: ...
