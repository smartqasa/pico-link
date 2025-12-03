from .device_registry import DeviceInfo as DeviceInfo
from homeassistant import const as const
from sensor_state_data import SensorDeviceInfo as SensorDeviceInfo

def sensor_device_info_to_hass_device_info(sensor_device_info: SensorDeviceInfo) -> DeviceInfo: ...
