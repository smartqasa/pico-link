from homeassistant.components.bluetooth.passive_update_processor import PassiveBluetoothEntityKey as PassiveBluetoothEntityKey
from mopeka_iot_ble import DeviceKey as DeviceKey

def device_key_to_bluetooth_entity_key(device_key: DeviceKey) -> PassiveBluetoothEntityKey: ...
