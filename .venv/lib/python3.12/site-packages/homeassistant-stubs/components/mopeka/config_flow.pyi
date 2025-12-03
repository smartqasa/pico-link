import voluptuous as vol
from .const import CONF_MEDIUM_TYPE as CONF_MEDIUM_TYPE, DEFAULT_MEDIUM_TYPE as DEFAULT_MEDIUM_TYPE, DOMAIN as DOMAIN, MediumType as MediumType
from _typeshed import Incomplete
from enum import Enum
from homeassistant import config_entries as config_entries
from homeassistant.components.bluetooth import BluetoothServiceInfoBleak as BluetoothServiceInfoBleak, async_discovered_service_info as async_discovered_service_info
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS
from homeassistant.core import callback as callback
from mopeka_iot_ble import MopekaIOTBluetoothDeviceData as DeviceData
from typing import Any

def format_medium_type(medium_type: Enum) -> str: ...

MEDIUM_TYPES_BY_NAME: Incomplete

def async_generate_schema(medium_type: str | None = None) -> vol.Schema: ...

class MopekaConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _discovery_info: BluetoothServiceInfoBleak | None
    _discovered_device: DeviceData | None
    _discovered_devices: dict[str, str]
    def __init__(self) -> None: ...
    @callback
    @staticmethod
    def async_get_options_flow(config_entry: config_entries.ConfigEntry) -> MopekaOptionsFlow: ...
    async def async_step_bluetooth(self, discovery_info: BluetoothServiceInfoBleak) -> ConfigFlowResult: ...
    async def async_step_bluetooth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class MopekaOptionsFlow(config_entries.OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
