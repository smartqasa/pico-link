from .coordinator import BTHomePassiveBluetoothDataProcessor as BTHomePassiveBluetoothDataProcessor
from .device import device_key_to_bluetooth_entity_key as device_key_to_bluetooth_entity_key
from .types import BTHomeConfigEntry as BTHomeConfigEntry
from _typeshed import Incomplete
from bthome_ble import SensorUpdate as SensorUpdate
from homeassistant.components.bluetooth.passive_update_processor import PassiveBluetoothDataUpdate as PassiveBluetoothDataUpdate, PassiveBluetoothProcessorEntity as PassiveBluetoothProcessorEntity
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, DEGREE as DEGREE, EntityCategory as EntityCategory, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfConductivity as UnitOfConductivity, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfLength as UnitOfLength, UnitOfMass as UnitOfMass, UnitOfPower as UnitOfPower, UnitOfPressure as UnitOfPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime, UnitOfVolume as UnitOfVolume, UnitOfVolumeFlowRate as UnitOfVolumeFlowRate
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.sensor import sensor_device_info_to_hass_device_info as sensor_device_info_to_hass_device_info

SENSOR_DESCRIPTIONS: Incomplete

def sensor_update_to_bluetooth_data_update(sensor_update: SensorUpdate) -> PassiveBluetoothDataUpdate[float | None]: ...
async def async_setup_entry(hass: HomeAssistant, entry: BTHomeConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BTHomeBluetoothSensorEntity(PassiveBluetoothProcessorEntity[BTHomePassiveBluetoothDataProcessor[float | None]], SensorEntity):
    @property
    def native_value(self) -> int | float | None: ...
    @property
    def available(self) -> bool: ...
