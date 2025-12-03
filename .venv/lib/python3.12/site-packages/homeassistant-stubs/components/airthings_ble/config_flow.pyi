import dataclasses
from .const import DOMAIN as DOMAIN, MFCT_ID as MFCT_ID
from _typeshed import Incomplete
from airthings_ble import AirthingsDevice as AirthingsDevice
from homeassistant.components import bluetooth as bluetooth
from homeassistant.components.bluetooth import BluetoothServiceInfo as BluetoothServiceInfo, async_discovered_service_info as async_discovered_service_info
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS
from typing import Any

_LOGGER: Incomplete
SERVICE_UUIDS: Incomplete

@dataclasses.dataclass
class Discovery:
    name: str
    discovery_info: BluetoothServiceInfo
    device: AirthingsDevice

def get_name(device: AirthingsDevice) -> str: ...

class AirthingsDeviceUpdateError(Exception): ...

class AirthingsConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _discovered_device: Discovery | None
    _discovered_devices: dict[str, Discovery]
    def __init__(self) -> None: ...
    async def _get_device_data(self, discovery_info: BluetoothServiceInfo) -> AirthingsDevice: ...
    async def async_step_bluetooth(self, discovery_info: BluetoothServiceInfo) -> ConfigFlowResult: ...
    async def async_step_bluetooth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
