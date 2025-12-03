from .const import CONF_IS_NEW_STYLE_SCALE as CONF_IS_NEW_STYLE_SCALE, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.bluetooth import BluetoothServiceInfoBleak as BluetoothServiceInfoBleak, async_discovered_service_info as async_discovered_service_info
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, CONF_NAME as CONF_NAME
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.selector import SelectOptionDict as SelectOptionDict, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode
from typing import Any

_LOGGER: Incomplete

class AcaiaConfigFlow(ConfigFlow, domain=DOMAIN):
    _discovered: dict[str, Any]
    _discovered_devices: dict[str, str]
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_bluetooth(self, discovery_info: BluetoothServiceInfoBleak) -> ConfigFlowResult: ...
    async def async_step_bluetooth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
