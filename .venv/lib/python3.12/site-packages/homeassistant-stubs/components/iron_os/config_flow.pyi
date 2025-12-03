from .const import DISCOVERY_SVC_UUID as DISCOVERY_SVC_UUID, DOMAIN as DOMAIN
from habluetooth import BluetoothServiceInfoBleak as BluetoothServiceInfoBleak
from homeassistant.components.bluetooth.api import async_discovered_service_info as async_discovered_service_info
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS
from typing import Any

class IronOSConfigFlow(ConfigFlow, domain=DOMAIN):
    _discovery_info: BluetoothServiceInfoBleak | None
    _discovered_devices: dict[str, str]
    def __init__(self) -> None: ...
    async def async_step_bluetooth(self, discovery_info: BluetoothServiceInfoBleak) -> ConfigFlowResult: ...
    async def async_step_bluetooth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
