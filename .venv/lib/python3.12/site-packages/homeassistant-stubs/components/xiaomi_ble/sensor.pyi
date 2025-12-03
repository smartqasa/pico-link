from .coordinator import XiaomiPassiveBluetoothDataProcessor as XiaomiPassiveBluetoothDataProcessor
from .device import device_key_to_bluetooth_entity_key as device_key_to_bluetooth_entity_key
from .types import XiaomiBLEConfigEntry as XiaomiBLEConfigEntry
from _typeshed import Incomplete
from homeassistant.components.bluetooth.passive_update_processor import PassiveBluetoothDataUpdate as PassiveBluetoothDataUpdate, PassiveBluetoothProcessorEntity as PassiveBluetoothProcessorEntity
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONCENTRATION_MILLIGRAMS_PER_CUBIC_METER as CONCENTRATION_MILLIGRAMS_PER_CUBIC_METER, EntityCategory as EntityCategory, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfConductivity as UnitOfConductivity, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfMass as UnitOfMass, UnitOfPressure as UnitOfPressure, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.sensor import sensor_device_info_to_hass_device_info as sensor_device_info_to_hass_device_info
from xiaomi_ble import SensorUpdate as SensorUpdate

SENSOR_DESCRIPTIONS: Incomplete

def sensor_update_to_bluetooth_data_update(sensor_update: SensorUpdate) -> PassiveBluetoothDataUpdate[float | None]: ...
async def async_setup_entry(hass: HomeAssistant, entry: XiaomiBLEConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class XiaomiBluetoothSensorEntity(PassiveBluetoothProcessorEntity[XiaomiPassiveBluetoothDataProcessor[float | None]], SensorEntity):
    @property
    def native_value(self) -> int | float | None: ...
    @property
    def available(self) -> bool: ...
