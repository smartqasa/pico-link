import dataclasses
from .const import DOMAIN as DOMAIN
from bthome_ble import BTHomeBluetoothDeviceData as DeviceData
from collections.abc import Mapping
from homeassistant.components import onboarding as onboarding
from homeassistant.components.bluetooth import BluetoothServiceInfoBleak as BluetoothServiceInfoBleak, async_discovered_service_info as async_discovered_service_info
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS
from typing import Any

@dataclasses.dataclass
class Discovery:
    title: str
    discovery_info: BluetoothServiceInfoBleak
    device: DeviceData

def _title(discovery_info: BluetoothServiceInfoBleak, device: DeviceData) -> str: ...

class BTHomeConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _discovery_info: BluetoothServiceInfoBleak | None
    _discovered_device: DeviceData | None
    _discovered_devices: dict[str, Discovery]
    def __init__(self) -> None: ...
    async def async_step_bluetooth(self, discovery_info: BluetoothServiceInfoBleak) -> ConfigFlowResult: ...
    async def async_step_get_encryption_key(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_bluetooth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    def _async_get_or_create_entry(self, bindkey: str | None = None) -> ConfigFlowResult: ...
