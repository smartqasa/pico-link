from .coordinator import GoveeBLEConfigEntry as GoveeBLEConfigEntry, GoveeBLEPassiveBluetoothDataProcessor as GoveeBLEPassiveBluetoothDataProcessor
from .device import device_key_to_bluetooth_entity_key as device_key_to_bluetooth_entity_key
from _typeshed import Incomplete
from datetime import date, datetime
from decimal import Decimal
from govee_ble import SensorUpdate
from homeassistant.components.bluetooth.passive_update_processor import PassiveBluetoothDataProcessor as PassiveBluetoothDataProcessor, PassiveBluetoothDataUpdate as PassiveBluetoothDataUpdate, PassiveBluetoothProcessorEntity as PassiveBluetoothProcessorEntity
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.sensor import sensor_device_info_to_hass_device_info as sensor_device_info_to_hass_device_info

type _SensorValueType = str | int | float | date | datetime | Decimal | None
SENSOR_DESCRIPTIONS: Incomplete

def sensor_update_to_bluetooth_data_update(sensor_update: SensorUpdate) -> PassiveBluetoothDataUpdate[_SensorValueType]: ...
async def async_setup_entry(hass: HomeAssistant, entry: GoveeBLEConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class GoveeBluetoothSensorEntity(PassiveBluetoothProcessorEntity[PassiveBluetoothDataProcessor[_SensorValueType, SensorUpdate]], SensorEntity):
    processor: GoveeBLEPassiveBluetoothDataProcessor[_SensorValueType]
    @property
    def available(self) -> bool: ...
    @property
    def native_value(self) -> _SensorValueType: ...
